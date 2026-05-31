# Claude Code Setup — /mindmap skill

## Quick Start

After installing this skill, type `/mindmap <topic>` in any Claude Code session:

```
/mindmap AI infrastructure buildout
/mindmap GLP-1 / Ozempic drug ecosystem --output glp1.html
/mindmap Copper critical minerals
```

Claude will generate a self-contained HTML investment mindmap and save it to your working directory.

## Installation

```bash
# Clone the repo into your global skills directory
git clone https://github.com/parkpineventure/mindmap-skill ~/.claude/skills/mindmap-skill

# Or via the skills marketplace (when available)
/skill add parkpineventure/mindmap-skill
```

## How Claude Uses This Skill

When you type `/mindmap <topic>`, Claude will:

1. Load `skills/mindmap/SKILL.md` as the task specification
2. Research the topic using its training knowledge (and web search if available)
3. Generate a structured JSON dataset: real tickers, revenue, growth, signals, theses
4. Read `skills/mindmap/template.html` from the repository
5. Substitute the four template placeholders (`__TITLE__`, `__SUBTITLE__`, `__HEADER_BADGE__`, `__MINDMAP_DATA__`)
6. Write the output HTML to your working directory
7. Report the file path and a short summary

## Output

A single `.html` file, fully self-contained (D3.js loaded via CDN). Open it in any browser — no server required.

## Notes

- Claude uses its own knowledge to populate firm data. For the most current revenue/price data, enable web search or verify figures independently.
- The skill does not require an Anthropic API key — it runs directly inside your Claude Code session.
- For batch generation outside Claude Code, use the Python CLI (`generate.py`) which does require an API key.

## Updating

```bash
cd ~/.claude/skills/mindmap-skill
git pull
```
