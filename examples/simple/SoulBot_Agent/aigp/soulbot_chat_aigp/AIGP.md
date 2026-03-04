---
# AIGP Governance Contract
# 治理字段 (6 个必需)
protocol: "AIGP V1.0.0"
authority: aigp.dev
seed: aisop.dev
executor: soulbot.dev
axiom_0: Human_Sovereignty_and_Benefit
governance_mode: NORMAL

# 项目字段 (6 个必需)
name: soulbot_chat
version: "1.0.0"
pattern: E
summary: "SoulBot Chat — core conversation and user cognition engine with proactive companion behaviors. Manages all dialogue with token budget management, structured context handoff, feedback learning loop, records conversations, builds user profiles through fractal emotion/preference/habit analysis, supports direct profile editing, session summaries, satisfaction signal extraction with repair loop, emotion causality tracking with values-aware advice, multi-language crisis detection with abuse pattern recognition, and enforces graduated safety compliance."
tools:
  - name: file_system
    required: true
    annotations:
      read_only: false
      destructive: false
      idempotent: false
      open_world: false
  - name: google_search
    required: false
    fallback: "degrade"
    annotations:
      read_only: true
      destructive: false
      idempotent: true
      open_world: true
  - name: web_browser
    required: false
    fallback: "degrade"
    annotations:
      read_only: true
      destructive: false
      idempotent: true
      open_world: true
modules:
  - id: soulbot_chat.main
    file: main.aisop.json
    nodes: 17
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: soulbot_chat.conversation
    file: conversation.aisop.json
    nodes: 11
    critical: true
    idempotent: true
    side_effects: []
  - id: soulbot_chat.memory
    file: memory.aisop.json
    nodes: 12
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: soulbot_chat.profiler
    file: profiler.aisop.json
    nodes: 12
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: soulbot_chat.safety
    file: safety.aisop.json
    nodes: 13
    critical: true
    idempotent: true
    side_effects: []

# 基础可选字段
identity:
  program_id: "soulbot.dev/soulbot_chat"
  publisher: "soulbot.dev"
  verified_on: "2026-03-03"
governance_hash: 8a06ac6a748bc8e283c0db598fa3aebe7e29782be0e238735b7435cdde9dadb6
quality:
  weighted_score: 5.00
  grade: S
  last_pipeline: "Quality: Safety Hardening & Interaction Quality. 65 nodes, 58 scenarios, 0 YELLOW, 0 RED."
tags: [soulbot, chat, conversation, memory, profiling, safety, cognition, companion]
author: AIGP Protocol Organization
license: Apache-2.0
copyright: "Copyright 2026 AISOP.dev | AIGP.dev | SoulBot.dev"

# 安全与运行时可选字段
trust_level:
  level: 3
  justification: "file_system read/write limited to memory_dir (./memory/). Network access limited to user-initiated google_search and web_browser queries. No autonomous destructive operations. Safety module operates with zero tools (T1-equivalent)."
  constraints:
    - "file_system write scope limited to memory_dir (./memory/)"
    - "network access limited to *.google.com and *.bing.com for user-initiated queries"
    - "no autonomous file deletion — GDPR delete requires explicit user confirmation gate"
    - "crisis_check outputs resource references only — never provides diagnosis or emergency services"
permissions:
  file_system:
    scope: "./memory/"
    operations: ["read", "write"]
  network:
    allowed: true
    endpoints: ["*.google.com", "*.bing.com"]
runtime:
  timeout_seconds: 300
  max_retries: 3
  token_budget: 80000
  idempotent: false
  side_effects: [file_write]
capabilities:
  offered:
    - file_write
    - search
    - state_persistence
    - user_profiling
  required:
    - file_read
ui:
  components:
    - type: dashboard
      title: "Session Overview"
      data_source: working_memory
      refresh: "on_event"
    - type: form
      title: "User Preferences"
      fields:
        - { name: communication_style, type: select, options: [formal, casual, playful], default: casual }
        - { name: response_verbosity, type: select, options: [concise, balanced, detailed], default: balanced }
        - { name: minor_mode, type: boolean, default: false }
    - type: visualization
      title: "Mood Trend"
      chart_type: line
      data_source: emotion_history
  rendering: "mcp_apps_v1"

# 工程化可选字段
status: active
applicability_condition:
  triggers:
    - "user initiates conversation or sends a chat message"
    - "user asks a factual question requiring search"
    - "user expresses emotion or seeks comfort"
    - "user requests memory recall of past conversations"
    - "user asks about their learned preferences or profile"
    - "user initiates creative collaboration or storytelling"
    - "user provides feedback or correction"
    - "user requests data export or deletion (GDPR)"
    - "user requests direct profile attribute modification"
  preconditions:
    - "memory_dir exists and is writable"
    - "file_system tool available"
    - "routed by SoulBot top-level router to soulbot_chat"
  exclusions:
    - "non-conversation AIGP tasks handled by other specialized modules"
    - "direct file operations unrelated to chat memory"
    - "system administration or AIGP program management tasks"
  confidence_threshold: 0.8
intent_examples:
  - "你好，今天心情怎么样？"
  - "帮我查一下明天的天气"
  - "我最近感觉很焦虑"
  - "你还记得我上次说的旅行计划吗？"
  - "你对我了解多少？"
  - "我们来编个故事吧"
  - "我觉得你刚才理解错了"
  - "把我的名字改成小明"
  - "今天聊得挺开心，再见！"
discovery_keywords: [soulbot, chat, conversation, companion, memory, profiling, emotion, safety]
dependencies: []
min_protocol_version: "AIGP V1.0.0"
benchmark:
  threedimscore: 5.00
  simulation_coverage: "A(10)+B(15)+C(3)+D(5)+E(5)+I(3)+E.injection(AT1-AT6)+L(2)+K(3)+F(6) = 58 scenarios"
  pass_rate: "58/58 GREEN (100%), 0 YELLOW, 0 RED"
---

## 治理声明

SoulBot Chat 是 SoulBot 生态系统的核心对话与用户认知引擎。本程序遵循 AIGP V1.0.0 协议，
以 Axiom 0 (Human Sovereignty and Benefit) 为不可变公理，通过三域治理链
(aisop.dev → aigp.dev → soulbot.dev) 确保所有交互对齐人类主权与福祉。

SoulBot Chat 不仅是一个对话系统，更是用户理解的核心——记录所有对话历史，分形分析用户
情绪、偏好、习惯，构建全面的用户认知画像。

## 功能概述

SoulBot Chat 通过 Pattern E (Package + memory/) 架构管理对话与用户认知的完整生命周期：

| 模块 | 职责 | 工具 |
|------|------|------|
| **main.aisop.json** | 无状态路由器 — 11意图分类(15混淆对) + 安全双关卡 + 会话管理 + 数据隐私 + 主动陪伴 + 会话总结 + 满意度信号提取 + token预算管理 + 结构化上下文传递 + **空消息防护(Y1)** + **SessionEnd意图(Y2)** | file_system, google_search, web_browser |
| **conversation.aisop.json** | 对话引擎 — 多轮对话、信息查询、情感支持、创意协作、价值观建议框架、满意度修复、讽刺消歧 + 预算感知简洁模式 + 结构化响应返回 + 反馈修正消费 + **优雅错误恢复(B2)** + **降级模式(B2)** | google_search, web_browser |
| **memory.aisop.json** | 记忆管理器 — 工作/情景/语义三层记忆、语义相关性排序、整合、衰减、主动回忆、会话总结 + 预算紧张激进摘要 + .bak恢复 + 实体关系图谱 + 层级摘要 + 上下文腐蚀防护 + **选择性上下文注入(B3)** + **乐观锁(Y4)** + **文件锁(Y6)** | file_system |
| **profiler.aisop.json** | 用户画像 — 情绪检测、因果追踪、偏好学习、习惯识别、满意度追踪、认知地图 + 反馈修正存储与衰减 + **交互质量监控(B4)** + **emotion_display修复(Y5)** | file_system |
| **safety.aisop.json** | 安全卫士 — 输入/输出筛查、分级危机干预(LOW/MEDIUM/HIGH)、多语言危机检测(6语言)、虐待模式识别、未成年人保护 + 宪法AI原则与自我批判 + **注入检测器(B1)** + **速率限制器(Y3)** | (零工具) |

### 记忆架构 (Pattern E)

```
memory/
  working.json              — 当前会话状态 (滑动窗口 + 摘要)
  working.json.bak          — 自动备份 (用于损坏恢复)
  episodic/                 — 按会话的完整对话日志
  semantic/                 — 提取的持久化用户知识
  semantic/{user_id}/relationships.json — 实体关系图谱 ({subject, relation, object, confidence})
  profiles/                 — 用户画像文档
```

### 安全合规

- **California SB 243**: 每3小时 AI 身份披露、未成年人保护、危机检测
- **EU AI Act Article 50**: AI 交互透明度
- **GDPR**: 数据最小化、删除权、导出权
- **三层安全**: 输入筛查 → 处理约束 → 输出过滤

## 使用方式

### 入口文件

`main.aisop.json` — 由顶级 SoulBot 路由器分发聊天意图后激活。

### 工具需求

| 工具 | 必需 | 用途 |
|------|------|------|
| file_system | 是 | 记忆持久化 (读写用户画像、对话日志) |
| google_search | 否 | 用户提问时搜索信息 |
| web_browser | 否 | 阅读用户分享的链接 |

### 前置条件

- 由 SoulBot 顶级 main.aisop.json 路由到本程序
- memory/ 目录已创建且可写
- AI Agent 支持 file_system 工具

## 示例交互

**场景 1: 日常对话**
- 用户: "你好，今天过得怎么样？"
- Agent: 温暖回应 → 记录对话 → 更新情绪画像

**场景 2: 信息查询**
- 用户: "帮我查一下量子计算的最新进展"
- Agent: google_search 查询 → 整理回答 → 标注来源

**场景 3: 情感支持**
- 用户: "最近工作压力很大，不知道该怎么办"
- Agent: 共情回应 → 检测情绪 → 更新情绪轨迹 → 提供非处方建议

**场景 4: 记忆回溯**
- 用户: "你还记得我上次提到的那本书吗？"
- Agent: 搜索情景记忆 → 找到相关对话 → 回复上下文

**场景 5: 危机干预**
- 用户: 表达自伤倾向
- Agent: 立即提供危机资源 (988 生命线) → 不提供诊断 → 建议专业帮助

## 适用条件

**适用**: 所有对话场景 — 闲聊、信息查询、情感支持、创意协作、记忆管理、用户画像
**不适用**: 非对话类 AIGP 任务 (那些由顶级路由器分发到其他专业 AIGP 处理)

---

Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev
