# /mindmap — Agent Compatibility

This skill generates interactive investment-grade supply chain mindmaps for any sector, narrative, or macro theme. It is compatible with any AI agent that can read files and write output to the filesystem.

## Invocation

```
/mindmap <topic>
/mindmap <topic> --output <filename.html>
```

## Skill Location

The runtime spec (source of truth) lives at:

```
skills/mindmap/SKILL.md
```

The D3.js HTML template lives at:

```
skills/mindmap/template.html
```

## Installation by Platform

### Claude Code (recommended)
```bash
/skill add parkpineventure/mindmap-skill
```
Or manually clone and register:
```bash
git clone https://github.com/parkpineventure/mindmap-skill
cd mindmap-skill
npx skills add . -g
```

### Cursor / Windsurf / Copilot Agent Mode
Add this repository as a context source. The agent will discover `SKILL.md` automatically when you type `/mindmap`.

### OpenClaw
```bash
clawhub install mindmap-skill
```

### Manual (any agent)
1. Clone this repository
2. Point your agent at `skills/mindmap/SKILL.md` as a system prompt or tool instruction
3. Ensure the agent has read access to `skills/mindmap/template.html` and write access to your working directory

## How It Works

The skill is **prompt-first** — it requires no Python, no API keys beyond your agent's own model access, and no external dependencies. The agent:

1. Reads `SKILL.md` to understand the task
2. Researches the requested topic using its own knowledge and any connected web tools
3. Generates a structured JSON investment brief
4. Reads `template.html` and substitutes placeholders
5. Writes a self-contained HTML file the user can open in any browser

## Optional: Python CLI

For batch generation or scripting, a Python CLI is also available:

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python generate.py "AI infrastructure buildout"
```

This calls the Anthropic API directly and produces the same HTML output.

## Security

- Never commit API keys or auth tokens
- The skill does not transmit user data to any external service
- All processing happens locally within the agent session

## File Structure

```
mindmap-skill/
├── skills/
│   └── mindmap/
│       ├── SKILL.md          # Runtime spec (source of truth)
│       └── template.html     # D3.js visualization template
├── examples/
│   └── space-economy.html    # Live demo — Space Economy / Starlink
├── generate.py               # Optional Python CLI
├── requirements.txt          # pip: anthropic
├── AGENTS.md                 # This file
├── CLAUDE.md                 # Claude Code setup
├── README.md                 # Full documentation
├── index.html                # GitHub Pages landing
└── .github/
    └── workflows/
        └── pages.yml         # Auto-deploy GitHub Pages
```

## Compatibility Matrix

| Platform | Slash Command | File Write | Status |
|----------|--------------|------------|--------|
| Claude Code | ✅ | ✅ | Fully supported |
| Cursor (agent) | ✅ | ✅ | Fully supported |
| Windsurf | ✅ | ✅ | Fully supported |
| GitHub Copilot (agent) | ✅ | ✅ | Fully supported |
| OpenClaw | ✅ | ✅ | Fully supported |
| claude.ai web | ⚠️ manual | ❌ | Outputs HTML in chat |
| Gemini CLI | ✅ | ✅ | Supported |

> On platforms without filesystem write access, the skill outputs the complete HTML as a fenced code block for manual saving.
