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

# Doc paths (AI reads on demand, not injected into prompt)
_SCHEDULE_GUIDE = Path(soulbot.__file__).parent / "docs" / "schedule_guide.md"
_AISOP_TEMPLATE = Path(soulbot.__file__).parent / "docs" / "STANDARD.aisop.json"
_MCP_GUIDE = Path(soulbot.__file__).parent / "docs" / "mcp_guide.md"


# ---------------------------------------------------------------------------
# Dynamic instruction: cached main + live file list
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = (
    "You are the AISOP Runtime. "
    "Strictly follow the loaded AISOP file and RUN its mermaid flow. "
    "Always mirror User's exact language and script variant. "
    "IMPORTANT: Before responding, verify you followed the mermaid flow exactly. "
    "If not, regenerate."
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

    # Discover *_aigp package directories
    if _AIGP_DIR.is_dir():
        pkg_names = sorted(
            d.name for d in _AIGP_DIR.iterdir()
            if d.is_dir()
            and d.name.endswith("_aigp")
            and (d / "main.aisop.json").is_file()
        )
        if pkg_names:
            parts.append(f"[Available AIGP packages]\n{', '.join(pkg_names)}")
            parts.append(
                "Each AIGP package is a directory containing main.aisop.json as entry point. "
                "Read [AIGP Directory]/{package_name}/main.aisop.json to load and execute."
            )

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
