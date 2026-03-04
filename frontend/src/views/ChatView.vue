<script setup lang="ts">
import { ref, watch, nextTick, onMounted } from 'vue'
import { useAgentStore } from '@/stores/agent'
import { useSessionStore } from '@/stores/session'
import { useSSE } from '@/composables/useSSE'
import ChatMessage from '@/components/chat/ChatMessage.vue'
import SessionList from '@/components/chat/SessionList.vue'
import type { AgentEvent } from '@/types'

interface ChatMsg {
  type: 'user' | 'agent' | 'tool-call' | 'tool-response' | 'transfer' | 'error' | 'thinking'
  author: string
  text: string
  streaming?: boolean
  timestamp?: number
}

const agentStore = useAgentStore()
const sessionStore = useSessionStore()
const { isStreaming, error: sseError, sendMessage } = useSSE()

const messages = ref<ChatMsg[]>([])
const inputText = ref('')
const chatContainer = ref<HTMLElement | null>(null)
const inputRef = ref<HTMLInputElement | null>(null)
const agentSelect = ref<string>('')

// Initialize
onMounted(async () => {
  inputRef.value?.focus()
  await agentStore.loadAgents()
  if (agentStore.currentAgent) {
    agentSelect.value = agentStore.currentAgent
    await sessionStore.loadSessions(agentStore.currentAgent)
    await loadChatHistory()
  }
})

// Watch session changes to load chat history (immediate: covers mount case)
watch(() => sessionStore.currentSessionId, async (newId) => {
  if (!newId || !agentStore.currentAgent) return
  await loadChatHistory()
}, { immediate: true })

async function loadChatHistory() {
  if (!agentStore.currentAgent || !sessionStore.currentSessionId) return

  try {
    const detail = await sessionStore.getSessionDetail(
      agentStore.currentAgent,
      sessionStore.currentSessionId
    )

    // Auto-switch agent to match session
    if (detail.last_agent && agentStore.agents.includes(detail.last_agent)) {
      agentStore.selectAgent(detail.last_agent)
      agentSelect.value = detail.last_agent
    }

    // Build messages from events
    const msgs: ChatMsg[] = []
    for (const ev of detail.events) {
      if (ev.partial) continue
      for (const part of ev.content?.parts || []) {
        if (part.text) {
          msgs.push({
            type: ev.author === 'user' ? 'user' : 'agent',
            author: ev.author || '?',
            text: part.text,
            timestamp: ev.timestamp,
          })
        }
        if (part.function_call) {
          msgs.push({
            type: 'tool-call',
            author: ev.author || 'agent',
            text: `Calling: ${part.function_call.name}(${JSON.stringify(part.function_call.args)})`,
            timestamp: ev.timestamp,
          })
        }
        if (part.function_response) {
          msgs.push({
            type: 'tool-response',
            author: part.function_response.name,
            text: JSON.stringify(part.function_response.response, null, 2),
            timestamp: ev.timestamp,
          })
        }
      }
      if (ev.actions?.transfer_to_agent) {
        msgs.push({
          type: 'transfer',
          author: 'system',
          text: `Transferred to: ${ev.actions.transfer_to_agent}`,
          timestamp: ev.timestamp,
        })
      }
      if (ev.error_code) {
        msgs.push({
          type: 'error',
          author: ev.author || 'error',
          text: `${ev.error_code}: ${ev.error_message || ''}`,
          timestamp: ev.timestamp,
        })
      }
    }
    messages.value = msgs
    await scrollToBottom()
  } catch {
    // Session might not exist yet
    messages.value = []
  }
}

async function onSubmit() {
  const text = inputText.value.trim()
  if (!text || !agentStore.currentAgent || !sessionStore.currentSessionId) return
  if (isStreaming.value) return

  inputText.value = ''
  const now = Date.now() / 1000
  messages.value.push({ type: 'user', author: 'You', text, timestamp: now })

  // Show thinking placeholder immediately so user knows the agent is working
  const agentName = agentStore.currentAgent || 'agent'
  messages.value.push({ type: 'thinking', author: agentName, text: '' })
  const thinkingIdx = messages.value.length - 1
  await scrollToBottom()

  // Streaming agent response
  let streamingIdx = -1
  let streamingText = ''
  let thinkingRemoved = false

  function removeThinking() {
    if (!thinkingRemoved && messages.value[thinkingIdx]?.type === 'thinking') {
      messages.value.splice(thinkingIdx, 1)
      thinkingRemoved = true
    }
  }

  await sendMessage(
    agentStore.currentAgent,
    'default',
    sessionStore.currentSessionId,
    text,
    (event: AgentEvent) => {
      removeThinking()
      for (const part of event.content?.parts || []) {
        if (part.function_call) {
          messages.value.push({
            type: 'tool-call',
            author: event.author || 'agent',
            text: `Calling: ${part.function_call.name}(${JSON.stringify(part.function_call.args)})`,
            timestamp: event.timestamp,
          })
          scrollToBottom()
          continue
        }
        if (part.function_response) {
          messages.value.push({
            type: 'tool-response',
            author: part.function_response.name,
            text: JSON.stringify(part.function_response.response, null, 2),
            timestamp: event.timestamp,
          })
          scrollToBottom()
          continue
        }
        if (part.text) {
          if (event.partial) {
            streamingText += part.text
            if (streamingIdx === -1) {
              messages.value.push({
                type: 'agent',
                author: event.author || 'agent',
                text: streamingText,
                streaming: true,
                timestamp: event.timestamp,
              })
              streamingIdx = messages.value.length - 1
            } else {
              messages.value[streamingIdx]!.text = streamingText
            }
          } else {
            // Final (complete) event — use its text as the definitive version
            if (streamingIdx !== -1) {
              messages.value[streamingIdx]!.text = part.text || streamingText
              messages.value[streamingIdx]!.streaming = false
              streamingIdx = -1
              streamingText = ''
            } else {
              messages.value.push({
                type: 'agent',
                author: event.author || 'agent',
                text: part.text,
                timestamp: event.timestamp,
              })
            }
          }
          scrollToBottom()
        }
      }
      if (event.actions?.transfer_to_agent) {
        messages.value.push({
          type: 'transfer',
          author: 'system',
          text: `Transferring to: ${event.actions.transfer_to_agent}`,
          timestamp: event.timestamp,
        })
        scrollToBottom()
      }
      if (event.error_code) {
        messages.value.push({
          type: 'error',
          author: event.author || 'error',
          text: `${event.error_code}: ${event.error_message || ''}`,
          timestamp: event.timestamp,
        })
        scrollToBottom()
      }
    }
  )

  // Clean up: remove thinking placeholder if still present (e.g. empty response or error)
  removeThinking()

  // Finalize streaming
  if (streamingIdx !== -1) {
    messages.value[streamingIdx]!.streaming = false
  }

  // Refresh session list to update timestamps
  if (agentStore.currentAgent) {
    await sessionStore.loadSessions(agentStore.currentAgent)
  }

  await nextTick()
  inputRef.value?.focus()
}

async function onAgentChange() {
  agentStore.selectAgent(agentSelect.value)
  messages.value = []
  sessionStore.selectSession(null)  // reset so loadSessions auto-selects
  await sessionStore.loadSessions(agentSelect.value)
  await loadChatHistory()
}

async function scrollToBottom() {
  await nextTick()
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  }
}
</script>

<template>
  <div class="chat-layout">
    <!-- Session sidebar -->
    <div class="chat-sidebar">
      <div class="agent-select-row">
        <span class="label">Agent</span>
        <select v-model="agentSelect" @change="onAgentChange" class="agent-select">
          <option v-for="a in agentStore.agents" :key="a" :value="a">{{ a }}</option>
        </select>
      </div>
      <SessionList />
    </div>

    <!-- Chat main area -->
    <div class="chat-main">
      <div class="chat-messages" ref="chatContainer">
        <ChatMessage
          v-for="(msg, idx) in messages"
          :key="idx"
          :type="msg.type"
          :author="msg.author"
          :text="msg.text"
          :streaming="msg.streaming"
          :timestamp="msg.timestamp"
        />
        <div v-if="messages.length === 0" class="chat-empty">
          Start a conversation...
        </div>
      </div>

      <div v-if="sseError" class="chat-error">{{ sseError }}</div>

      <form class="chat-form" @submit.prevent="onSubmit">
        <input
          ref="inputRef"
          v-model="inputText"
          class="chat-input"
          placeholder="Type a message..."
          autocomplete="off"
          :disabled="isStreaming"
        />
        <button type="submit" class="btn-send" :disabled="isStreaming || !inputText.trim()">
          {{ isStreaming ? '...' : 'Send' }}
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.chat-layout {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.chat-sidebar {
  width: var(--sidebar-width);
  display: flex;
  flex-direction: column;
  border-right: 1px solid var(--border);
  flex-shrink: 0;
}

.agent-select-row {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-secondary);
}

.agent-select-row .label {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: var(--text-muted);
  flex-shrink: 0;
}

.agent-select {
  flex: 1;
  background: var(--bg-card);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 4px 8px;
  font-size: 12px;
}

.chat-main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.chat-empty {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  color: var(--text-muted);
  font-size: 14px;
}

.chat-error {
  padding: 8px 16px;
  background: #2a1a1a;
  color: var(--error);
  font-size: 12px;
  border-top: 1px solid var(--error);
}

.chat-form {
  display: flex;
  padding: 12px;
  gap: 8px;
  background: var(--bg-secondary);
  border-top: 1px solid var(--border);
}

.chat-input {
  flex: 1;
  padding: 10px 14px;
  background: var(--bg-card);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  font-size: 14px;
  outline: none;
  font-family: var(--font);
}
.chat-input:focus { border-color: var(--accent); }

.btn-send {
  padding: 10px 20px;
  background: var(--accent);
  color: var(--bg);
  border: none;
  border-radius: var(--radius);
  font-weight: 600;
  cursor: pointer;
  font-size: 14px;
  font-family: var(--font);
}
.btn-send:hover { background: var(--accent-hover); }
.btn-send:disabled { opacity: 0.5; cursor: not-allowed; }
</style>
