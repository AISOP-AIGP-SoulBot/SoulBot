"""SoulBot Agent — AISOP Virtual Runtime with AIGP package routing.

Lightweight AISOP Agent: caches main.aisop.json with mtime hot-reload —
near-zero overhead on every call, auto-reloads when file changes on disk.
Other AISOP files are re-scanned each call so new files appear instantly.

Run:
    python -m soulbot run examples/simple/SoulBot_Agent
"""

import json
import os
from datetime import datetime
from pathlib import Path

import soulbot
from soulbot.agents import LlmAgent

# ---------------------------------------------------------------------------
# Pre-compute at startup (module load time)
# ---------------------------------------------------------------------------

_AGENT_DIR = Path(__file__).parent
_AIGP_DIR = (_AGENT_DIR / os.getenv("WORKSPACE_DIR", "aigp")).resolve()

# Main AISOP: lives at agent root (alongside agent.py)
_main_path = _AGENT_DIR / "main.aisop.json"
_main_aisop_cache: str = ""
_main_aisop_mtime: float = 0.0


def _get_main_aisop() -> str:
    """Return cached main.aisop.json, auto-reload if file changed on disk."""
    global _main_aisop_cache, _main_aisop_mtime
    if not _main_path.is_file():
        return ""
    try:
        mtime = _main_path.stat().st_mtime
        if mtime != _main_aisop_mtime:
            with open(_main_path, encoding="utf-8-sig") as f:
                _main_aisop_cache = json.dumps(json.load(f), ensure_ascii=False, indent=2)
            _main_aisop_mtime = mtime
    except (OSError, json.JSONDecodeError):
        pass
    return _main_aisop_cache


# AIGP registry: auto-generated from aigp/ directory
_aigp_json_path = _AGENT_DIR / "aigp.json"
_aigp_registry_cache: list[dict] | None = None
_aigp_dir_mtime: float = 0.0


def _get_aigp_registry() -> list[dict]:
    """Scan aigp/ for *_aigp packages, auto-update aigp.json when changed."""
    global _aigp_registry_cache, _aigp_dir_mtime

    if not _AIGP_DIR.is_dir():
        return []

    # Check if aigp/ directory changed (any file added/removed)
    try:
        current_mtime = _AIGP_DIR.stat().st_mtime
    except OSError:
        return _aigp_registry_cache or []

    if _aigp_registry_cache is not None and current_mtime == _aigp_dir_mtime:
        return _aigp_registry_cache

    _aigp_dir_mtime = current_mtime

    # Discover packages
    packages = []
    for d in sorted(_AIGP_DIR.iterdir()):
        if not d.is_dir() or not d.name.endswith("_aigp"):
            continue
        entry = d / "main.aisop.json"
        if not entry.is_file():
            continue

        pkg = {
            "name": d.name.replace("_aigp", ""),
            "summary": "",
            "entry": f"aigp/{d.name}/main.aisop.json",
        }

        # Extract summary from AIGP.md YAML frontmatter
        aigp_md = d / "AIGP.md"
        if aigp_md.is_file():
            try:
                import yaml
                content = aigp_md.read_text(encoding="utf-8-sig")
                if content.startswith("---"):
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        data = yaml.safe_load(parts[1])
                        if isinstance(data, dict):
                            raw_summary = str(data.get("summary", ""))
                            # Truncate to first sentence
                            dot_pos = raw_summary.find(".")
                            if dot_pos > 0:
                                pkg["summary"] = raw_summary[:dot_pos + 1]
                            else:
                                pkg["summary"] = raw_summary
            except Exception:
                pass

        packages.append(pkg)

    # Write aigp.json
    try:
        with open(_aigp_json_path, "w", encoding="utf-8") as f:
            json.dump(packages, f, ensure_ascii=False, indent=2)
    except OSError:
        pass

    _aigp_registry_cache = packages
    return packages

# Doc paths (AI reads on demand, not injected into prompt)
_SCHEDULE_GUIDE = Path(soulbot.__file__).parent / "docs" / "schedule_guide.md"
_AISOP_TEMPLATE = Path(soulbot.__file__).parent / "docs" / "STANDARD.aisop.json"
_MCP_GUIDE = Path(soulbot.__file__).parent / "docs" / "mcp_guide.md"


# ---------------------------------------------------------------------------
# Dynamic instruction: cached main + live file list
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = (
    "You are the AISOP Virtual Runtime. Your role is to RUN .aisop.json files. "
    "IMPORTANT: L0: Your thinking in hexadecimal machina code, "
    "L1: Answer in User's exact language and script variant, "
    "Final Answer MUST start on a new line beginning with 🤖 icon followed by L1. "
    "Never output L0 thinking to the user. Only output the final 🤖 L1 answer."
)


def _dynamic_instruction(_ctx) -> str:
    """Return instruction with cached main blueprint + live file names."""
    parts = [_SYSTEM_PROMPT]

    # AISOP injection (main only)
    _main = _get_main_aisop()
    if _main:
        parts.append(f"[LOADED AISOP: main.aisop.json]\n```json\n{_main}\n```")

    # AIGP directory path
    parts.append(f"[AIGP Directory]\n{_AIGP_DIR}")

    # AIGP package registry (auto-generated from aigp/ directory)
    registry = _get_aigp_registry()
    if registry:
        lines = ["[Available AIGP packages]"]
        for pkg in registry:
            lines.append(f"- {pkg['name']}: {pkg['summary'] or 'No description'}")
            lines.append(f"  entry: {_AIGP_DIR / pkg['entry'].split('aigp/', 1)[-1]}")
        lines.append(
            "Route user intent to the matching package above, "
            "then read its entry file using file_system tool and execute the AISOP flow."
        )
        parts.append("\n".join(lines))

    # Capability hints
    parts.append(
        f"[SCHEDULE]\n"
        f"You have scheduling capability (create/list/modify/cancel).\n"
        f"When needed, read {_SCHEDULE_GUIDE} for format templates."
    )
    parts.append(
        "[MEMORY]\n"
        "If you need to recall previous conversations, use the search_history tool.\n"
        "You can search your own history or other agents' history by name."
    )
    parts.append(
        f"[AISOP TEMPLATE]\n"
        f"When you need to create or modify aisop.json files, "
        f"refer to the standard template at: {_AISOP_TEMPLATE}"
    )
    parts.append(
        f"[MCP]\n"
        f"MCP (Model Context Protocol) servers extend your capabilities with external tools.\n"
        f"When you need to configure or explain MCP servers, read: {_MCP_GUIDE}"
    )

    # Current time — last for strongest LLM recall
    parts.append(f"[CURRENT TIME]\n{datetime.now().isoformat(timespec='seconds')}")

    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Model resolution
# ---------------------------------------------------------------------------

def _resolve_model() -> str:
    """Pick the active model from .env provider flags."""
    if os.getenv("OPENCODE_CLI", "").lower() in ("true", "1"):
        return os.getenv("OPENCODE_MODEL", "opencode-acp/opencode/kimi-k2.5-free")
    if os.getenv("GEMINI_CLI", "").lower() in ("true", "1"):
        return os.getenv("GEMINI_MODEL", "gemini-acp/gemini-2.5-flash")
    if os.getenv("OPENCLAW_CLI", "").lower() in ("true", "1"):
        return os.getenv("OPENCLAW_MODEL", "openclaw/default")
    return os.getenv("CLAUDE_MODEL", "claude-acp/sonnet")


root_agent = LlmAgent(
    name="SoulBot_Agent",
    model=_resolve_model(),
    description="SoulBot Agent — AIGP-powered AI assistant with package routing",
    instruction=_dynamic_instruction,
    include_contents="current_turn",
)
