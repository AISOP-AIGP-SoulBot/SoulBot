# AIGP Structural Specification

---

## Table of Contents

**Part I: Protocol Foundations**
1. [Protocol Declaration](#1-protocol-declaration)
2. [Core Definitions: AISOP = Language, AIGP = Rules](#2-core-definitions)
3. [AIGP.md Rules](#3-aigpmd-rules)

**Part II: Structural Specification**
4. [Node = Functional Responsibility](#4-node--functional-responsibility)
5. [Functional Node Count](#5-functional-node-count)
6. [Progressive Node Guidelines](#6-progressive-node-guidelines)
7. [fractal_exempt Annotation](#7-fractal_exempt-annotation)
8. [Pattern Selection](#8-pattern-selection)
9. [Pattern A-G Detailed Definitions](#9-pattern-a-g-detailed-definitions)
10. [main.aisop.json Rules](#10-mainaisopjson-rules)
11. [Functional Module Rules](#11-functional-module-rules)
12. [Independent Function Judgment](#12-independent-function-judgment)
13. [Sub_AIGP Split Rules](#13-sub_aigp-split-rules)
14. [Pattern Upgrade Convergence Handling](#14-pattern-upgrade-convergence-handling)
15. [Dual-Stream Rules](#15-dual-stream-rules)

**Part III: Security & Runtime**
16. [Trust Levels](#16-trust-levels)
17. [Permission Boundaries](#17-permission-boundaries)
18. [Integrity Verification](#18-integrity-verification)
19. [Runtime Constraints](#19-runtime-constraints)
20. [Error Handling Protocol](#20-error-handling-protocol)

**Part IV: Engineering Capabilities**
21. [Discovery Protocol](#21-discovery-protocol)
22. [Dependency Resolution](#22-dependency-resolution)
23. [Program Lifecycle](#23-program-lifecycle)
24. [Orchestration Patterns](#24-orchestration-patterns)

**Part V: Quality & Compatibility**
25. [Version Compatibility](#25-version-compatibility)
26. [Documentation Completeness Levels](#26-documentation-completeness-levels)

---

## Part I: Protocol Foundations

---

## 1. Protocol Declaration

```
AIGP Structural Specification
Protocol: AIGP V1.0.0
Authority: aigp.dev
Seed: aisop.dev
Axiom 0: Human Sovereignty and Benefit

This document defines the structural specification for AIGP programs, including:
- AIGP.md project declaration rules
- Pattern A-G fractal patterns
- Node counting and splitting strategies
- Security, runtime, discovery, dependency, lifecycle, and orchestration protocols

All AIGP programs must follow this specification.
AISOP file format (.aisop.json) as the underlying language is not governed by this document.
```

---

## 2. Core Definitions

> AISOP is the programming language, AIGP is the programming rules.

| Concept | Analogy | Definition |
|------|------|------|
| **AISOP** | Programming language (Java/Python) | Underlying language — defines file format (`.aisop.json`), syntax structure (`role/content`), execution model |
| **AIGP** | Programming rules (coding standards/design patterns) | Governance protocol — defines how programs should be written, quality standards, security guards, axiom constraints |
| **AIGP Program** | A standards-compliant project | A complete project written in AISOP language following AIGP rules |
| **AIGP Creator** | Project scaffolding (`create-react-app`) | Tool for creating AIGP programs — is itself an AIGP program (bootstrapping) |

```
Naming conventions:
  .aisop.json  →  Language format identifier (what language the file is written in)
  _aigp        →  Program type identifier (what rules the directory follows)
  AIGP.md      →  Project declaration (similar to pyproject.toml / pom.xml)
```

### 2.1 AISOP File Field Responsibilities

> Each field has one and only one responsibility. Information appears in only one place.

| Field | Responsibility | Content |
|------|------|------|
| `id` | Identity | Unique identifier for programs and modules |
| `name` | Name | Product name + version number |
| `version` | Version | Semantic version number |
| `summary` | Capability overview | One sentence describing "what I can do" |
| `description` | Detailed description | Architecture, history, patterns, implementation details |
| `system_prompt` | **Behavioral guidelines** | Defines how the agent should behave (the sole behavior definition layer) |
| `instruction` | **Execution instruction** | Fixed as `RUN aisop.main` (immutable constant) |
| `aisop.main` | Execution graph | Main Mermaid flowchart — all execution starts here |
| `functions` | Execution logic | Specific steps and constraints for each node |

### 2.2 instruction Immutable Constant

```
Rule: The instruction field of every AISOP file must be exactly: RUN aisop.main
```

**Rationale**:
- `RUN` is a machine execution instruction, not a natural language suggestion. Analogous to Dockerfile `RUN`, SQL `SELECT`.
- `aisop.main` is a JSON structural path, pointing to the `content.aisop.main` execution graph.
- Program identity is provided by the `id` field; no need to repeat in instruction.
- Capability description is provided by `summary`/`description`; no need to repeat in instruction.

```
C language analogy:
  int main() { ... }     ← Entry is always main, uniform across all programs
  RUN aisop.main          ← Entry is always aisop.main, uniform across all AISOP files
```

**sub_mermaid**: Even if the aisop object contains multiple graphs (e.g., `main`, `orchestrate`, `memory`), the entry point is still `aisop.main`. The main graph routes to sub-graphs internally through parameters.

### 2.3 system_prompt Behavioral Layer Rules

```
Rule: system_prompt is the behavioral layer — defines how the agent should behave, not what it is or how it's built.
```

**Must include**:
1. **Role positioning** — the agent's behavioral role (not the product name)
2. **Domain behavioral guidelines** — behavioral constraints specific to the domain
3. `Mirror User's exact language and script variant.` — multilingual requirement
4. `Align: Human Sovereignty and Benefit.` — Axiom 0 seal

**Must not include**:
- Product name or version number → already in `name` + `version` fields
- Architecture or pattern details → already in `description` field
- Module filenames or delegation logic → already in `functions` field
- Capability lists → already in `summary` field

```
Format template:
  "{behavioral role}. {domain guidelines}. Mirror User's exact language and script variant.
   Align: Human Sovereignty and Benefit."

Good example:
  "Personal expense tracking assistant. Prioritize numerical precision.
   Protect user financial privacy. Mirror User's exact language and script variant.
   Align: Human Sovereignty and Benefit."

Bad example:
  "Expense Tracker v1.0.0. Pattern B router: delegate data operations
   to record.aisop.json. Mirror User's exact language and script variant.
   Align: Human Sovereignty and Benefit."
   ↑ Contains product name+version(name), architecture(description), filenames(functions)
```

---

## 3. AIGP.md Rules

Every `{name}_aigp/` directory **must** contain an AIGP.md file. AIGP.md is the project's governance contract and discovery entry point.

### 3.1 Required Fields (YAML frontmatter)

**Governance Fields (6)**:

| Field | Type | Description |
|------|------|------|
| `protocol` | string | AIGP version number, e.g., `"AIGP V1.0.0"` |
| `authority` | string | Governance authority domain, fixed as `aigp.dev` |
| `seed` | string | Format seed domain, fixed as `aisop.dev` |
| `executor` | string | Execution platform domain, fixed as `soulbot.dev` |
| `axiom_0` | string | Core axiom, fixed as `Human_Sovereignty_and_Benefit` |
| `governance_mode` | string | `NORMAL` or `DEV` |

**Project Fields (6)**:

| Field | Type | Description |
|------|------|------|
| `name` | string | Project name (snake_case) |
| `version` | string | Current version (semver, synchronized with main.aisop.json) |
| `pattern` | string | Structural pattern `A|B|C|D|E|F` |
| `summary` | string | 1-2 sentence feature overview |
| `tools` | list/object | Tool declarations (see §3.3) |
| `modules` | list | Module inventory (see §3.4) |

### 3.2 Optional Fields (YAML frontmatter)

**Basic Optional Fields**:

| Field | Type | Description |
|------|------|------|
| `governance_hash` | string | Governance hash (see §18) |
| `quality` | object | `{weighted_score, grade, last_pipeline}` |
| `description` | string | Agent Skills compatible field — skill description |
| `tags` | list | Classification tags |
| `author` | string | Author information |
| `license` | string | License |
| `tool_dirs` | list | Pattern G tool directory declarations (see §9 Pattern G) |
| `capabilities` | object | Runtime capability declarations `{offered, required}` |

**Security & Runtime Optional Fields** (Part III):

| Field | Type | Default | Description |
|------|------|--------|------|
| `trust_level` | number (1-4) | 3 | Trust level (see §16) |
| `permissions` | object | null | Permission boundaries (see §17) |
| `runtime` | object | null | Runtime constraints (see §19) |

**Engineering Optional Fields** (Part IV):

| Field | Type | Default | Description |
|------|------|--------|------|
| `status` | string | "draft" | Lifecycle state (see §23) |
| `deprecated_date` | string | null | Deprecation date |
| `successor` | string | null | Replacement program name |
| `intent_examples` | list | [] | Semantic routing anchors (see §21) |
| `discovery_keywords` | list | [] | Keyword index |
| `dependencies` | list | [] | Cross-project dependencies (see §22) |
| `min_protocol_version` | string | null | Minimum protocol version (see §25) |
| `benchmark` | object | null | Quality benchmark declaration |
| `identity` | object | null | Program identity and provenance (see I11) — `{ program_id, publisher, verified_on }` |

### 3.3 tools Field Specification

**Compact format** (backward compatible):

```yaml
tools: [file_system, shell]
```

**Structured format** (recommended):

```yaml
tools:
  - name: file_system
    required: true
    min_version: "1.0"
  - name: shell
    required: false
    fallback: "degrade"       # Degrade when unavailable
```

| Attribute | Type | Default | Description |
|------|------|--------|------|
| `name` | string | (required) | Tool name |
| `required` | boolean | true | Whether the tool is required |
| `min_version` | string | null | Minimum version requirement |
| `fallback` | string | null | Degradation strategy when unavailable: `"degrade"` / `"skip"` / `"error"` |

### 3.4 modules Field Specification

```yaml
modules:
  - id: health_tracker.record
    file: record.aisop.json
    nodes: 7
    critical: true              # Whether it is a critical module (default true)
    idempotent: true            # Whether it is idempotent (default false)
    side_effects: [file_write]  # Side effect declarations (default [])
```

| Attribute | Type | Default | Description |
|------|------|--------|------|
| `id` | string | (required) | Module unique identifier `{project}.{module}` |
| `file` | string | (required) | Filename |
| `nodes` | number | (required) | Number of functional nodes |
| `critical` | boolean | true | Whether to trigger FATAL on failure (see §20) |
| `idempotent` | boolean | false | Whether repeated execution is safe |
| `side_effects` | list | [] | Side effect list: `file_write`, `file_delete`, `api_call`, `shell_exec` |

Empty `side_effects` list = pure function (no side effects).

### 3.5 Markdown Body

**Required sections**:

| Section | Content |
|---|------|
| **Governance Declaration** | Declare adherence to AIGP protocol + Axiom 0 alignment |
| **Feature Overview** | List core features by module/intent |
| **Usage** | Entry file, tool requirements, prerequisites |

**Recommended sections** (when status=active):

| Section | Content |
|---|------|
| **Example Interactions** | 1-3 typical usage scenario input/output examples |
| **Applicable Conditions** | Clearly state scenarios where the program is and is not applicable |

**Optional sections**:

| Section | Content |
|---|------|
| **Data Storage** | Data file paths and formats |
| **Configuration** | Configurable parameters and defaults |
| **Quality Status** | ThreeDimTest scores, Pipeline history |
| **Version History** | Major version change summaries (structured format see §25) |
| **Error Handling** | Common errors and user handling instructions |

**File ending**: Must end with the AIGP closing seal.

| governance_mode | Seal Format |
|----------------|---------|
| NORMAL | `Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev` |
| DEV | `[L0_BOOT: Success] [L1_REPORT: Success] [endNode_Align: Human Sovereignty and Benefit]. Version: AIGP V1.0.0. www.aigp.dev` |

### 3.6 Creator Auto-Maintenance Rules

| Trigger Event | Creator Behavior |
|---------|-------------|
| **Create** | Auto-generate AIGP.md, populate all required fields, set status to draft |
| **Evolve** | Update version, modules, quality, summary (if changed) |
| **Modify** | Update version, quality |
| **Validate** | Check AIGP.md existence and field completeness (D8 check) |
| **QualityGate Pass** | If status=draft, automatically upgrade to active |
| **version_history snapshot** | Save AIGP.md snapshot in `{version}/` directory |

---

## Part II: Structural Specification

---

## 4. Node = Functional Responsibility

> Nodes match functions, main routes and dispatches, modules are self-contained, shared logic is extracted separately, no infinite splitting.

Each Mermaid node represents one functional responsibility of a module, similar to a function in a Python file. The number of nodes is naturally determined by functional complexity, not imposed by external hard limits.

```
Python analogy:
  record.py has 4 functions → record.aisop.json has 4 functional nodes
  query.py has 6 functions  → query.aisop.json has 6 functional nodes
  Node count follows function count, not quotas
```

---

## 5. Functional Node Count

```
Functional nodes = Total Mermaid nodes - Start - endNode
```

Start and endNode are the fixed structural framework of every AISOP file (similar to Python's `if __name__`), they don't reflect functional complexity and are not counted.

Example:

```
graph TD
    Start --> Parse --> Validate{OK?} --> Save --> Alert --> endNode
                                       --> AskFix --> Parse
```

Total nodes 7, functional nodes 5 (Parse, Validate, Save, Alert, AskFix).

---

## 6. Progressive Node Guidelines

Applies to all `.aisop.json` files (including main):

```
Functional nodes 3-12  → Normal, no prompt
Functional nodes 13-15 → ADVISORY — Suggest checking for split opportunities, provide specific suggestions
Functional nodes 16+   → RECOMMENDED — Strongly recommend splitting, provide split plan
```

- Both levels are WARNING, not FAIL
- Functionally cohesive large modules can annotate `fractal_exempt` to skip the suggestion
- Minimum requirement: >=3 functional nodes + (>=1 tool call OR >=3 steps)

---

## 7. fractal_exempt Annotation

When a module's functional nodes exceed 12 but the flow is highly cohesive, annotate in `system.content`:

```json
{
    "fractal_exempt": "The pipeline's 13 stages form a continuous pipeline; splitting would cause context fragmentation"
}
```

After annotation, Creator skips the progressive split suggestion for that file. Equivalent to Python's `# noqa`.

---

## 8. Pattern Selection

```
Number of independent functions → Pattern:
  1 function              → A: Script (single file)
  2+ functions            → B: Package (multiple files)
  2+ functions + complex shared → C: Package + Shared
  Sub-modules also need splitting → D: Nested Package
  With memory layer       → E: Package + Memory
  Multi-AIGP program ecosystem → F: Ecosystem
  With embedded tool directory → G: Embedded Runtime
```

---

## 9. Pattern A-G Detailed Definitions

### Pattern A: Script

```
{name}_aigp/
├── AIGP.md                     # Required: governance contract
└── main.aisop.json             # All logic
```

Applicable: todo list, timer, calculator, and other single-function programs. No hard limits. Progressive guidelines apply.

### Pattern B: Package

```
{name}_aigp/
├── AIGP.md                     # Required: governance contract
├── main.aisop.json             # Router: intent recognition → dispatch
├── {func1}.aisop.json          # Functional module (fully self-contained)
├── {func2}.aisop.json
└── {func3}.aisop.json
```

Example:
```
expense_tracker_aigp/
├── AIGP.md                     # Governance contract
├── main.aisop.json             # Intents: record / query / budget / report
├── record.aisop.json           # Validate → Write → Confirm
├── query.aisop.json            # Parse → Read → Filter → Format
├── budget.aisop.json           # Set → Check → Alert
└── report.aisop.json           # Aggregate → Analyze → Display
```

### Pattern C: Package + Shared

```
{name}_aigp/
├── AIGP.md                     # Required: governance contract
├── main.aisop.json             # Router
├── {func1}.aisop.json
├── {func2}.aisop.json
└── shared.aisop.json           # Complex shared logic called by 2+ modules
```

Shared rule: Create only when 2+ modules reuse **complex operations**. Simple sharing (formatting/style) goes in each module's system_prompt.

### Pattern D: Nested Package

```
{name}_aigp/
├── AIGP.md                     # Required: governance contract
├── main.aisop.json             # Top-level router
├── {simple_func}.aisop.json    # Simple module
└── {complex}_sub_aigp/         # Complex module (has sub-structure)
    ├── AIGP.md                 # Sub-package governance contract (if independently published)
    ├── main.aisop.json         # Sub-router
    ├── {sub1}.aisop.json
    └── {sub2}.aisop.json
```

Nesting rule: Maximum 2 levels, nest only when the sub-module itself has 2+ sub-functions.

#### Pattern D Example: AIGP Creator

```
aigp_creator_aigp/
├── AIGP.md                     # Governance contract (AIGP V1.0.0)
├── main.aisop.json             # Top-level orchestrator (21 functional nodes, fractal_exempt)
│   └── Intents: Create, Evolve, Modify, Validate, Simulate, Compare, Explain, General
│   └── Pipeline: Research→Evolve→Generate→Modify→QualityGate→Validate→Simulate→Observability→Review
├── generate.aisop.json         # Generator (10 functional nodes)
├── research.aisop.json         # Shared research module (14 functional nodes, fractal_exempt, 3-mode reuse)
├── review.aisop.json           # Reviewer (9 functional nodes)
├── simulate.aisop.json         # Simulator (7 functional nodes)
├── modify.aisop.json           # Modifier (9 functional nodes)
├── observability.aisop.json    # Telemetry analysis (5 functional nodes)
├── advisor.aisop.json          # Advanced advisor (24 functional nodes, fractal_exempt, 4 mutually exclusive sub-graphs)
├── AIGP_Standard.core.aisop.json         # Core quality standard (C1-C7, I1-I7, D1-D7, PL1-PL12, PL19-PL21, MF1-MF9)
├── AIGP_Standard.security.aisop.json     # Security extension (I8-I11, D8-D10, AT1-AT6)
├── AIGP_Standard.ecosystem.aisop.json    # Ecosystem extension (MF10-MF14, K1-K4, PL16-PL17)
├── AIGP_Standard.performance.aisop.json  # Performance extension (PL13-PL15, PL18, QRG1-QRG4, E.injection)
└── AIGP_Protocol.md            # Structural specification (Protocol-level)
```

Characteristics:
- 8+4 modules (8 executable modules + 4 STANDARD extension files), ~100 functional nodes total
- main is a pure orchestrator (sequential delegation, no business logic), annotated fractal_exempt
- research reuses 3 modes via ModeGate (structure/quality/compliance), annotated fractal_exempt
- advisor uses sub_mermaid sub-graphs (4 mutually exclusive sub-graphs), actual single-path maximum 12 nodes
- Communication topology is star-shaped (main orchestrates), no direct inter-module communication

### Pattern E: Package + Memory

```
{name}_aigp/
├── AIGP.md                     # Required: governance contract
├── main.aisop.json             # Router
├── {func1}.aisop.json
├── {func2}.aisop.json
└── memory/                     # Memory layer
    ├── schema.json             # Memory field definitions (episodic/semantic/working)
    ├── decay_config.json       # Decay strategy parameters
    └── context_manager.json    # Context budget and loading strategy
```

Applicable: AIGP programs requiring cross-session memory, personalization, or RAG retrieval. Use advisor.aisop.json (advisor_type='memory') to generate memory/ directory content.

### Pattern F: Ecosystem

```
{ecosystem_name}/
├── AIGP.md                     # Required: ecosystem-level governance contract
├── blueprint.json              # Ecosystem blueprint (components, interfaces, topology)
├── {component1}_aigp/          # Independent component (Pattern A-E)
│   ├── AIGP.md                 # Required: component-level governance contract
│   └── main.aisop.json
├── {component2}_aigp/
│   ├── AIGP.md
│   └── ...
└── shared/                     # Cross-component shared data contracts
    └── data_contracts.json
```

Applicable: Complex systems with 3+ AIGP program components collaborating. Use advisor.aisop.json (advisor_type='orchestrate') to design ecosystem blueprints.

#### blueprint.json Component Interface Declaration

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
├── AIGP.md                     # Required: governance contract (with tool_dirs field)
├── main.aisop.json             # Router
├── {func1}.aisop.json
├── {func2}.aisop.json
├── python-tools/               # Python tool implementations
│   ├── README.md               # Required: tool description, interfaces, security constraints
│   ├── requirements.txt        # Frozen versions (== pinning, >= / * / ~= prohibited)
│   ├── *.py                    # Tool code
│   └── mcp_adapter.py          # Creator auto-generated MCP stdio endpoint
├── ts-tools/                   # TypeScript tool implementations
│   ├── README.md
│   ├── package.json            # Exact versions (^ ~ prohibited)
│   ├── package-lock.json       # Lock transitive dependencies
│   └── *.ts
├── go-tools/                   # Go tool implementations
│   ├── README.md
│   ├── go.mod + go.sum         # Dependency lock
│   └── bin/tool                # Pre-compiled binary (recommended)
├── rust-tools/                 # Rust tool implementations
│   ├── README.md
│   ├── Cargo.toml + Cargo.lock
│   └── target/release/tool     # Must be pre-compiled
├── shell-tools/                # Shell scripts (T4 + manual audit only)
│   ├── README.md
│   └── tool.sh / tool.ps1
├── mcp-tools/                  # MCP Server definition layer
│   └── mcp_server.json         # MCP Server manifest + runtime declaration
├── a2a-tools/                  # A2A Agent Card layer (optional)
│   └── agent_card.json
├── n8n-tools/                  # n8n workflow automation layer (optional)
│   ├── workflow.json
│   └── config.json
├── other-tools/                # Open extension layer (optional)
│   └── README.md               # Required: invocation method, interfaces, security constraints
└── memory/                     # Pattern E memory layer (optional)
    └── ...
```

Inherits: All rules from Pattern E or F

Additional requirements:
- AIGP.md must include a `tool_dirs` field declaring tool directories
- `mcp-tools/mcp_server.json` must exist
- I13 Embedded Code Safety rules apply (6 sub-checks)
- MF16 Tool Directory Consistency rules apply
- Minimum trust level: T3
- Requires Code Trust Gate verification

Characteristics:
- CLI executors have native shell tools and can directly execute bundled code
- No intermediate layer or pre-installed tools needed
- Self-contained, independently deployable

#### Supported tool_dirs Directory Types

| Type | Runtime | Dependency Lock | Use Cases |
|------|--------|---------|---------|
| `python-tools/` | Python 3.9-3.13 | `requirements.txt` (== pinning) | Data processing, AI/ML, file operations |
| `ts-tools/` | Node.js/Deno/Bun | `package-lock.json` | Web API, JSON processing, type safety |
| `go-tools/` | Go or pre-compiled binary | `go.sum` | High concurrency, CLI, low latency |
| `rust-tools/` | Pre-compiled binary | `Cargo.lock` | High performance, memory safety, WASM |
| `shell-tools/` | bash / pwsh | None | System scripts (T4 only) |
| `mcp-tools/` | stdio transport | `mcp_server.json` | MCP ecosystem tools |
| `a2a-tools/` | A2A protocol | `agent_card.json` | Inter-agent collaboration |
| `n8n-tools/` | n8n instance | `workflow.json` | Multi-service integration |
| `other-tools/` | Custom | README.md | Open extension |

#### mcp_server.json Format

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

Pattern G programs must pass the Code Trust Gate security verification upon loading:

```
Load Pattern G program
    ↓
Code Trust Gate:
  1. governance_hash verification (covers all files including tool_dirs source code)
  2. Static analysis: import/require declarations vs permissions.network
  3. File hash verification (against mcp_server.json file_hashes)
  4. Trust level check (Pattern G minimum T3)
  5. Dependency lock file verification
    ↓
  [T3 mode] Requires human review confirmation
  [T4 mode] Auto-pass
    ↓
Start MCP Server (stdio)
    ↓
AIGP program execution (invokes tools via MCP)
```

#### I13 Embedded Code Safety (6 Sub-Checks)

Applicable: Pattern G programs (with tool_dirs). Pattern A-F marked N/A.

| Sub-Check | Description |
|--------|------|
| **(a) CODE INTEGRITY** | SHA-256 hashes of all source/binary files in tool_dirs/ must be recorded in mcp_server.json file_hashes |
| **(b) NETWORK DECLARATION** | Detect network access APIs (requests/fetch/net/http, etc.); if present, permissions.network.allowed must be true |
| **(c) FILE SYSTEM SCOPE** | File write operations must not exceed permissions.file_system.scope |
| **(d) DEPENDENCY VERSION PINNING** | Python: == pinning; TS/JS: ^ ~ prohibited; Go: go.sum must exist; Rust: Cargo.lock must exist |
| **(e) MCP PROXY REQUIRED** | All code tools must be exposed through the mcp-tools/ layer; executor direct subprocess execution of source files is prohibited |
| **(f) SHELL AUDIT** | When shell-tools/ exists, trust_level must be ≥ T4 |

#### MF16 Tool Directory Consistency

Applicable: Pattern G programs.

| Check | Description |
|------|------|
| **(a)** | mcp_server.json exists at the declared path |
| **(b)** | mcp_server.json exposed_tools entries have corresponding declarations in AIGP.md tools[] |
| **(c)** | AIGP.md tools[] entries referencing mcp_server exist in exposed_tools |
| **(d)** | a2a agent_card.json governance_hash matches AIGP.md |

#### Backward Compatibility

- The tool_dirs field is entirely optional
- Programs without tool_dirs (Pattern A-F) are unaffected
- I13 and MF16 are marked N/A for non-Pattern G programs
- The governance_hash algorithm is unchanged for non-Pattern G programs

---

## 10. main.aisop.json Rules

main follows the same progressive node guidelines as functional modules. The distinction is a **qualitative constraint** (not a quantitative one):

**Pattern A**: main is the only file, contains all logic, no special constraints.

**Pattern B+**: main is a router:
- Contains only routing logic + lightweight inline handling
- No business logic (data processing, file I/O, complex validation)
- tools = union of all sub-module tools
- The number of routing nodes is naturally determined by the number of intents
- Invocation method: intent recognition → read corresponding sub-file → AI Agent executes

```
Determining whether a node belongs to main:
  ≤2 steps + no tool calls → OK (lightweight inline, e.g., Explain, General)
  >2 steps or has tool calls → should be placed in sub_aisop
```

---

## 11. Functional Module Rules

- Fully self-contained (independent system_prompt / tools / parameters / functions)
- Does not depend on other modules' internal implementations
- Module internal depth is determined by function, progressive guidelines apply
- Minimum requirement: >=3 functional nodes + (>=1 tool call OR >=3 steps)

---

## 12. Independent Function Judgment

Can be described in one sentence + does not share dedicated tools/state + can be tested independently → separate into its own file

- Level 1 tools (file_system, shell) are general infrastructure and do not count as "shared tools"
- Modules that read/write the same data file via file_system can still be independent (each responsible for different operations)
- "Shared state" refers to runtime memory state or dedicated connections, not persisted data files

---

## 13. Sub_AIGP Split Rules

When Creator suggests splitting, analyze split boundaries in the following priority order:

```
Priority 1 — Tool boundaries:
  Node group A uses google_search + web_browser
  Node group B uses only file_system
  → Natural boundary, split into independent sub_aigp

Priority 2 — Data flow stages:
  Clear stage boundaries in a linear pipeline (research → generate → test)
  → Each stage is a sub_aigp candidate

Priority 3 — Functional independence:
  Meets the three conditions for independent function judgment
  → Split into sub_aigp
```

**Patterns that must not be split**:
- Convergence node groups (many-to-one fan-in pattern) → keep in the same sub_aigp
- Error recovery loops (Error → Retry → original node) → keep in the same sub_aigp
- Tightly coupled nodes sharing the same tool + state → keep in the same sub_aigp

---

## 14. Pattern Upgrade Convergence Handling

When upgrading from Pattern A→B and splitting files, existing convergence/display nodes (e.g., Respond, Display, Output) need special handling:

```
Convergence node determination:
  Does the node have >2 steps or tool calls?
    → Does not meet main inline criteria, must be assigned to a sub-module

  Do multiple sub-modules need this node's logic?
    → Each sub-module creates its own dedicated version (customized to its output format)
    → Do not create shared.aisop.json (unless logic is complex and completely identical)

  Only one sub-module uses it?
    → Directly include in that sub-module
```

Example:
```
Pattern A (before split):
  SearchRecipes → ReadRecipe → NutritionAnalysis → Respond → endNode
  SaveCollection → Respond → endNode
  CompareView → Respond → endNode
  (Respond is a full-path convergence point, 4 steps + tool references)

Pattern B (after split):
  search.aisop.json:  ...→ SearchRespond → endNode  (search result display)
  collection.aisop.json: ...→ CollectionRespond → endNode (collection operation display)
  (Each sub-module has a dedicated Respond, content customized per module output)
```

---

## 15. Dual-Stream Rules

Complex projects (Pattern D+) may optionally provide both human-readable and AI-optimized versions:

```
{name}_aigp/
├── AIGP.md
├── main.human.aisop.json      # Human-readable version (full key names)
├── main.ai.aisop.json         # AI-optimized version (compressed key names)
└── ...
```

Rules:
- Both versions must have completely identical logical semantics
- `.human` version uses full key names, convenient for human review
- `.ai` version uses abbreviated key names, reducing token consumption
- AI Agent preferentially loads the `.ai` version, loads the `.human` version for debugging
- Non-dual-stream projects still use a single `.aisop.json` (without `.human` or `.ai` prefix)

---

## Part III: Security & Runtime

---

## 16. Trust Levels

AIGP programs declare their permission requirements and execution modes through `trust_level`.

### 16.1 Four-Tier Trust Definition

| Tier | Name | Meaning | Permission Scope |
|------|------|------|---------|
| **T1** | Metadata-Only | Read AIGP.md frontmatter only | Does not load .aisop.json content |
| **T2** | Instruction-Read | Can read .aisop.json instruction content | Cannot execute any tool calls |
| **T3** | Supervised | Requires human approval or sandbox environment for execution | Each tool call requires confirmation |
| **T4** | Autonomous | Executes autonomously within declared permission boundaries | Follows permissions field constraints |

### 16.2 Relationship Between Trust Levels and Capabilities

| trust_level | Executable Operations | Typical Use Cases |
|-------------|-------------|---------|
| T1 | Read summary, name, description | Program directory indexing, search result display |
| T2 | Read complete flowcharts, function definitions | Code review, documentation generation, teaching |
| T3 | Execute all tool calls under human supervision | First-run new programs, high-risk operations |
| T4 | Autonomously execute all declared tool calls | Verified production programs |

### 16.3 Declaration Method

```yaml
# AIGP.md frontmatter
trust_level: 3    # Default value, optional field
```

When trust_level is not declared, the executor should treat it as T3 (Supervised).

---

## 17. Permission Boundaries

T4 (Autonomous) programs **must** declare permission boundaries through `permissions`. This field is optional for T1-T3 programs.

### 17.1 Declaration Format

```yaml
# AIGP.md frontmatter
permissions:
  file_system:
    scope: "./data/"            # Read/write scope restriction (relative to project root)
    operations: ["read", "write"]
  shell:
    allowed: false              # Prohibit shell calls
  network:
    allowed: false              # Prohibit network calls
```

### 17.2 Permission Types

| Permission | Attribute | Description |
|------|------|------|
| **file_system** | `scope` | Directories allowed for access (glob syntax) |
| | `operations` | Allowed operations: `read`, `write`, `delete` |
| **shell** | `allowed` | Whether shell execution is allowed |
| | `allowlist` | List of allowed commands (only when allowed=true) |
| **network** | `allowed` | Whether network requests are allowed |
| | `endpoints` | List of allowed URL patterns |

### 17.3 Executor Responsibilities

The executor (SoulBot) **must** do the following when running T4 programs:
1. Read the `permissions` declaration
2. Verify whether tool calls are within the declared scope before execution
3. Out-of-scope calls → Reject execution + Report security violation

---

## 18. Integrity Verification

### 18.1 governance_hash Algorithm

```
governance_hash = SHA-256(
    All .aisop.json file contents (concatenated in alphabetical order by filename, CRLF→LF normalized)
)

Pattern G Extension:
  The .aisop.json file set remains unchanged. File hashes of tool_dirs/ are recorded
  in the file_hashes field of mcp_server.json, indirectly covered by governance_hash.
  The governance_hash algorithm for programs without tool_dirs remains unchanged (backward compatible).
```

Output format: `"sha256:{hash_value}"` (64-character hexadecimal)

### 18.2 Requirement Rules

| trust_level | governance_hash |
|-------------|----------------|
| T1-T2 | Optional |
| T3 | Recommended |
| T4 | Recommended |
| Published to Registry | Required |

### 18.3 Verification Process

Creator ValidateStep performs verification:
1. Compute the SHA-256 hash of the current files
2. Compare with the governance_hash declared in AIGP.md
3. Mismatch → WARNING: "Integrity check failed — files may have been modified outside Creator pipeline"

---

## 19. Runtime Constraints

### 19.1 Declaration Format

```yaml
# AIGP.md frontmatter
runtime:
  timeout_seconds: 300          # Per-execution timeout (default: executor-determined)
  max_retries: 3                # Maximum retry count (default: 3)
  token_budget: 50000           # Token budget limit (default: unlimited)
  idempotent: false             # Whether overall execution is idempotent (default: false)
  side_effects:                 # Overall side effect declarations
    - file_write
    - api_call
```

### 19.2 Field Descriptions

| Field | Meaning | Purpose |
|------|------|------|
| `timeout_seconds` | Timeout limit for a single complete execution | Prevent infinite execution |
| `max_retries` | Maximum retry count for RECOVERABLE errors | Control retry overhead |
| `token_budget` | Token consumption limit for a single execution | Cost control |
| `idempotent` | Whether repeated execution produces the same result | Orchestrator determines if safe retry is possible |
| `side_effects` | List of side effects for the overall program | Orchestrator assesses execution risk |

### 19.3 Relationship with modules

- Program-level `runtime.side_effects` = Union of all module `side_effects`
- Program-level `runtime.idempotent` = true when all critical modules are `idempotent`
- Module-level attributes (§3.4) provide fine-grained control; program-level attributes provide a quick overview

---

## 20. Error Handling Protocol

### 20.1 Error Classification

| Category | Meaning | Strategy |
|------|------|------|
| **RECOVERABLE** | Transient failures (network timeout, file lock, API throttling) | Retry per `max_retries`, exponential backoff |
| **DEGRADABLE** | Non-critical module failure (`critical: false`) | Skip failed module, execute in degraded mode, mark WARNING |
| **FATAL** | Critical module failure (`critical: true`) or security violation | Stop immediately, report error, produce no output |

### 20.2 Retry Strategy

```
Retry interval: 1s, 2s, 4s, 8s, ... (exponential backoff, base=2)
Maximum retries: runtime.max_retries (default 3)
Maximum interval: min(2^retry_count, 30) seconds
Each retry must log: error reason + retry count + timestamp
```

### 20.3 Degradation Behavior

When a module execution fails and the module has `critical: false`:
1. Skip that module's output
2. Mark in the final result: `"DEGRADED: {module_name} skipped due to {error}"`
3. Does not affect the overall success/failure determination
4. Final result includes a list of degraded modules

### 20.4 Termination Conditions

Each AIGP program execution terminates under the following conditions:

| Termination Type | Condition | Result |
|---------|------|------|
| **Successful Termination** | All critical modules completed + output passes validation | Return complete result |
| **Timeout Termination** | `runtime.timeout_seconds` reached | Return completed portion + timeout marker |
| **Error Termination** | FATAL-level error triggered | Return error report, no partial results |
| **Degraded Termination** | Successful termination but with skipped modules | Return degraded result + degradation report |

---

## Part IV: Engineering Capabilities

---

## 21. Discovery Protocol

### 21.1 Discovery Layers

| Layer | Method | Mechanism | Token Cost |
|------|------|------|-----------|
| **L1 Passive Discovery** | File system scan | Scanner traverses directories, identifies `_aigp/` directories containing AIGP.md | ~50-80/program |
| **L2 Semantic Discovery** | Intent matching | Match user queries against `intent_examples` by semantic similarity | 0 (pre-computed) |
| **L3 Registry Discovery** | Registry query | Query published programs via AIGP Registry (aigp.dev) | ~100/query |

### 21.2 L1 Scanning Protocol

The scanner should search for AIGP programs in the following order:

1. `*_aigp/` subdirectories under the current working directory
2. Configured AIGP library paths (e.g., `~/.aigp/library/`)
3. Dependency paths declared in the project's `aigp.config`

For each discovered AIGP program:
1. Read AIGP.md YAML frontmatter (L1 metadata, ~50-80 tokens)
2. Register to the available program inventory (name + summary + status)
3. Load full content only when matched (L2+L3)

### 21.3 L2 Semantic Matching

```yaml
# AIGP.md frontmatter
intent_examples:
  - "Record today's weight"
  - "View this week's blood pressure trend"
  - "Generate monthly health report"
discovery_keywords:
  - health
  - tracking
  - wellness
```

Matching process:
1. Convert `intent_examples` to embedding vectors
2. When a new query arrives, compute cosine similarity with existing vectors
3. Similarity exceeds threshold → candidate match
4. Rank using `summary` + `discovery_keywords`

### 21.4 Invocation Modes

| Mode | Trigger Method | Matching Mechanism |
|------|---------|---------|
| **Explicit Invocation** | User specifies program name (e.g., "use health_tracker") | Exact match on `name` field |
| **Implicit Invocation** | LLM automatically selects based on user intent | Semantic matching on `summary` + `intent_examples` |

---

## 22. Dependency Resolution

### 22.1 Dependency Declaration

```yaml
# AIGP.md frontmatter
dependencies:
  - name: shared_utils_aigp
    version: "^1.0.0"           # semver range constraint
    required: true
  - name: analytics_aigp
    version: ">=2.0.0"
    required: false              # Optional dependency
    fallback: "skip"             # When unavailable: "skip" / "degrade" / "error"
```

### 22.2 Version Constraint Syntax

| Syntax | Meaning | Match Examples |
|------|------|---------|
| `"1.2.3"` | Exact version | 1.2.3 only |
| `"^1.2.0"` | Compatible updates | >=1.2.0 and <2.0.0 |
| `"~1.2.0"` | Patch updates | >=1.2.0 and <1.3.0 |
| `">=1.0.0"` | Minimum version | >=1.0.0 |

### 22.3 Resolution Strategies

1. **Flat Resolution** (default) — All dependencies are resolved at the same level; when version conflicts arise, the highest compatible version satisfying all constraints is selected
2. **Isolated Resolution** — In Pattern F Ecosystem, each component resolves dependencies independently, interacting through `data_contracts`

### 22.4 Conflict Resolution

When multiple AIGP programs depend on different versions of the same program:
- Automatically select the highest version satisfying all constraints
- If no version can satisfy all constraints → Report conflict, require human decision
- Conflict report includes: conflicting dependency name, source of each constraint, possible solutions

---

## 23. Program Lifecycle

### 23.1 Lifecycle States

| State | Meaning | AIGP.md Field | Creator Behavior |
|------|------|-------------|-------------|
| **draft** | In development, unstable | `status: draft` | Automatically set during Create phase |
| **active** | Production-ready | `status: active` | Automatically upgraded after first QualityGate pass |
| **deprecated** | Planned for deprecation | `status: deprecated` + `deprecated_date` + `successor` | Manually marked by human |
| **archived** | Archived, read-only | `status: archived` | Automatically archived 90 days after deprecated_date |

### 23.2 State Transitions

```
draft → active → deprecated → archived
                      ↓
              (successor takes over)
```

### 23.3 Deprecation Protocol

1. Mark `status: deprecated` + set `deprecated_date`
2. Add deprecation notice in the AIGP.md governance declaration section
3. If a replacement program exists, set the `successor` field
4. Deprecation window: remains available for at least 90 days after `deprecated_date`
5. Transitions to archived after the window period ends

### 23.4 Archival Protocol

AIGP programs in archived state:
- Retain complete directory structure, no files are deleted
- AIGP.md retains complete version history
- No longer accept Evolve/Modify operations
- Only Validate operations are allowed (for auditing)
- Executor should return WARNING + recommend successor when encountering an archived program

---

## 24. Orchestration Patterns

AIGP programs support four orchestration patterns, declared through semantic annotations in Mermaid flowcharts.

### 24.1 Pattern 1: Sequential

Already fully covered by the current AIGP Pipeline. Modules execute in the order defined by `-->` in the Mermaid flowchart.

```mermaid
Start --> ModuleA --> ModuleB --> ModuleC --> endNode
```

Applicable: Default pattern for Pattern A-E.

### 24.2 Pattern 2: Parallel

```mermaid
Start --> fork{Parallel Fork}
fork --> ModuleA
fork --> ModuleB
ModuleA --> join{Join}
ModuleB --> join
join --> End
```

- `fork` node distributes tasks to multiple modules
- `join` node waits for all concurrent modules to complete
- No data dependencies between concurrent modules
- Applicable: When independent subtasks can be processed in parallel

### 24.3 Pattern 3: Conditional

```mermaid
Start --> Classify{Classification}
Classify -->|Type A| ModuleA
Classify -->|Type B| ModuleB
Classify -->|Other| ModuleDefault
```

- Conditional branches are annotated using the `|label|` syntax on Classify nodes
- The current Mermaid flowchart already supports this syntax; no new format is needed
- Applicable: Intent routing, input type dispatching

### 24.4 Pattern 4: Handoff

Applicable for cross-component control transfer in Pattern F Ecosystem:

```
handoff_context = {
    "source": "component_a_aigp",
    "target": "component_b_aigp",
    "intent": "process_health_data",
    "payload": { ... },
    "metadata": { "timestamp": "...", "trace_id": "..." }
}
```

Process:
1. The initiator packages the complete context as `handoff_context`
2. The receiver restores state from `handoff_context`
3. The receiver returns `handoff_result` upon completion
4. The initiator confirms the result or initiates a new handoff

---

## Part V: Quality & Compatibility

---

## 25. Version Compatibility

### 25.1 Protocol Version Compatibility Guarantees

| Version Range | Compatibility Guarantee |
|---------|---------|
| AIGP V1.x.y | Backward compatible within the same major version |
| AIGP V2.0.0+ | May introduce breaking changes, migration guide provided |

### 25.2 Program Version Specification

AIGP program versions follow semver:

| Version Change | Meaning | Example |
|---------|------|------|
| **major** (x.0.0) | Breaking change — input/output format changes | 1.0.0 → 2.0.0 |
| **minor** (x.y.0) | New feature — backward compatible | 1.0.0 → 1.1.0 |
| **patch** (x.y.z) | Bug fix/improvement — backward compatible | 1.1.0 → 1.1.1 |

### 25.3 Minimum Protocol Version

```yaml
# AIGP.md frontmatter
min_protocol_version: "AIGP V1.0.0"
```

The executor checks before loading a program: if the executor's supported protocol version < `min_protocol_version` → Reject loading + Prompt upgrade.

### 25.4 Version Changelog Format

It is recommended to use a structured format in the optional "Version History" section of AIGP.md:

```markdown
## Version History

### v1.2.0 (2026-03-01)
- **Added**: Monthly report trend analysis
- **Improved**: Query performance optimization

### v1.1.0 (2026-02-15)
- **Added**: Blood pressure recording feature
- **Fixed**: Date parsing boundary error
```

Change type labels: `Added` / `Improved` / `Fixed` / `Removed` / `Security`

---

## 26. Documentation Completeness Levels

### 26.1 Three-Tier Classification

| Level | Requirements | Applicable To |
|------|------|------|
| **Level 1** (Minimum) | AIGP.md required sections (Governance Declaration + Feature Overview + Usage) | All AIGP programs |
| **Level 2** (Recommended) | + Example Interactions + Applicable Conditions | Programs with `status=active` |
| **Level 3** (Complete) | + Error Handling + Version History + All optional fields | Programs published to Registry |

### 26.2 Checklist for Each Level

**Level 1 (Minimum)**:
```
[ ] AIGP.md exists
[ ] 12 required frontmatter fields are complete
[ ] Governance Declaration section exists
[ ] Feature Overview section exists
[ ] Usage section exists
[ ] Closing seal exists
```

**Level 2 (Recommended)**:
```
[ ] All Level 1 checks passed
[ ] Example Interactions section exists (1-3 scenarios)
[ ] Applicable Conditions section exists (applicable + not applicable)
[ ] quality optional fields are populated
[ ] status = active
```

**Level 3 (Complete)**:
```
[ ] All Level 2 checks passed
[ ] Error Handling section exists
[ ] Version History section exists (structured format)
[ ] trust_level is declared
[ ] permissions is declared (if trust_level >= T3)
[ ] runtime is declared
[ ] intent_examples is populated
[ ] governance_hash is computed
[ ] benchmark is populated
```

---

## Appendix A: PL24 Auto-Fix Protocol

Applicable: When AutoFixEngine generates fix proposals.

| Constraint | Description |
|------|------|
| **(a) SCOPE** | Fixes limited to 1-3 files, symbol changes ≤ 10, line changes ≤ 50 |
| **(b) CONFIDENCE** | Auto-apply when confidence ≥ 0.85, otherwise submit as suggestion requiring human approval |
| **(c) RATE LIMIT** | Maximum 1 auto-fix per object per day, to prevent infinite loops |
| **(d) AUDIT** | All auto-fixes logged to observability.lint_report |
| **(e) ROLLBACK** | All auto-fixes are rollbackable (git format) |
| **(f) NO LOGIC CHANGE** | Limited to format/style/missing declarations/version constraint fixes; algorithm or business logic changes are prohibited |

---

## Appendix B: PL25 License Declaration

Applicable: All AIGP programs, especially for aigp-store distribution.

### B.1 Core Rules

| Rule | Description |
|------|------|
| **(a) LICENSE FIELD** | AIGP.md must include a `license` field |
| **(b) SPDX VALIDITY** | Value must be a valid SPDX identifier (e.g., "Apache-2.0", "MIT") or "proprietary" |
| **(c) PROPRIETARY** | When license is "proprietary", `terms_url` or `contact` must be provided |
| **(d) STORE** | The license field is mandatory for distribution through aigp-store |

### B.2 Field Attributes

| Attribute | Value |
|------|-----|
| Field Name | `license` |
| Type | `string` |
| Required | Optional (local programs) / **Mandatory** (Store listing) |
| Default | `proprietary` (treated as all rights reserved when not declared) |
| Format Specification | SPDX standard identifiers (see https://spdx.org/licenses/) |

### B.3 Common SPDX Values Reference

| Value | Meaning |
|----|------|
| `MIT` | MIT License (most permissive) |
| `Apache-2.0` | Apache 2.0 (includes patent protection) |
| `GPL-3.0` | GPL v3 (strong copyleft) |
| `proprietary` | Proprietary / All rights reserved |
| `CC-BY-4.0` | Creative Commons Attribution (suitable for documentation-type programs) |

### B.4 Default Value Behavior

- The `license` field is **optional** (for local use)
- When not specified, the program defaults to `proprietary`
- Does not affect existing program operation (backward compatible)

### B.5 Additional Requirements for `proprietary`

When `license: proprietary`, at least one of the following fields must be provided:

```yaml
license: proprietary
terms_url: https://example.com/terms   # or
contact: author@example.com            # at least one is required
```

### B.6 aigp-store Store Integration

aigp-store registry entries read and display the `license` field directly from AIGP.md:

```json
{
  "program_id": "publisher.domain/program_name",
  "version": "1.0.0",
  "license": "MIT",
  "store_url": "https://aigp.store/programs/publisher.domain/program_name"
}
```

Listing checks:
- Missing `license` field → Store registration API returns error, listing rejected
- `license: proprietary` without `terms_url`/`contact` → Listing rejected

### B.7 Backward Compatibility Guarantees

| Scenario | Behavior |
|------|------|
| Existing programs without a `license` field | Run normally, default treated as `proprietary` |
| Local use without Store listing | Completely unaffected |
| Submitted to Store without `license` filled in | Store registration API returns error, listing rejected |

---

## Appendix C: Category M — Tool Directory Simulation Scenarios

Applicable: Pattern G programs.

| Scenario | Description |
|------|------|
| M1 | Normal MCP Server startup and tool invocation |
| M2 | MCP Server startup failure, degraded handling |
| M3 | Python dependency installation failure |
| M4 | MCP Server tool invocation timeout |
| M5 | governance_hash mismatch (Code Trust Gate interception) |
| M6 | ZIP SLIP attack (malicious paths in tool_dirs) |
| M7 | Network permission violation (undeclared import requests) |
| M8 | Dependency version not pinned (TS ^ prefix detection) |
| M9 | go.sum missing |
| M10 | Rust pre-compiled binary hash mismatch |
| M11 | shell-tools present but trust_level < T4 |
| M12 | Multi-language MCP Server partial startup failure |

---

Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev
