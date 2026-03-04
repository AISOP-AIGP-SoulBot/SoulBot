# AIGP Structural Specification

---

## 目录

**Part I: 协议基础**
1. [协议声明](#1-协议声明)
2. [核心定义：AISOP = 语言，AIGP = 规则](#2-核心定义)
3. [AIGP.md 规则](#3-aigpmd-规则)

**Part II: 结构规范**
4. [节点 = 功能职责](#4-节点--功能职责)
5. [功能节点计数](#5-功能节点计数)
6. [渐进式节点建议](#6-渐进式节点建议)
7. [fractal_exempt 标注](#7-fractal_exempt-标注)
8. [Pattern 选择](#8-pattern-选择)
9. [Pattern A-F 详细定义](#9-pattern-a-f-详细定义)
10. [main.aisop.json 规则](#10-mainaisopjson-规则)
11. [功能模块规则](#11-功能模块规则)
12. [独立功能判断](#12-独立功能判断)
13. [Sub_AIGP 拆分规则](#13-sub_aigp-拆分规则)
14. [Pattern 升级汇聚处理](#14-pattern-升级汇聚处理)
15. [双流规则](#15-双流规则)

**Part III: 安全与运行时**
16. [信任层级](#16-信任层级)
17. [权限边界](#17-权限边界)
18. [完整性验证](#18-完整性验证)
19. [运行时约束](#19-运行时约束)
20. [错误处理协议](#20-错误处理协议)

**Part IV: 工程化能力**
21. [发现协议](#21-发现协议)
22. [依赖解析](#22-依赖解析)
23. [程序生命周期](#23-程序生命周期)
24. [编排模式](#24-编排模式)

**Part V: 质量与兼容**
25. [版本兼容性](#25-版本兼容性)
26. [文档完整性分级](#26-文档完整性分级)

---

## Part I: 协议基础

---

## 1. 协议声明

```
AIGP Structural Specification
Protocol: AIGP V1.0.0
Authority: aigp.dev
Seed: aisop.dev
Axiom 0: Human Sovereignty and Benefit

本文档定义 AIGP 程序的结构规范，包括：
- AIGP.md 项目声明规则
- Pattern A-F 分形模式
- 节点计数与拆分策略
- 安全、运行时、发现、依赖、生命周期、编排协议

所有 AIGP 程序必须遵循本规范。
AISOP 文件格式 (.aisop.json) 作为底层语言不受本文档约束。
```

---

## 2. 核心定义

> AISOP 是编程语言，AIGP 是编程规则。

| 概念 | 类比 | 定义 |
|------|------|------|
| **AISOP** | 编程语言 (Java/Python) | 底层语言 — 定义文件格式 (`.aisop.json`)、语法结构 (`role/content`)、执行模型 |
| **AIGP** | 编程规则 (编码规范/设计模式) | 治理协议 — 定义程序应该怎么写、质量标准、安全守卫、公理约束 |
| **AIGP 程序** | 一个符合规范的项目 | 用 AISOP 语言、按 AIGP 规则编写的完整项目 |
| **AIGP Creator** | 项目脚手架 (`create-react-app`) | 创建 AIGP 程序的工具 — 自身也是一个 AIGP 程序 (自举) |

```
命名规则：
  .aisop.json  →  语言格式标识 (文件用什么语言写的)
  _aigp        →  程序类型标识 (目录遵循什么规则)
  AIGP.md      →  项目声明 (类似 pyproject.toml / pom.xml)
```

### 2.1 AISOP 文件字段职责

> 每个字段有且仅有一个职责。信息只在一处出现。

| 字段 | 职责 | 内容 |
|------|------|------|
| `id` | 身份标识 | 程序和模块的唯一标识符 |
| `name` | 名称 | 产品名称 + 版本号 |
| `version` | 版本 | 语义版本号 |
| `summary` | 能力概述 | 一句话说明"我能做什么" |
| `description` | 详细描述 | 架构、历史、模式、实现细节 |
| `system_prompt` | **行为准则** | 定义 agent 应该怎么做 (唯一的行为定义层) |
| `instruction` | **执行指令** | 固定为 `RUN aisop.main` (不可变常量) |
| `aisop.main` | 执行图 | 主 Mermaid 流程图 — 所有执行从此开始 |
| `functions` | 执行逻辑 | 每个节点的具体步骤和约束 |

### 2.2 instruction 不可变常量

```
规则：每个 AISOP 文件的 instruction 字段必须精确为：RUN aisop.main
```

**原理**：
- `RUN` 是机器执行指令，不是自然语言建议。类比 Dockerfile `RUN`、SQL `SELECT`。
- `aisop.main` 是 JSON 结构路径，指向 `content.aisop.main` 执行图。
- 程序身份由 `id` 字段提供，不需要在 instruction 中重复。
- 能力描述由 `summary`/`description` 提供，不需要在 instruction 中重复。

```
C 语言类比：
  int main() { ... }     ← 入口永远是 main，所有程序统一
  RUN aisop.main          ← 入口永远是 aisop.main，所有 AISOP 文件统一
```

**sub_mermaid**：即使 aisop 对象包含多个图（如 `main`, `orchestrate`, `memory`），入口仍然是 `aisop.main`。main 图内部通过参数路由到子图。

### 2.3 system_prompt 行为层规则

```
规则：system_prompt 是行为层 — 定义 agent 应该怎么做，不描述它是什么或怎么构建的。
```

**必须包含**：
1. **角色定位** — agent 的行为角色（不是产品名）
2. **领域行为准则** — 该领域特有的行为约束
3. `Mirror User's exact language and script variant.` — 多语言要求
4. `Align: Human Sovereignty and Benefit.` — Axiom 0 封印

**禁止包含**：
- 产品名或版本号 → 已在 `name` + `version` 字段
- 架构或模式细节 → 已在 `description` 字段
- 模块文件名或委托逻辑 → 已在 `functions` 字段
- 能力列表 → 已在 `summary` 字段

```
格式模板：
  "{行为角色}. {领域准则}. Mirror User's exact language and script variant.\nAlign: Human Sovereignty and Benefit."

正例：
  "Personal expense tracking assistant. Prioritize numerical precision.
   Protect user financial privacy. Mirror User's exact language and script variant.
   Align: Human Sovereignty and Benefit."

反例：
  "Expense Tracker v1.0.0. Pattern B router: delegate data operations
   to record.aisop.json. Mirror User's exact language and script variant.
   Align: Human Sovereignty and Benefit."
   ↑ 包含产品名+版本(name)、架构(description)、文件名(functions)
```

---

## 3. AIGP.md 规则

每个 `{name}_aigp/` 目录**必须**包含 AIGP.md 文件。AIGP.md 是项目的治理契约和发现入口。

### 3.1 必需字段 (YAML frontmatter)

**治理字段 (6 个)**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `protocol` | string | AIGP 版本号，如 `"AIGP V1.0.0"` |
| `authority` | string | 治理权威域，固定为 `aigp.dev` |
| `seed` | string | 格式种子域，固定为 `aisop.dev` |
| `executor` | string | 执行平台域，固定为 `soulbot.dev` |
| `axiom_0` | string | 核心公理，固定为 `Human_Sovereignty_and_Benefit` |
| `governance_mode` | string | `NORMAL` 或 `DEV` |

**项目字段 (6 个)**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 项目名称 (snake_case) |
| `version` | string | 当前版本 (semver, 与 main.aisop.json 同步) |
| `pattern` | string | 结构模式 `A\|B\|C\|D\|E\|F` |
| `summary` | string | 1-2 句功能概述 |
| `tools` | list/object | 工具声明 (见 §3.3) |
| `modules` | list | 模块清单 (见 §3.4) |

### 3.2 可选字段 (YAML frontmatter)

**基础可选字段**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `governance_hash` | string | 治理哈希 (见 §18) |
| `quality` | object | `{weighted_score, grade, last_pipeline}` |
| `description` | string | Agent Skills 兼容字段 — 技能描述 |
| `tags` | list | 分类标签 |
| `author` | string | 作者信息 |
| `license` | string | 许可证 |
| `tool_dirs` | list | Pattern G 工具目录声明 (见 §9 Pattern G) |
| `capabilities` | object | 运行时能力声明 `{offered, required}` |

**安全与运行时可选字段** (Part III):

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `trust_level` | number (1-4) | 3 | 信任层级 (见 §16) |
| `permissions` | object | null | 权限边界 (见 §17) |
| `runtime` | object | null | 运行时约束 (见 §19) |

**工程化可选字段** (Part IV):

| 字段 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `status` | string | "draft" | 生命周期状态 (见 §23) |
| `deprecated_date` | string | null | 弃用日期 |
| `successor` | string | null | 替代程序名 |
| `intent_examples` | list | [] | 语义路由锚点 (见 §21) |
| `discovery_keywords` | list | [] | 关键词索引 |
| `dependencies` | list | [] | 跨项目依赖 (见 §22) |
| `min_protocol_version` | string | null | 最低协议版本 (见 §25) |
| `benchmark` | object | null | 质量基准声明 |
| `identity` | object | null | 程序身份与来源 (见 I11) — `{ program_id, publisher, verified_on }` |

### 3.3 tools 字段规范

**简洁格式** (向后兼容):

```yaml
tools: [file_system, shell]
```

**结构化格式** (推荐):

```yaml
tools:
  - name: file_system
    required: true
    min_version: "1.0"
  - name: shell
    required: false
    fallback: "degrade"       # 不可用时降级运行
```

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `name` | string | (必需) | 工具名称 |
| `required` | boolean | true | 是否为必需工具 |
| `min_version` | string | null | 最低版本要求 |
| `fallback` | string | null | 不可用时的降级策略: `"degrade"` / `"skip"` / `"error"` |

### 3.4 modules 字段规范

```yaml
modules:
  - id: health_tracker.record
    file: record.aisop.json
    nodes: 7
    critical: true              # 是否为关键模块 (默认 true)
    idempotent: true            # 是否幂等 (默认 false)
    side_effects: [file_write]  # 副作用声明 (默认 [])
```

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `id` | string | (必需) | 模块唯一标识 `{project}.{module}` |
| `file` | string | (必需) | 文件名 |
| `nodes` | number | (必需) | 功能节点数 |
| `critical` | boolean | true | 失败时是否触发 FATAL (见 §20) |
| `idempotent` | boolean | false | 重复执行是否安全 |
| `side_effects` | list | [] | 副作用列表: `file_write`, `file_delete`, `api_call`, `shell_exec` |

空 `side_effects` 列表 = 纯函数 (无副作用)。

### 3.5 Markdown Body

**必需节**:

| 节 | 内容 |
|---|------|
| **治理声明** | 声明遵循 AIGP 协议 + Axiom 0 对齐 |
| **功能概述** | 按模块/意图列出核心功能 |
| **使用方式** | 入口文件、工具需求、前置条件 |

**推荐节** (status=active 时):

| 节 | 内容 |
|---|------|
| **示例交互** | 1-3 个典型使用场景的输入/输出示例 |
| **适用条件** | 明确程序适用和不适用的场景 |

**可选节**:

| 节 | 内容 |
|---|------|
| **数据存储** | 数据文件路径和格式 |
| **配置说明** | 可配置参数和默认值 |
| **质量状态** | ThreeDimTest 分数、Pipeline 历史 |
| **版本历史** | 主要版本变更摘要 (结构化格式见 §25) |
| **错误处理** | 常见错误及用户处理方式 |

**文件末尾**: 必须以 AIGP 闭环印章结尾。

| governance_mode | 印章格式 |
|----------------|---------|
| NORMAL | `Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev` |
| DEV | `[L0_BOOT: Success] [L1_REPORT: Success] [endNode_Align: Human Sovereignty and Benefit]. Version: AIGP V1.0.0. www.aigp.dev` |

### 3.6 Creator 自动维护规则

| 触发事件 | Creator 行为 |
|---------|-------------|
| **Create** | 自动生成 AIGP.md，所有必需字段填充，status 设为 draft |
| **Evolve** | 更新 version、modules、quality、summary (如有变化) |
| **Modify** | 更新 version、quality |
| **Validate** | 检查 AIGP.md 存在性和字段完整性 (D8 检查) |
| **QualityGate 通过** | 若 status=draft，自动升级为 active |
| **version_history snapshot** | 在 `{version}/` 目录中保存 AIGP.md 快照 |

---

## Part II: 结构规范

---

## 4. 节点 = 功能职责

> 节点匹配功能，main 路由分发，模块自包含，共享逻辑单独提取，不无限拆分。

每个 Mermaid 节点代表模块的一个功能职责，类似 Python 文件中的一个函数。节点数由功能复杂度自然决定，不由外部硬限强加。

```
Python 类比：
  record.py 有 4 个函数 → record.aisop.json 有 4 个功能节点
  query.py 有 6 个函数  → query.aisop.json 有 6 个功能节点
  节点数跟随功能，不跟随配额
```

---

## 5. 功能节点计数

```
功能节点 = Mermaid 总节点 - Start - endNode
```

Start 和 endNode 是每个 AISOP 文件的固定结构框架 (类似 Python 的 `if __name__`)，不反映功能复杂度，不计入节点数。

示例：

```
graph TD
    Start --> Parse --> Validate{OK?} --> Save --> Alert --> endNode
                                       --> AskFix --> Parse
```

总节点 7，功能节点 5 (Parse, Validate, Save, Alert, AskFix)。

---

## 6. 渐进式节点建议

适用于所有 `.aisop.json` 文件 (包括 main):

```
功能节点 3-12  → 正常，无提示
功能节点 13-15 → ADVISORY — 建议检查拆分机会，给出具体建议
功能节点 16+   → RECOMMENDED — 强烈建议拆分，给出拆分方案
```

- 两级都是 WARNING，不是 FAIL
- 功能内聚的大模块可标注 `fractal_exempt` 跳过建议
- 最小要求: >=3 功能节点 + (>=1 tool call OR >=3 steps)

---

## 7. fractal_exempt 标注

当模块功能节点超过 12 但流程高度内聚时，可在 `system.content` 中标注：

```json
{
    "fractal_exempt": "Pipeline 的 13 个阶段是连续管道，拆分导致上下文碎片化"
}
```

标注后 Creator 跳过该文件的渐进式拆分建议。等价于 Python 的 `# noqa`。

---

## 8. Pattern 选择

```
独立功能数 → Pattern：
  1 个功能            → A: Script (单文件)
  2+ 个功能           → B: Package (多文件)
  2+ 功能 + 复杂共享   → C: Package + Shared
  子模块也需要再拆     → D: Nested Package
  带记忆层            → E: Package + Memory
  多 AIGP 程序生态系统  → F: Ecosystem
  带嵌入式工具目录      → G: Embedded Runtime
```

---

## 9. Pattern A-G 详细定义

### Pattern A: Script

```
{name}_aigp/
├── AIGP.md                     # 必需：治理契约
└── main.aisop.json             # 全部逻辑
```

适用: todo list, timer, calculator 等单一功能。无硬限。渐进式建议适用。

### Pattern B: Package

```
{name}_aigp/
├── AIGP.md                     # 必需：治理契约
├── main.aisop.json             # 路由器：意图识别 → 分发
├── {func1}.aisop.json          # 功能模块 (完全自包含)
├── {func2}.aisop.json
└── {func3}.aisop.json
```

示例：
```
expense_tracker_aigp/
├── AIGP.md                     # 治理契约
├── main.aisop.json             # 意图：record / query / budget / report
├── record.aisop.json           # 验证 → 写入 → 确认
├── query.aisop.json            # 解析 → 读取 → 过滤 → 格式化
├── budget.aisop.json           # 设置 → 检查 → 提醒
└── report.aisop.json           # 聚合 → 分析 → 展示
```

### Pattern C: Package + Shared

```
{name}_aigp/
├── AIGP.md                     # 必需：治理契约
├── main.aisop.json             # 路由器
├── {func1}.aisop.json
├── {func2}.aisop.json
└── shared.aisop.json           # 被 2+ 模块调用的复杂共享逻辑
```

shared 规则: 只在 2+ 模块复用**复杂操作**时创建。简单共享 (格式/风格) 写在各模块 system_prompt 里。

### Pattern D: Nested Package

```
{name}_aigp/
├── AIGP.md                     # 必需：治理契约
├── main.aisop.json             # 顶级路由器
├── {simple_func}.aisop.json    # 简单模块
└── {complex}_sub_aigp/         # 复杂模块 (有子结构)
    ├── AIGP.md                 # 子包治理契约 (如果独立发布)
    ├── main.aisop.json         # 子路由器
    ├── {sub1}.aisop.json
    └── {sub2}.aisop.json
```

嵌套规则: 最多 2 层，只在子模块本身有 2+ 个子功能时才嵌套。

#### Pattern D 实例: AIGP Creator

```
aigp_creator_aigp/
├── AIGP.md                     # 治理契约 (AIGP V1.0.0)
├── main.aisop.json             # 顶级编排器 (21 功能节点, fractal_exempt)
│   └── 意图: Create, Evolve, Modify, Validate, Simulate, Compare, Explain, General
│   └── Pipeline: Research→Evolve→Generate→Modify→QualityGate→Validate→Simulate→Observability→Review
├── generate.aisop.json         # 生成器 (10 功能节点)
├── research.aisop.json         # 共享研究模块 (14 功能节点, fractal_exempt, 3 模式复用)
├── review.aisop.json           # 审查器 (9 功能节点)
├── simulate.aisop.json         # 模拟器 (7 功能节点)
├── modify.aisop.json           # 修改器 (9 功能节点)
├── observability.aisop.json    # 遥测分析 (5 功能节点)
├── advisor.aisop.json          # 高级顾问 (24 功能节点, fractal_exempt, 4 子图互斥)
├── AIGP_Standard.core.aisop.json         # 核心质量标准 (C1-C7, I1-I7, D1-D7, PL1-PL12, PL19-PL21, MF1-MF9)
├── AIGP_Standard.security.aisop.json     # 安全扩展 (I8-I11, D8-D10, AT1-AT6)
├── AIGP_Standard.ecosystem.aisop.json    # 生态扩展 (MF10-MF14, K1-K4, PL16-PL17)
├── AIGP_Standard.performance.aisop.json  # 性能扩展 (PL13-PL15, PL18, QRG1-QRG4, E.injection)
└── AIGP_Protocol.md            # 结构规范 (Protocol-level)
```

特点:
- 8+4 个模块 (8 个可执行模块 + 4 个 STANDARD 扩展文件)，共约 100 个功能节点
- main 是纯编排器 (连续委托，无业务逻辑)，标注 fractal_exempt
- research 通过 ModeGate 复用 3 种模式 (structure/quality/compliance)，标注 fractal_exempt
- advisor 使用 sub_mermaid 子图 (4 个互斥子图)，实际单路径最大 12 节点
- 通信拓扑为星型 (main 编排)，模块间无直接通信

### Pattern E: Package + Memory

```
{name}_aigp/
├── AIGP.md                     # 必需：治理契约
├── main.aisop.json             # 路由器
├── {func1}.aisop.json
├── {func2}.aisop.json
└── memory/                     # 记忆层
    ├── schema.json             # 记忆字段定义 (episodic/semantic/working)
    ├── decay_config.json       # 衰减策略参数
    └── context_manager.json    # 上下文预算和加载策略
```

适用: 需要跨会话记忆、个性化、RAG 检索的 AIGP 程序。使用 advisor.aisop.json (advisor_type='memory') 生成 memory/ 目录内容。

### Pattern F: Ecosystem

```
{ecosystem_name}/
├── AIGP.md                     # 必需：生态系统级治理契约
├── blueprint.json              # 生态系统蓝图 (组件、接口、拓扑)
├── {component1}_aigp/          # 独立组件 (Pattern A-E)
│   ├── AIGP.md                 # 必需：组件级治理契约
│   └── main.aisop.json
├── {component2}_aigp/
│   ├── AIGP.md
│   └── ...
└── shared/                     # 跨组件共享的数据契约
    └── data_contracts.json
```

适用: 3+ 个 AIGP 程序组件协作的复杂系统。使用 advisor.aisop.json (advisor_type='orchestrate') 设计生态系统蓝图。

#### blueprint.json 组件接口声明

```json
{
    "ecosystem": "soulbot_ecosystem",
    "protocol": "AIGP V1.0.0",
    "components": ["component_a_aigp", "component_b_aigp"],
    "interfaces": [
        {
            "name": "health_data_query",
            "provider": "component_a_aigp",
            "consumer": "component_b_aigp",
            "contract": "shared/data_contracts.json#health_query",
            "mode": "sequential"
        }
    ]
}
```

### Pattern G: Embedded Runtime

```
{name}_aigp/
├── AIGP.md                     # 必需：治理契约 (含 tool_dirs 字段)
├── main.aisop.json             # 路由器
├── {func1}.aisop.json
├── {func2}.aisop.json
├── python-tools/               # Python 工具实现
│   ├── README.md               # 必需：工具说明、接口、安全约束
│   ├── requirements.txt        # 冻结版本 (== 固定，禁止 >=/*~=)
│   ├── *.py                    # 工具代码
│   └── mcp_adapter.py          # Creator 自动生成的 MCP stdio 端点
├── ts-tools/                   # TypeScript 工具实现
│   ├── README.md
│   ├── package.json            # 精确版本 (禁止 ^~)
│   ├── package-lock.json       # 锁定传递依赖
│   └── *.ts
├── go-tools/                   # Go 工具实现
│   ├── README.md
│   ├── go.mod + go.sum         # 依赖锁定
│   └── bin/tool                # 预编译二进制 (推荐)
├── rust-tools/                 # Rust 工具实现
│   ├── README.md
│   ├── Cargo.toml + Cargo.lock
│   └── target/release/tool     # 必须预编译
├── shell-tools/                # Shell 脚本 (仅 T4 + 人工审计)
│   ├── README.md
│   └── tool.sh / tool.ps1
├── mcp-tools/                  # MCP Server 定义层
│   └── mcp_server.json         # MCP Server 清单 + 运行时声明
├── a2a-tools/                  # A2A Agent Card 层 (可选)
│   └── agent_card.json
├── n8n-tools/                  # n8n 工作流自动化层 (可选)
│   ├── workflow.json
│   └── config.json
├── other-tools/                # 开放扩展层 (可选)
│   └── README.md               # 必需：调用方式、接口、安全约束
└── memory/                     # Pattern E 记忆层 (可选)
    └── ...
```

继承: Pattern E 或 F 的所有规则

额外要求:
- AIGP.md 必须包含 `tool_dirs` 字段声明工具目录
- `mcp-tools/mcp_server.json` 必须存在
- I13 Embedded Code Safety 规则适用 (6 项子检查)
- MF16 Tool Directory Consistency 规则适用
- 最低信任层级: T3
- 需要 Code Trust Gate 验证

特性:
- CLI 执行器有原生 shell 工具，可直接执行捆绑代码
- 无需中间层或预装工具
- 自包含、可独立部署

#### tool_dirs 支持的工具目录类型

| 类型 | 运行时 | 依赖锁定 | 适用场景 |
|------|--------|---------|---------|
| `python-tools/` | Python 3.9-3.13 | `requirements.txt` (== 固定) | 数据处理、AI/ML、文件操作 |
| `ts-tools/` | Node.js/Deno/Bun | `package-lock.json` | Web API、JSON 处理、类型安全 |
| `go-tools/` | Go 或预编译二进制 | `go.sum` | 高并发、CLI、低延迟 |
| `rust-tools/` | 预编译二进制 | `Cargo.lock` | 高性能、内存安全、WASM |
| `shell-tools/` | bash / pwsh | 无 | 系统脚本 (仅 T4) |
| `mcp-tools/` | stdio transport | `mcp_server.json` | MCP 生态工具 |
| `a2a-tools/` | A2A 协议 | `agent_card.json` | Agent 间协作 |
| `n8n-tools/` | n8n 实例 | `workflow.json` | 多服务集成 |
| `other-tools/` | 自定义 | README.md | 开放扩展 |

#### mcp_server.json 格式

```json
{
  "schema_version": "mcp-1.0",
  "server_id": "file:///./mcp-tools",
  "transport": "stdio",
  "runtime": "python3.11",
  "entry_point": "python-tools/mcp_adapter.py",
  "exposed_tools": [
    {
      "name": "process_data",
      "description": "Process input data and return structured result",
      "inputSchema": {
        "type": "object",
        "required": ["data"],
        "properties": {
          "data": { "type": "string" }
        }
      }
    }
  ],
  "file_hashes": {
    "python-tools/data_processor.py": "sha256_hash_value",
    "python-tools/mcp_adapter.py": "sha256_hash_value"
  },
  "governance": {
    "aigp_protocol": "AIGP V1.0.0",
    "trust_level": 3,
    "governance_hash": "filled by Creator ReviewStep"
  }
}
```

#### Code Trust Gate

Pattern G 程序加载时必须通过 Code Trust Gate 安全验证：

```
加载 Pattern G 程序
    ↓
Code Trust Gate:
  1. governance_hash 验证 (覆盖所有文件含 tool_dirs 源码)
  2. 静态分析: import/require 声明 vs permissions.network
  3. 文件哈希验证 (对照 mcp_server.json file_hashes)
  4. 信任层级检查 (Pattern G 最低 T3)
  5. 依赖锁定文件验证
    ↓
  [T3 模式] 需要人工审核确认
  [T4 模式] 自动通过
    ↓
启动 MCP Server (stdio)
    ↓
AIGP 程序执行 (通过 MCP 调用工具)
```

#### I13 Embedded Code Safety (6 项子检查)

适用: Pattern G 程序 (含 tool_dirs)。Pattern A-F 标记 N/A。

| 子检查 | 说明 |
|--------|------|
| **(a) CODE INTEGRITY** | tool_dirs/ 所有源码/二进制文件的 SHA-256 哈希必须记录在 mcp_server.json file_hashes 中 |
| **(b) NETWORK DECLARATION** | 检测网络访问 API (requests/fetch/net/http 等)，若存在则 permissions.network.allowed 必须为 true |
| **(c) FILE SYSTEM SCOPE** | 文件写入操作不得超出 permissions.file_system.scope |
| **(d) DEPENDENCY VERSION PINNING** | Python: == 固定; TS/JS: 禁止 ^~; Go: go.sum 必须存在; Rust: Cargo.lock 必须存在 |
| **(e) MCP PROXY REQUIRED** | 所有代码工具必须通过 mcp-tools/ 层暴露，禁止执行器直接子进程执行源文件 |
| **(f) SHELL AUDIT** | shell-tools/ 存在时 trust_level 必须 ≥ T4 |

#### MF16 Tool Directory Consistency

适用: Pattern G 程序。

| 检查 | 说明 |
|------|------|
| **(a)** | mcp_server.json 存在于声明路径 |
| **(b)** | mcp_server.json exposed_tools 条目在 AIGP.md tools[] 中有对应声明 |
| **(c)** | AIGP.md tools[] 引用 mcp_server 的条目在 exposed_tools 中存在 |
| **(d)** | a2a agent_card.json 的 governance_hash 与 AIGP.md 一致 |

#### 向后兼容

- tool_dirs 字段完全可选
- 无 tool_dirs 的程序 (Pattern A-F) 不受影响
- I13、MF16 对非 Pattern G 程序标记 N/A
- governance_hash 算法对非 Pattern G 程序不变

---

## 10. main.aisop.json 规则

main 遵循与功能模块相同的渐进式节点建议。区别是**质的约束** (不是量的约束):

**Pattern A**: main 是唯一文件，包含全部逻辑，无特殊约束。

**Pattern B+**: main 是路由器:
- 只包含路由逻辑 + 轻量内联处理
- 不含业务逻辑 (数据处理、文件 I/O、复杂验证)
- tools = 所有子模块 tools 的并集
- 路由节点数量由意图数量自然决定
- 调用方式: 意图识别 → 读取对应子文件 → AI Agent 执行

```
判断节点是否属于 main：
  ≤2 steps + 无工具调用 → OK (轻量内联，如 Explain、General)
  >2 steps 或 有工具调用 → 应放入 sub_aisop
```

---

## 11. 功能模块规则

- 完全自包含 (独立 system_prompt / tools / parameters / functions)
- 不依赖其他模块的内部实现
- 模块内部深度由功能决定，渐进式建议适用
- 最小要求: >=3 功能节点 + (>=1 tool call OR >=3 steps)

---

## 12. 独立功能判断

能用一句话描述 + 不共享专用工具/状态 + 能单独测试 → 独立成文件

- Level 1 工具 (file_system, shell) 为通用基础设施，不计入"共享工具"
- 通过 file_system 读写同一数据文件的模块仍可独立 (各自负责不同操作)
- "共享状态"指运行时内存状态或专用连接，非持久化数据文件

---

## 13. Sub_AIGP 拆分规则

当 Creator 建议拆分时，按以下优先级分析拆分边界:

```
优先级 1 — 工具边界:
  节点组 A 用 google_search + web_browser
  节点组 B 只用 file_system
  → 天然分界线，拆分为独立 sub_aigp

优先级 2 — 数据流阶段:
  线性管道中的明确阶段界限 (research → generate → test)
  → 每个阶段为 sub_aigp 候选

优先级 3 — 功能独立性:
  满足独立功能判断三条件
  → 拆分为 sub_aigp
```

**禁止拆分的模式**:
- 汇聚节点组 (多→一的扇入模式) → 保持同一 sub_aigp
- 错误恢复循环 (Error → Retry → 原节点) → 保持同一 sub_aigp
- 共享同一 tool + state 的紧密节点 → 保持同一 sub_aigp

---

## 14. Pattern 升级汇聚处理

当 Pattern A→B 升级拆分文件时，原有的汇聚/展示节点 (如 Respond、Display、Output) 需要特殊处理:

```
汇聚节点判断：
  该节点有 >2 steps 或 有工具调用？
    → 不符合 main 内联标准，必须分入子模块

  多个子模块都需要该节点的逻辑？
    → 各子模块创建自己的专用版本 (按各自输出格式定制)
    → 不创建 shared.aisop.json (除非逻辑复杂且完全相同)

  只有一个子模块使用？
    → 直接归入该子模块
```

示例:
```
Pattern A (拆分前):
  SearchRecipes → ReadRecipe → NutritionAnalysis → Respond → endNode
  SaveCollection → Respond → endNode
  CompareView → Respond → endNode
  (Respond 是全路径汇聚点，4 steps + 工具引用)

Pattern B (拆分后):
  search.aisop.json:  ...→ SearchRespond → endNode  (搜索结果展示)
  collection.aisop.json: ...→ CollectionRespond → endNode (收藏操作展示)
  (各子模块有专用 Respond，内容按模块输出定制)
```

---

## 15. 双流规则

复杂项目 (Pattern D+) 可选择提供人类版和 AI 版双文件:

```
{name}_aigp/
├── AIGP.md
├── main.human.aisop.json      # 人类可读版 (完整键名)
├── main.ai.aisop.json         # AI 优化版 (压缩键名)
└── ...
```

规则:
- 两个版本的逻辑语义必须完全一致
- `.human` 版使用完整键名，便于人类审查
- `.ai` 版使用缩写键名，减少 token 消耗
- AI Agent 优先加载 `.ai` 版，调试时加载 `.human` 版
- 非双流项目仍使用单一 `.aisop.json` (不加 `.human` 或 `.ai` 前缀)

---

## Part III: 安全与运行时

---

## 16. 信任层级

AIGP 程序通过 `trust_level` 声明其权限需求和执行模式。

### 16.1 四层信任定义

| 层级 | 名称 | 含义 | 权限范围 |
|------|------|------|---------|
| **T1** | Metadata-Only | 仅读取 AIGP.md frontmatter | 不加载 .aisop.json 内容 |
| **T2** | Instruction-Read | 可读取 .aisop.json 指令内容 | 不可执行任何工具调用 |
| **T3** | Supervised | 需要人类审批或沙箱环境执行 | 每个工具调用需确认 |
| **T4** | Autonomous | 在声明的权限边界内自主执行 | 遵循 permissions 字段约束 |

### 16.2 信任层级与功能的关系

| trust_level | 可执行的操作 | 典型用途 |
|-------------|-------------|---------|
| T1 | 读取 summary、name、description | 程序目录索引、搜索结果展示 |
| T2 | 读取完整流程图、函数定义 | 代码审查、文档生成、教学 |
| T3 | 在人类监督下执行所有工具调用 | 首次运行的新程序、高风险操作 |
| T4 | 自主执行所有声明的工具调用 | 已验证的生产程序 |

### 16.3 声明方式

```yaml
# AIGP.md frontmatter
trust_level: 3    # 默认值，可选字段
```

未声明 trust_level 时，执行器应按 T3 (Supervised) 处理。

---

## 17. 权限边界

T4 (Autonomous) 程序**必须**通过 `permissions` 声明权限边界。T1-T3 程序此字段可选。

### 17.1 声明格式

```yaml
# AIGP.md frontmatter
permissions:
  file_system:
    scope: "./data/"            # 读写范围限定 (相对于项目根目录)
    operations: ["read", "write"]
  shell:
    allowed: false              # 禁止 shell 调用
  network:
    allowed: false              # 禁止网络调用
```

### 17.2 权限类型

| 权限 | 属性 | 说明 |
|------|------|------|
| **file_system** | `scope` | 允许访问的目录 (glob 语法) |
| | `operations` | 允许的操作: `read`, `write`, `delete` |
| **shell** | `allowed` | 是否允许 shell 执行 |
| | `allowlist` | 允许的命令列表 (仅 allowed=true 时) |
| **network** | `allowed` | 是否允许网络请求 |
| | `endpoints` | 允许访问的 URL 模式列表 |

### 17.3 执行器职责

执行器 (SoulBot) 在运行 T4 程序时**必须**:
1. 读取 `permissions` 声明
2. 在工具调用前验证是否在声明范围内
3. 超范围调用 → 拒绝执行 + 报告安全违规

---

## 18. 完整性验证

### 18.1 governance_hash 算法

```
governance_hash = SHA-256(
    所有 .aisop.json 文件内容 (按文件名字母序拼接, CRLF→LF 规范化)
)

Pattern G 扩展:
  .aisop.json 文件集不变。tool_dirs/ 文件哈希记录在 mcp_server.json
  的 file_hashes 字段中，通过 governance_hash 间接覆盖。
  无 tool_dirs 的程序 governance_hash 算法不变 (向后兼容)。
```

输出格式: `"sha256:{hash_value}"` (64 字符十六进制)

### 18.2 必需性规则

| trust_level | governance_hash |
|-------------|----------------|
| T1-T2 | 可选 |
| T3 | 推荐 |
| T4 | 推荐 |
| 已发布到 Registry | 必需 |

### 18.3 验证流程

Creator ValidateStep 执行验证:
1. 计算当前文件的 SHA-256 哈希
2. 与 AIGP.md 中声明的 governance_hash 对比
3. 不匹配 → WARNING: "Integrity check failed — files may have been modified outside Creator pipeline"

---

## 19. 运行时约束

### 19.1 声明格式

```yaml
# AIGP.md frontmatter
runtime:
  timeout_seconds: 300          # 单次执行超时 (默认: 执行器决定)
  max_retries: 3                # 最大重试次数 (默认: 3)
  token_budget: 50000           # Token 预算上限 (默认: 无限制)
  idempotent: false             # 整体是否幂等 (默认: false)
  side_effects:                 # 整体副作用声明
    - file_write
    - api_call
```

### 19.2 字段说明

| 字段 | 含义 | 用途 |
|------|------|------|
| `timeout_seconds` | 单次完整执行的超时上限 | 防止无限执行 |
| `max_retries` | RECOVERABLE 错误的最大重试次数 | 控制重试开销 |
| `token_budget` | 单次执行的 token 消耗上限 | 成本控制 |
| `idempotent` | 重复执行是否产生相同结果 | 编排器判断是否可安全重试 |
| `side_effects` | 程序整体的副作用列表 | 编排器判断执行风险 |

### 19.3 与 modules 的关系

- 程序级 `runtime.side_effects` = 所有模块 `side_effects` 的并集
- 程序级 `runtime.idempotent` = 所有 critical 模块均 `idempotent` 时为 true
- 模块级属性 (§3.4) 提供细粒度控制，程序级属性提供快速概览

---

## 20. 错误处理协议

### 20.1 错误分类

| 类别 | 含义 | 策略 |
|------|------|------|
| **RECOVERABLE** | 暂时性失败 (网络超时、文件锁、API 限流) | 按 `max_retries` 重试，指数退避 |
| **DEGRADABLE** | 非关键模块失败 (`critical: false`) | 跳过失败模块，降级执行，标记 WARNING |
| **FATAL** | 关键模块失败 (`critical: true`) 或安全违规 | 立即停止，报告错误，不产出结果 |

### 20.2 重试策略

```
重试间隔: 1s, 2s, 4s, 8s, ... (指数退避，base=2)
最大重试: runtime.max_retries (默认 3)
最大间隔: min(2^retry_count, 30) 秒
每次重试必须记录: 错误原因 + 重试次数 + 时间戳
```

### 20.3 降级行为

当模块执行失败且该模块 `critical: false` 时:
1. 跳过该模块的输出
2. 在最终结果中标记: `"DEGRADED: {module_name} skipped due to {error}"`
3. 不影响整体执行的成功/失败判定
4. 最终结果包含降级模块列表

### 20.4 终止条件

每个 AIGP 程序的执行按以下条件终止:

| 终止类型 | 条件 | 结果 |
|---------|------|------|
| **成功终止** | 所有 critical 模块执行完毕 + 输出通过验证 | 返回完整结果 |
| **超时终止** | `runtime.timeout_seconds` 到达 | 返回已完成部分 + 超时标记 |
| **错误终止** | FATAL 级错误触发 | 返回错误报告，不返回部分结果 |
| **降级终止** | 成功终止但有模块被跳过 | 返回降级结果 + 降级报告 |

---

## Part IV: 工程化能力

---

## 21. 发现协议

### 21.1 发现层次

| 层次 | 方式 | 机制 | Token 开销 |
|------|------|------|-----------|
| **L1 被动发现** | 文件系统扫描 | 扫描器遍历目录，识别包含 AIGP.md 的 `_aigp/` 目录 | ~50-80/程序 |
| **L2 语义发现** | 意图匹配 | 将用户查询与 `intent_examples` 语义相似度匹配 | 0 (预计算) |
| **L3 注册发现** | 注册中心查询 | 通过 AIGP Registry (aigp.dev) 查询已发布程序 | ~100/查询 |

### 21.2 L1 扫描协议

扫描器应按以下顺序搜索 AIGP 程序:

1. 当前工作目录下的 `*_aigp/` 子目录
2. 配置的 AIGP 库路径 (如 `~/.aigp/library/`)
3. 项目 `aigp.config` 中声明的依赖路径

对每个发现的 AIGP 程序:
1. 读取 AIGP.md YAML frontmatter (L1 元数据, ~50-80 tokens)
2. 注册到可用程序清单 (name + summary + status)
3. 仅在匹配时加载完整内容 (L2+L3)

### 21.3 L2 语义匹配

```yaml
# AIGP.md frontmatter
intent_examples:
  - "记录今天的体重"
  - "查看本周的血压趋势"
  - "生成月度健康报告"
discovery_keywords:
  - health
  - tracking
  - wellness
```

匹配流程:
1. 将 `intent_examples` 转换为嵌入向量 (embedding)
2. 新查询到来时，计算与已有向量的余弦相似度
3. 相似度超过阈值 → 候选匹配
4. 结合 `summary` + `discovery_keywords` 排序

### 21.4 调用模式

| 模式 | 触发方式 | 匹配机制 |
|------|---------|---------|
| **显式调用** | 用户指定程序名 (如 "使用 health_tracker") | 精确匹配 `name` 字段 |
| **隐式调用** | LLM 根据用户意图自动选择 | 语义匹配 `summary` + `intent_examples` |

---

## 22. 依赖解析

### 22.1 依赖声明

```yaml
# AIGP.md frontmatter
dependencies:
  - name: shared_utils_aigp
    version: "^1.0.0"           # semver 范围约束
    required: true
  - name: analytics_aigp
    version: ">=2.0.0"
    required: false              # 可选依赖
    fallback: "skip"             # 不可用时: "skip" / "degrade" / "error"
```

### 22.2 版本约束语法

| 语法 | 含义 | 匹配示例 |
|------|------|---------|
| `"1.2.3"` | 精确版本 | 仅 1.2.3 |
| `"^1.2.0"` | 兼容更新 | >=1.2.0 且 <2.0.0 |
| `"~1.2.0"` | 补丁更新 | >=1.2.0 且 <1.3.0 |
| `">=1.0.0"` | 最低版本 | >=1.0.0 |

### 22.3 解析策略

1. **扁平化解析** (默认) — 所有依赖平铺在同一层级，版本冲突时选择满足所有约束的最高兼容版本
2. **隔离解析** — Pattern F Ecosystem 中，各组件独立解析依赖，通过 `data_contracts` 交互

### 22.4 冲突解析

当多个 AIGP 程序依赖同一程序的不同版本时:
- 自动选择满足所有约束的最高版本
- 如无法满足所有约束 → 报告冲突，要求人类决策
- 冲突报告包含: 冲突依赖名、各约束来源、可选解决方案

---

## 23. 程序生命周期

### 23.1 生命周期状态

| 状态 | 含义 | AIGP.md 字段 | Creator 行为 |
|------|------|-------------|-------------|
| **draft** | 开发中，不稳定 | `status: draft` | Create 阶段自动设置 |
| **active** | 生产可用 | `status: active` | 首次通过 QualityGate 后自动升级 |
| **deprecated** | 计划弃用 | `status: deprecated` + `deprecated_date` + `successor` | 人类手动标记 |
| **archived** | 已归档，只读 | `status: archived` | deprecated_date 后 90 天自动归档 |

### 23.2 状态流转

```
draft → active → deprecated → archived
                      ↓
              (successor 接替)
```

### 23.3 弃用协议

1. 标记 `status: deprecated` + 设置 `deprecated_date`
2. 在 AIGP.md 治理声明节添加弃用通知
3. 如有替代程序，设置 `successor` 字段
4. 弃用窗口期: `deprecated_date` 后至少 90 天保持可用
5. 窗口期结束后转为 archived

### 23.4 归档协议

archived 状态的 AIGP 程序:
- 保留完整目录结构，不删除任何文件
- AIGP.md 保留完整的版本历史
- 不再接受 Evolve/Modify 操作
- 仅允许 Validate 操作 (用于审计)
- 执行器遇到 archived 程序时应返回 WARNING + 推荐 successor

---

## 24. 编排模式

AIGP 程序支持四种编排模式，通过 Mermaid 流程图中的语义标注声明。

### 24.1 模式 1: Sequential (顺序)

当前 AIGP Pipeline 已完整覆盖。模块按 Mermaid 流程图中的 `-->` 顺序执行。

```mermaid
Start --> ModuleA --> ModuleB --> ModuleC --> endNode
```

适用: Pattern A-E 的默认模式。

### 24.2 模式 2: Parallel (并发)

```mermaid
Start --> fork{并发分叉}
fork --> ModuleA
fork --> ModuleB
ModuleA --> join{汇合}
ModuleB --> join
join --> End
```

- `fork` 节点将任务分发到多个模块
- `join` 节点等待所有并发模块完成
- 各并发模块之间无数据依赖
- 适用: 独立子任务可并行处理时

### 24.3 模式 3: Conditional (条件分支)

```mermaid
Start --> Classify{分类}
Classify -->|类型A| ModuleA
Classify -->|类型B| ModuleB
Classify -->|其他| ModuleDefault
```

- 条件分支通过 Classify 节点的 `|标签|` 语法标注
- 当前 Mermaid 流程图已支持此语法，无需新增格式
- 适用: 意图路由、输入类型分发

### 24.4 模式 4: Handoff (控制权转移)

适用于 Pattern F Ecosystem 中跨组件的控制权转移:

```
handoff_context = {
    "source": "component_a_aigp",
    "target": "component_b_aigp",
    "intent": "process_health_data",
    "payload": { ... },
    "metadata": { "timestamp": "...", "trace_id": "..." }
}
```

流程:
1. 发起者将完整上下文打包为 `handoff_context`
2. 接收者从 `handoff_context` 恢复状态
3. 接收者完成后返回 `handoff_result`
4. 发起者确认结果或发起新的 handoff

---

## Part V: 质量与兼容

---

## 25. 版本兼容性

### 25.1 协议版本兼容保证

| 版本范围 | 兼容保证 |
|---------|---------|
| AIGP V1.x.y | 同一 major 版本内向后兼容 |
| AIGP V2.0.0+ | 可能引入破坏性变更，提供迁移指南 |

### 25.2 程序版本规范

AIGP 程序版本遵循 semver:

| 版本变化 | 含义 | 示例 |
|---------|------|------|
| **major** (x.0.0) | 破坏性变更 — 输入/输出格式变化 | 1.0.0 → 2.0.0 |
| **minor** (x.y.0) | 新增功能 — 向后兼容 | 1.0.0 → 1.1.0 |
| **patch** (x.y.z) | Bug 修复/改善 — 向后兼容 | 1.1.0 → 1.1.1 |

### 25.3 最低协议版本

```yaml
# AIGP.md frontmatter
min_protocol_version: "AIGP V1.0.0"
```

执行器在加载程序前检查: 若执行器支持的协议版本 < `min_protocol_version` → 拒绝加载 + 提示升级。

### 25.4 版本变更日志格式

推荐在 AIGP.md "版本历史" 可选节中使用结构化格式:

```markdown
## 版本历史

### v1.2.0 (2026-03-01)
- **新增**: 月度报告趋势分析
- **改善**: 查询性能优化

### v1.1.0 (2026-02-15)
- **新增**: 血压记录功能
- **修复**: 日期解析边界错误
```

变更类型标签: `新增` / `改善` / `修复` / `移除` / `安全`

---

## 26. 文档完整性分级

### 26.1 三级分级

| 级别 | 要求 | 适用 |
|------|------|------|
| **Level 1** (最低) | AIGP.md 必需节 (治理声明 + 功能概述 + 使用方式) | 所有 AIGP 程序 |
| **Level 2** (推荐) | + 示例交互 + 适用条件 | `status=active` 的程序 |
| **Level 3** (完整) | + 错误处理 + 版本历史 + 所有可选字段 | 公开发布到 Registry 的程序 |

### 26.2 各级别检查清单

**Level 1 (最低)**:
```
[ ] AIGP.md 存在
[ ] 12 个必需 frontmatter 字段完整
[ ] 治理声明节存在
[ ] 功能概述节存在
[ ] 使用方式节存在
[ ] 闭环印章存在
```

**Level 2 (推荐)**:
```
[ ] Level 1 全部通过
[ ] 示例交互节存在 (1-3 个场景)
[ ] 适用条件节存在 (适用 + 不适用)
[ ] quality 可选字段已填充
[ ] status = active
```

**Level 3 (完整)**:
```
[ ] Level 2 全部通过
[ ] 错误处理节存在
[ ] 版本历史节存在 (结构化格式)
[ ] trust_level 已声明
[ ] permissions 已声明 (如 trust_level >= T3)
[ ] runtime 已声明
[ ] intent_examples 已填充
[ ] governance_hash 已计算
[ ] benchmark 已填充
```

---

## Appendix A: PL24 Auto-Fix Protocol

适用: AutoFixEngine 生成修复提案时。

| 约束 | 说明 |
|------|------|
| **(a) SCOPE** | 修复限于 1-3 文件，符号变更 ≤ 10，行变更 ≤ 50 |
| **(b) CONFIDENCE** | 置信度 ≥ 0.85 时自动应用，否则作为建议需人工批准 |
| **(c) RATE LIMIT** | 每个对象每天最多 1 次自动修复，防止无限循环 |
| **(d) AUDIT** | 所有自动修复记录到 observability.lint_report |
| **(e) ROLLBACK** | 所有自动修复可回滚 (git 格式) |
| **(f) NO LOGIC CHANGE** | 仅限格式/样式/缺失声明/版本约束修复，禁止算法或业务逻辑变更 |

---

## Appendix B: PL25 License Declaration

适用: 所有 AIGP 程序，特别是 aigp-store 分发。

### B.1 核心规则

| 规则 | 说明 |
|------|------|
| **(a) LICENSE FIELD** | AIGP.md 必须包含 `license` 字段 |
| **(b) SPDX VALIDITY** | 值必须为有效 SPDX 标识符 (如 "Apache-2.0", "MIT") 或 "proprietary" |
| **(c) PROPRIETARY** | license 为 "proprietary" 时，必须附带 `terms_url` 或 `contact` |
| **(d) STORE** | 通过 aigp-store 分发时 license 字段强制要求 |

### B.2 字段属性

| 属性 | 值 |
|------|-----|
| 字段名 | `license` |
| 类型 | `string` |
| 是否必填 | 可选（本地程序）/ **强制**（Store 上架） |
| 默认值 | `proprietary`（未声明时视为保留所有权利） |
| 格式规范 | SPDX 标准标识符（见 https://spdx.org/licenses/ ）|

### B.3 SPDX 常用值参考

| 值 | 含义 |
|----|------|
| `MIT` | MIT 许可证（最宽松） |
| `Apache-2.0` | Apache 2.0（含专利保护） |
| `GPL-3.0` | GPL v3（强 copyleft） |
| `proprietary` | 专有/保留所有权利 |
| `CC-BY-4.0` | 知识共享署名（适合文档类程序） |

### B.4 默认值行为

- `license` 字段**可选**（本地使用时）
- 未填写时，程序默认视为 `proprietary`
- 不影响现有程序运行（向后兼容）

### B.5 `proprietary` 附加要求

当 `license: proprietary` 时，必须附带以下字段之一：

```yaml
license: proprietary
terms_url: https://example.com/terms   # 或
contact: author@example.com            # 至少一项必填
```

### B.6 aigp-store 上架集成

aigp-store 注册条目直接从 AIGP.md 读取 `license` 字段展示：

```json
{
  "program_id": "publisher.domain/program_name",
  "version": "1.0.0",
  "license": "MIT",
  "store_url": "https://aigp.store/programs/publisher.domain/program_name"
}
```

上架检查：
- 缺少 `license` 字段 → Store 注册 API 返回错误，拒绝上架
- `license: proprietary` 但无 `terms_url`/`contact` → 拒绝上架

### B.7 向后兼容保证

| 场景 | 行为 |
|------|------|
| 现有无 `license` 字段的程序 | 正常运行，默认视为 `proprietary` |
| 本地使用但不上架 Store | 完全不受影响 |
| 提交 Store 但未填 `license` | Store 注册 API 返回错误，拒绝上架 |

---

## Appendix C: Category M — Tool Directory Simulation Scenarios

适用: Pattern G 程序。

| 场景 | 说明 |
|------|------|
| M1 | 正常 MCP Server 启动和工具调用 |
| M2 | MCP Server 启动失败，降级处理 |
| M3 | Python 依赖安装失败 |
| M4 | MCP Server 工具调用超时 |
| M5 | governance_hash 不匹配 (Code Trust Gate 拦截) |
| M6 | ZIP SLIP 攻击 (tool_dirs 中的恶意路径) |
| M7 | 网络权限违规 (未声明的 import requests) |
| M8 | 依赖版本未固定 (TS ^ 前缀检测) |
| M9 | go.sum 缺失 |
| M10 | Rust 预编译二进制哈希不匹配 |
| M11 | shell-tools 存在但 trust_level < T4 |
| M12 | 多语言 MCP Server 部分启动失败 |

---

Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev
