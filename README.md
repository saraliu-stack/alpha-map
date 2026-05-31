# 📡 /mindmap — Market Intelligence Mindmap Skill

> An AI agent skill that generates interactive, investment-grade supply chain mindmaps for any sector, narrative, or macro theme.

**[🛰️ Live Demo — Space Economy](https://saraliu-stack.github.io/alpha-map/examples/space-economy.html)**  &nbsp;|&nbsp;  **[🌐 Homepage](https://saraliu-stack.github.io/alpha-map/)**

---

## Usage

```
/mindmap <topic>
/mindmap <topic> --output <filename>
```

```
/mindmap AI infrastructure buildout
/mindmap GLP-1 / Ozempic drug ecosystem
/mindmap Copper and critical minerals supply chain
/mindmap US defence tech post-Ukraine narrative
/mindmap India consumer internet boom
/mindmap Nuclear energy renaissance
/mindmap SpaceX Starlink ecosystem
```

The skill writes a single self-contained HTML file to your working directory. Open it in any browser — no server needed.

---

## Install

### Claude Code
```bash
/skill add saraliu-stack/alpha-map
```

### Agent Skills CLI
```bash
npx skills add saraliu-stack/alpha-map -g
```

### Manual (any agent)
```bash
git clone https://github.com/saraliu-stack/alpha-map
```
Then point your agent at `skills/mindmap/SKILL.md`.

### Python CLI (optional, for scripting/batch use)
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...     # Mac/Linux
$env:ANTHROPIC_API_KEY = "sk-ant-..."  # Windows PowerShell

python generate.py "AI infrastructure buildout"
python generate.py "GLP-1 ecosystem" --output glp1.html
```

---

## What You Get

Each generated mindmap is a **fully interactive single-page app**:

| Feature | Description |
|---------|-------------|
| 📡 **Radial supply chain map** | D3.js interactive tree — zoom, pan, click to expand/collapse sectors |
| ⬆⬇ **Upstream & downstream** | Supply bottlenecks in red/amber, beneficiaries in green — color-coded by tension |
| 📋 **Investment Brief sidebar** | Hover any bubble → public tickers, revenue, growth, market cap, investment signal |
| 🏷️ **Sector role one-liners** | Every ticker: one sentence on exactly what they do *in this sector* |
| ⤢ **Fullscreen overlay** | Expand any brief to a full-screen card with bull/bear thesis, private IPO watch |
| 🔍 **Filter controls** | Filter: upstream only · downstream only · critical bottlenecks · 5★ conviction |
| 🎯 **Investment signals** | STRONG BUY → BUY → HOLD → CAUTIOUS → AVOID → SPECULATIVE |
| ⭐ **Conviction stars** | 1–5 star rating per sector — research quality indicator |

---

## How It Works

The skill is **prompt-first** — no external APIs, no Python required to run inside an agent.

```
/mindmap "GLP-1 drug ecosystem"
          │
          ▼
    Agent reads SKILL.md
          │
          ▼
    Research: upstream inputs (API manufacturing, cold chain, devices)
              downstream beneficiaries (cardiac care, food, fitness, retail)
          │
          ▼
    Generate JSON: real tickers, revenue, growth, signals, theses, roles
          │
          ▼
    Read template.html → substitute placeholders
          │
          ▼
    Write: glp1-drug-ecosystem-mindmap.html  ✓
```

The agent uses its own knowledge (and web search if available) to populate real firm data. No API keys needed beyond your agent.

---

## Example Output

**[🛰️ Space Economy / Starlink](https://saraliu-stack.github.io/alpha-map/examples/space-economy.html)**

Includes: Rad-Hard ICs (critical bottleneck), Rare Earths (critical), Launch & Propulsion, Satellite Manufacturing, Autonomous Vehicles, Defense & National Security, IoT & Smart Infrastructure, Earth Observation, and more — with 50+ public firms, revenue/growth data, and full investment theses.

---

## Skill File Structure

```
alpha-map/
├── skills/
│   └── mindmap/
│       ├── SKILL.md          ← Runtime spec (source of truth for all agents)
│       └── template.html     ← D3.js visualization template
├── examples/
│   └── space-economy.html    ← Live demo
├── generate.py               ← Optional Python CLI (batch/scripting)
├── requirements.txt          ← pip: anthropic
├── AGENTS.md                 ← Cross-agent compatibility guide
├── CLAUDE.md                 ← Claude Code setup notes
├── index.html                ← GitHub Pages landing
└── .github/
    └── workflows/
        └── pages.yml         ← Auto-deploy to GitHub Pages
```

---

## Agent Compatibility

| Platform | `/mindmap` command | File output | Notes |
|----------|--------------------|-------------|-------|
| **Claude Code** | ✅ | ✅ | Fully supported |
| **Cursor** (agent mode) | ✅ | ✅ | Fully supported |
| **Windsurf** | ✅ | ✅ | Fully supported |
| **GitHub Copilot** (agent) | ✅ | ✅ | Fully supported |
| **OpenClaw** | ✅ | ✅ | Fully supported |
| **Gemini CLI** | ✅ | ✅ | Supported |
| **claude.ai web** | ⚠️ | ❌ | Outputs HTML as code block to copy |

---

## Example Topics

| Topic | What the mindmap covers |
|-------|------------------------|
| `"NVIDIA AI chip supply chain"` | CoWoS packaging → HBM → power → hyperscaler capex → inference apps |
| `"EV battery supply chain"` | Lithium → cathode → cell → pack → OEM → charging infrastructure |
| `"Biotech gene therapy platforms"` | Viral vectors → CDMOs → clinical trials → payer access → patients |
| `"Southeast Asia digital economy"` | Fintech → logistics → super-apps → underlying infra → advertisers |
| `"Water infrastructure crisis"` | Pipe replacement → desalination → smart metering → utilities → EPCs |
| `"Quantum computing ecosystem"` | Cryogenics → qubit supply → error correction → cloud access → verticals |

---

## Disclaimer

Data is AI-generated for research and educational purposes only. Not financial advice. Always verify figures independently before making investment decisions. Revenue and market cap data reflects the agent's training knowledge and may not be current.

---

## License

MIT — free to use, fork, and modify. Pull requests welcome.

Built by **ParkPine Venture** · Powered by **Anthropic Claude** · Visualized with **D3.js v7**
