<script setup lang="ts">
import { computed } from 'vue'
import { marked } from 'marked'

const props = defineProps<{
  type: 'user' | 'agent' | 'tool-call' | 'tool-response' | 'transfer' | 'error' | 'thinking'
  author: string
  text: string
  streaming?: boolean
  timestamp?: number
}>()

marked.use({ breaks: true, gfm: true })

const renderedText = computed(() => {
  if (props.type === 'agent') {
    return marked.parse(props.text) as string
  }
  return props.text
})

const isMarkdown = computed(() => props.type === 'agent')

const timeStr = computed(() => {
  if (!props.timestamp) return ''
  const d = new Date(props.timestamp * 1000)
  return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
})
</script>

<template>
  <div class="msg" :class="[type, { streaming }]">
    <div class="msg-author" :class="{ 'streaming-dot': streaming }">
      {{ author }}<span v-if="timeStr" class="msg-time">{{ timeStr }}</span>
    </div>
    <div v-if="type === 'thinking'" class="msg-text">
      <div class="thinking-dots"><span></span><span></span><span></span></div>
    </div>
    <div v-else-if="isMarkdown" class="msg-text markdown-body" v-html="renderedText"></div>
    <div v-else class="msg-text">{{ text }}</div>
  </div>
</template>

<style scoped>
.msg {
  max-width: 80%;
  padding: 10px 14px;
  border-radius: 12px;
  font-size: 14px;
  line-height: 1.5;
  word-wrap: break-word;
}

.msg.user {
  align-self: flex-end;
  background: var(--user-bg);
  border-bottom-right-radius: 2px;
}

.msg.agent {
  align-self: flex-start;
  background: var(--agent-bg);
  border: 1px solid var(--border);
  border-bottom-left-radius: 2px;
}

.msg.tool-call {
  align-self: flex-start;
  background: var(--tool-bg);
  border: 1px solid #3a2a5c;
  font-family: var(--mono);
  font-size: 12px;
  max-width: 90%;
}

.msg.tool-response {
  align-self: flex-start;
  background: var(--tool-bg);
  border: 1px solid #3a2a5c;
  font-family: var(--mono);
  font-size: 12px;
  color: var(--text-muted);
  max-width: 90%;
}

.msg.transfer {
  align-self: center;
  background: var(--transfer-bg);
  border: 1px solid #2a5c3a;
  font-size: 12px;
  text-align: center;
  color: var(--accent);
  max-width: 100%;
}

.msg.error {
  align-self: flex-start;
  background: #2a1a1a;
  border: 1px solid var(--error);
  color: var(--error);
  font-size: 12px;
}

.msg.thinking {
  align-self: flex-start;
  background: var(--agent-bg);
  border: 1px solid var(--border);
  border-bottom-left-radius: 2px;
}

.msg-author {
  font-size: 11px;
  color: var(--text-muted);
  margin-bottom: 4px;
}

.msg-time {
  margin-left: 8px;
  opacity: 0.6;
}

.msg-text {
  white-space: pre-wrap;
}

.msg-text.markdown-body {
  white-space: normal;
}
</style>
