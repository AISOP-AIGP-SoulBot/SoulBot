---
# AIGP Governance Contract
# Governance Fields (6 required)
protocol: "AIGP V1.0.0"
authority: aigp.dev
seed: aisop.dev
executor: soulbot.dev
axiom_0: Human_Sovereignty_and_Benefit
governance_mode: NORMAL

# Project Fields (6 required)
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

# Optional Fields
governance_hash: 0aaa80977242a967fede7c33dd64b4b3b477d1098bceed2684cbeb8a9480c673
quality:
  weighted_score: 5.000
  grade: S
  last_pipeline: "Quality Intelligence Enhancement: YellowFixProposalGenerator, D8-LICENSE semantic check, D4-RANGE cross-reference staleness detection, domain-specific quality research, competitive landscape analysis. PostSimulateGate yellow_fix_proposals consumption with 4 user action options. ValidateStep LICENSE COMPLIANCE CHECK with PL25 enforcement. range_reference_consistency rule in AIGP_Standard.core. competitive_insights data contract in research_context."
tags: [aigp, creator, pipeline, governance, meta]
author: AIGP Protocol Organization
license: Apache-2.0
copyright: "Copyright 2026 AISOP.dev | AIGP.dev | SoulBot.dev"

# Security and Runtime Optional Fields
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

# Engineering Optional Fields
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
  - "Create a personal expense tracker AIGP program"
  - "Evolve health_tracker from v1.1 to v1.2"
  - "Modify the search module of recipe_finder"
  - "Validate the code quality of expense_tracker"
  - "Simulate the execution paths of travel_planner"
  - "Search for any health-related AIGP programs"
  - "Deprecate old_tracker program"
  - "Export recipe_finder as SKILL.md"
  - "Import a SKILL.md file as an AIGP program"
  - "Map health_tracker tools to MCP protocol"
  - "Search remote registry for health-related AIGP programs"
  - "Package health_tracker as a .aigp file"
  - "Unpack and verify recipe_finder_v1.0.0.aigp"
  - "Add a Dashboard UI component to health_tracker"
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

## Governance Declaration

AIGP Creator is the reference implementation and bootstrapping tool for the AIGP protocol.
This program follows the AIGP V1.0.0 protocol, with Axiom 0 (Human Sovereignty and Benefit)
as its immutable axiom, ensuring all outputs align with human sovereignty and benefit through
the three-domain governance chain (aisop.dev -> aigp.dev -> soulbot.dev).

AIGP Creator is itself an AIGP program (bootstrapping property) — it creates AIGP programs
while also following all AIGP rules itself.

## Feature Overview

AIGP Creator manages the complete lifecycle of AIGP programs through a 14-stage pipeline:

| Intent | Description | Pipeline |
|--------|-------------|----------|
| **Create** | Create a new AIGP program | Research -> Evolve -> Generate -> Modify -> QualityGate -> Validate -> Simulate -> PostSimulateGate -> Observability -> Review |
| **Evolve** | Evolve an existing AIGP program | Same as Create (with incremental diff analysis) |
| **Modify** | Modify a specific module | Research(quality) -> Modify -> Generate -> Validate -> [Simulate] -> [PostSimulateGate] -> Review |
| **Validate** | Validate code quality | ThreeDimTest 33+ checks (C1-C7, I1-I13, D1-D10) |
| **Simulate** | Simulate execution paths | Path tracing + scenario coverage (Categories A-M) |
| **Compare** | Compare two versions | Side-by-side diff display |
| **Discover** | Search existing programs | Workspace scan + federated registry query + semantic matching + related recommendations |
| **Deprecate** | Deprecate/archive a program | State transition + migration guide generation |
| **Export** | Export as SKILL.md | AIGP->SKILL.md field mapping + governance metadata preservation |
| **Import** | Import from SKILL.md | SKILL.md->AIGP skeleton generation + governance defaults |
| **Explain** | Explain AIGP concepts | Inline knowledge response |
| **Package** | Pack/unpack a program | advisor package sub-graph (pack -> .aigp / unpack -> verify) |

### Module Architecture (Pattern D+G)

- **main.aisop.json** — Top-level orchestrator (27 nodes, fractal_exempt)
- **generate.aisop.json** — Generator (10 nodes)
- **research.aisop.json** — Shared research module (15 nodes, fractal_exempt, 3-mode reuse)
- **modify.aisop.json** — Modifier (9 nodes)
- **review.aisop.json** — Reviewer (11 nodes, +AutoFixEngine)
- **simulate.aisop.json** — Simulator (10 nodes, +YellowRemediationGuide, +YellowFixProposalGenerator)
- **observability.aisop.json** — Telemetry analysis (9 nodes, Token/Error/Dimension/RootCause/QRG analysis)
- **advisor.aisop.json** — Advanced advisor (52 nodes, fractal_exempt, 8 sub-graphs: main router + 7 mutually exclusive sub-graphs orchestrate/memory/protocol/skill_export/skill_import/mcp_adapter/package)
- **AIGP_Standard.core.aisop.json** — Core quality standard (C1-C7, I1-I7, I12-I13, D1-D7, PL1-PL12, PL19-PL21, MF1-MF9, MF15-MF16 + extension_registry + tool_annotations + json_schema + interop.mcp_tool_mapping + tool_dirs_spec + pattern_thresholds(G) + mcp_tool_mapping/registry/capability_negotiation/sampling_request/aigp_package/ui_output contracts)
- **AIGP_Standard.security.aisop.json** — Security extension (I8-I11, I13 Embedded Code Safety, D8-D10, AT1-AT6 threat taxonomy, Code Trust Gate with ZIP SLIP extension)
- **AIGP_Standard.ecosystem.aisop.json** — Ecosystem extension (MF10-MF14, MF16, K1-K5, PL16-PL17 dynamic TTL, PL22 Registry Integration, packaging_specification + tool_dirs_packaging, registry_endpoint_extension, tool_dirs extension, ui_rendering_rules, yellow_persistence_tracking, Categories F-M)
- **AIGP_Standard.performance.aisop.json** — Performance extension (PL13-PL15, PL18, PL23 Sampling Protocol, PL24 Auto-Fix Protocol, QRG1-QRG5, E.injection)

## Usage

### Entry File

`main.aisop.json` — AI Agent loads this file to start AIGP Creator.

### Tool Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| file_system | Yes | Read/write AISOP files |
| google_search | No | Search best practices during research stages |
| web_browser | No | Deep web research |

### Prerequisites

- AIGP_Standard.core.aisop.json (and extension files) and AIGP_Protocol.md accessible in target directory
- AI Agent supports the file_system tool

## Example Interactions

**Scenario 1: Create a New Program**
- User: "Create a personal expense tracker AIGP program"
- Agent: Executes full Pipeline -> generates expense_tracker_aigp/ directory with AIGP.md + main + modules

**Scenario 2: Evolve an Existing Program**
- User: "Evolve health_tracker from v1.1 to v1.2 with monthly report functionality"
- Agent: Analyzes existing structure -> proposes LEVEL_A/B changes -> user confirms -> generates new version

**Scenario 3: Validate Quality**
- User: "Validate the code quality of recipe_finder"
- Agent: Runs ThreeDimTest -> outputs three-dimensional scores + traffic light classification

## Applicability

**Applicable**: Creating, evolving, modifying, validating, simulating, discovering, and deprecating AIGP programs; SKILL.md bidirectional conversion; MCP tool mapping; federated registry discovery (with MCP/A2A endpoint discovery); AIGP packaging/unpackaging (with tool_dirs directory and Code Trust Gate); UI component declaration generation; Pattern G embedded tool directory (tool_dirs) validation and auto-generation; Pattern E/F->G migration guidance; auto-fix proposal generation and application; YELLOW persistence tracking and remediation guide; automated quality verification (lint_report)
**Not applicable**: Direct execution of AIGP programs (that is the SoulBot executor's responsibility); non-AISOP format projects

---

Align: Human Sovereignty and Benefit. Version: AIGP V1.0.0. www.aigp.dev
