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
name: aigp_creator
version: "1.0.0"
pattern: D+G
summary: "AIGP Creator — creates, evolves, discovers, deprecates, validates, and simulates AIGP programs through a 14-stage pipeline. Supports YellowFixProposalGenerator, D8-LICENSE semantic check, D4-RANGE cross-reference staleness detection, domain-specific quality research, PostSimulateGate yellow_fix_proposals consumption, ValidateStep LICENSE COMPLIANCE CHECK, Pattern G embedded runtime with Code Trust Gate, auto-fix protocol, YELLOW remediation, MCP tool adapter, federated registry, capability negotiation, AIGP packaging, UI component generation, multi-language tool directory generation, and comprehensive quality intelligence."
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
  - id: aigp_creator.main
    file: main.aisop.json
    nodes: 27
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: aigp_creator.generate
    file: generate.aisop.json
    nodes: 10
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: aigp_creator.research
    file: research.aisop.json
    nodes: 15
    critical: false
    idempotent: true
    side_effects: []
  - id: aigp_creator.modify
    file: modify.aisop.json
    nodes: 9
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: aigp_creator.review
    file: review.aisop.json
    nodes: 11
    critical: true
    idempotent: false
    side_effects: [file_write]
  - id: aigp_creator.simulate
    file: simulate.aisop.json
    nodes: 10
    critical: false
    idempotent: true
    side_effects: []
  - id: aigp_creator.observability
    file: observability.aisop.json
    nodes: 9
    critical: false
    idempotent: true
    side_effects: []
  - id: aigp_creator.advisor
    file: advisor.aisop.json
    nodes: 52
    critical: false
    idempotent: false
    side_effects: [file_write]
  - id: aigp_creator.standard_core
    file: AIGP_Standard.core.aisop.json
    nodes: 0
    critical: true
    idempotent: true
    side_effects: []
  - id: aigp_creator.standard_security
    file: AIGP_Standard.security.aisop.json
    nodes: 0
    critical: true
    idempotent: true
    side_effects: []
  - id: aigp_creator.standard_ecosystem
    file: AIGP_Standard.ecosystem.aisop.json
    nodes: 0
    critical: false
    idempotent: true
    side_effects: []
  - id: aigp_creator.standard_performance
    file: AIGP_Standard.performance.aisop.json
    nodes: 0
    critical: false
    idempotent: true
    side_effects: []

# 基础可选字段
governance_hash: 0aaa80977242a967fede7c33dd64b4b3b477d1098bceed2684cbeb8a9480c673
quality:
  weighted_score: 5.000
  grade: S
  last_pipeline: "Quality Intelligence Enhancement: YellowFixProposalGenerator, D8-LICENSE semantic check, D4-RANGE cross-reference staleness detection, domain-specific quality research, competitive landscape analysis. PostSimulateGate yellow_fix_proposals consumption with 4 user action options. ValidateStep LICENSE COMPLIANCE CHECK with PL25 enforcement. range_reference_consistency rule in AIGP_Standard.core. competitive_insights data contract in research_context."
tags: [aigp, creator, pipeline, governance, meta]
author: AIGP Protocol Organization
license: Apache-2.0
copyright: "Copyright 2026 AISOP.dev | AIGP.dev | SoulBot.dev"

# 安全与运行时可选字段
trust_level:
  level: 4
  justification: "AIGP Creator requires full read/write access to workspace for creating, evolving, and modifying AIGP programs. Network access needed for research stages (google_search, web_browser)."
  constraints:
    - "file_system write scope limited to workspace_dir"
    - "network access limited to *.google.com and *.bing.com"
permissions:
  file_system:
    scope: "./"
    operations: ["read", "write"]
  network:
    allowed: true
    endpoints: ["*.google.com", "*.bing.com"]
runtime:
  timeout_seconds: 600
  max_retries: 3
  token_budget: 100000
  idempotent: false
  side_effects: [file_write]
capabilities:
  offered:
    - file_write
    - search
    - state_persistence
    - code_generation
  required:
    - file_read
ui:
  components:
    - type: dashboard
      title: "Pipeline Progress"
      data_source: pipeline_metadata
      refresh: "on_event"
    - type: form
      title: "Configuration"
      fields:
        - { name: quality_threshold, type: select, options: [strict, standard, relaxed], default: standard }
        - { name: research_mode, type: select, options: [structure, quality, compliance] }
    - type: visualization
      title: "Quality Trend"
      chart_type: line
      data_source: quality_baseline
  rendering: "mcp_apps_v1"

# 工程化可选字段
status: active
applicability_condition:
  triggers:
    - "user asks to create a new AIGP program"
    - "user asks to evolve an existing AIGP program"
    - "user asks to validate or simulate an AIGP program"
    - "user asks to modify a specific AIGP module"
    - "file with .aisop.json extension detected in workspace"
    - "user asks to discover or search for existing AIGP programs"
    - "user asks to deprecate or archive an AIGP program"
    - "user asks to export an AIGP program to SKILL.md format"
    - "user asks to import a SKILL.md file as an AIGP program"
    - "user asks to map AIGP tools to MCP protocol"
    - "user asks to discover programs from a remote registry"
    - "user asks to pack or package an AIGP program"
    - "user asks to unpack or verify a .aigp archive"
    - "user asks about UI components or dashboard for an AIGP program"
  preconditions:
    - "AIGP_Standard.core.aisop.json and extension files accessible in workspace"
    - "AIGP_Protocol.md accessible in workspace"
    - "workspace_dir writable"
  exclusions:
    - "input is not related to AIGP/AISOP format"
    - "user requests direct execution of an AIGP program (SoulBot executor responsibility)"
    - "target project uses non-AISOP format"
  confidence_threshold: 0.8
intent_examples:
  - "创建一个健康追踪 AIGP 程序"
  - "将 health_tracker 从 v1.1 进化到 v1.2"
  - "修改 recipe_finder 的搜索模块"
  - "验证 expense_tracker 的代码质量"
  - "模拟 travel_planner 的执行路径"
  - "查找有没有健康相关的 AIGP 程序"
  - "弃用 old_tracker 程序"
  - "将 recipe_finder 导出为 SKILL.md"
  - "从 SKILL.md 导入一个技能作为 AIGP 程序"
  - "将 health_tracker 的工具映射到 MCP 协议"
  - "从远程注册表搜索健康相关的 AIGP 程序"
  - "将 health_tracker 打包为 .aigp 文件"
  - "解包并验证 recipe_finder_v1.0.0.aigp"
  - "为 health_tracker 添加 Dashboard UI 组件"
discovery_keywords: [aigp, creator, aisop, pipeline, evolve, generate, validate, simulate, skill, discover, deprecate, export, import, mcp, registry, adapter, package, pack, sampling, capability, ui, dashboard, form, visualization, tool_dirs, pattern_g, embedded_runtime, code_trust, mcp_server, agent_card, migration, auto_fix, remediation, yellow_persistence, lint_report, automated_verification, endpoint, a2a, license, spdx, store]
dependencies:
  - file: AIGP_Protocol.md
    required: true
    description: "AIGP protocol specification used by ReadTemplate and research modules"
min_protocol_version: "AIGP V1.0.0"
identity:
  program_id: "aigp.dev/aigp_creator"
  publisher: "AIGP Protocol Organization"
  verified_on: "2026-03-03"
benchmark:
  threedimscore: 5.000
  grade: "S"
  simulation_coverage: "A(16)+B(13)+C(10)+D(10)+E(13)+F(6)+G(10)+H(14)+J(2)+K(5)+L(2)+M(12) = 113 scenarios"
  pass_rate: "113/113 (100%) — 0 RED, 0 YELLOW"
---

## 治理声明

AIGP Creator 是 AIGP 协议的参考实现和自举工具。本程序遵循 AIGP V1.0.0 协议，
以 Axiom 0 (Human Sovereignty and Benefit) 为不可变公理，通过三域治理链
(aisop.dev → aigp.dev → soulbot.dev) 确保所有产出对齐人类主权与福祉。

AIGP Creator 自身是一个 AIGP 程序 (自举属性)——它创建 AIGP 程序，同时自身也遵循
所有 AIGP 规则。

## 功能概述

AIGP Creator 通过 14 阶段 Pipeline 管理 AIGP 程序的完整生命周期：

| 意图 | 说明 | Pipeline |
|------|------|----------|
| **Create** | 创建新的 AIGP 程序 | Research → Evolve → Generate → Modify → QualityGate → Validate → Simulate → PostSimulateGate → Observability → Review |
| **Evolve** | 进化现有 AIGP 程序 | 同 Create (带增量差异分析) |
| **Modify** | 修改特定模块 | Research(quality) → Modify → Generate → Validate → [Simulate] → [PostSimulateGate] → Review |
| **Validate** | 验证代码质量 | ThreeDimTest 33+ 项检查 (C1-C7, I1-I13, D1-D10) |
| **Simulate** | 模拟执行路径 | 路径追踪 + 场景覆盖 (Categories A-M) |
| **Compare** | 对比两个版本 | 并排差异展示 |
| **Discover** | 搜索现有程序 | 工作区扫描 + 联邦注册表查询 + 语义匹配 + 关联推荐 |
| **Deprecate** | 弃用/归档程序 | 状态转换 + 迁移指南生成 |
| **Export** | 导出为 SKILL.md | AIGP→SKILL.md 字段映射 + 治理元数据保留 |
| **Import** | 从 SKILL.md 导入 | SKILL.md→AIGP 骨架生成 + 治理默认值填充 |
| **Explain** | 解释 AIGP 概念 | 内联知识回答 |
| **Package** | 打包/解包程序 | advisor package 子图 (pack → .aigp / unpack → verify) |

### 模块架构 (Pattern D+G)

- **main.aisop.json** — 顶级编排器 (27 节点, fractal_exempt)
- **generate.aisop.json** — 生成器 (10 节点)
- **research.aisop.json** — 共享研究模块 (15 节点, fractal_exempt, 3 模式复用)
- **modify.aisop.json** — 修改器 (9 节点)
- **review.aisop.json** — 审查器 (11 节点, +AutoFixEngine)
- **simulate.aisop.json** — 模拟器 (10 节点, +YellowRemediationGuide, +YellowFixProposalGenerator)
- **observability.aisop.json** — 遥测分析 (9 节点, Token/Error/Dimension/RootCause/QRG 分析)
- **advisor.aisop.json** — 高级顾问 (52 节点, fractal_exempt, 8 子图: main 路由 + 7 互斥子图 orchestrate/memory/protocol/skill_export/skill_import/mcp_adapter/package)
- **AIGP_Standard.core.aisop.json** — 核心质量标准 (C1-C7, I1-I7, I12-I13, D1-D7, PL1-PL12, PL19-PL21, MF1-MF9, MF15-MF16 + extension_registry + tool_annotations + json_schema + interop.mcp_tool_mapping + tool_dirs_spec + pattern_thresholds(G) + mcp_tool_mapping/registry/capability_negotiation/sampling_request/aigp_package/ui_output contracts)
- **AIGP_Standard.security.aisop.json** — 安全扩展 (I8-I11, I13 Embedded Code Safety, D8-D10, AT1-AT6 威胁分类, Code Trust Gate with ZIP SLIP extension)
- **AIGP_Standard.ecosystem.aisop.json** — 生态扩展 (MF10-MF14, MF16, K1-K5, PL16-PL17 动态 TTL, PL22 Registry Integration, packaging_specification + tool_dirs_packaging, registry_endpoint_extension, tool_dirs extension, ui_rendering_rules, yellow_persistence_tracking, Categories F-M)
- **AIGP_Standard.performance.aisop.json** — 性能扩展 (PL13-PL15, PL18, PL23 Sampling Protocol, PL24 Auto-Fix Protocol, QRG1-QRG5, E.injection)

## 使用方式

### 入口文件

`main.aisop.json` — AI Agent 加载此文件启动 AIGP Creator。

### 工具需求

| 工具 | 必需 | 用途 |
|------|------|------|
| file_system | 是 | 读写 AISOP 文件 |
| google_search | 否 | 研究阶段搜索最佳实践 |
| web_browser | 否 | 深度网页研究 |

### 前置条件

- 目标目录中包含 AIGP_Standard.core.aisop.json (及扩展文件) 和 AIGP_Protocol.md
- AI Agent 支持 file_system 工具

## 示例交互

**场景 1: 创建新程序**
- 用户: "创建一个个人支出追踪器 AIGP 程序"
- Agent: 执行完整 Pipeline → 生成 expense_tracker_aigp/ 目录含 AIGP.md + main + 模块

**场景 2: 进化现有程序**
- 用户: "将 health_tracker 从 v1.1 进化到 v1.2，添加月度报告功能"
- Agent: 分析现有结构 → 提议 LEVEL_A/B 变更 → 用户确认 → 生成新版本

**场景 3: 验证质量**
- 用户: "验证 recipe_finder 的代码质量"
- Agent: 运行 ThreeDimTest → 输出三维成绩 + 流量分级

## 适用条件

**适用**: 创建、进化、修改、验证、模拟、搜索、弃用 AIGP 程序；SKILL.md 双向转换；MCP 工具映射；联邦注册表发现 (含 MCP/A2A 端点发现)；AIGP 打包/解包 (含 tool_dirs 目录和 Code Trust Gate)；UI 组件声明生成；Pattern G 嵌入式工具目录 (tool_dirs) 验证与自动生成；Pattern E/F→G 迁移指导；自动修复提案生成与应用；YELLOW 持久化追踪与修复指南；自动化质量验证 (lint_report)
**不适用**: 直接执行 AIGP 程序 (那是 SoulBot 执行器的职责)、非 AISOP 格式的项目

---

Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev
