# 📡 Market Intelligence Mindmap Generator

Generate interactive, investment-grade supply chain mindmaps for **any sector, company, market narrative, or macro theme** — powered by Claude AI.

**[🛰️ Live Demo — Space Economy](https://parkpineventure.github.io/market-mindmap/examples/space-economy.html)**  
**[🌐 Generator Homepage](https://parkpineventure.github.io/market-mindmap/)**

---

## What It Does

Point the generator at any investment topic and get a fully interactive HTML site with:

| Feature | Description |
|---------|-------------|
| 📡 **Radial supply chain mindmap** | D3.js interactive tree — zoom, pan, expand/collapse sectors |
| 📋 **Investment Brief sidebar** | Click any bubble → public tickers, revenue, growth, market cap, signal |
| ⤢ **Fullscreen overlay** | Expand any brief to a full-screen card with bull/bear thesis |
| 🔍 **Filter controls** | Filter by upstream, downstream, critical bottlenecks, or 5★ conviction |
| 🏷️ **Sector role labels** | Every ticker: one sentence on what they specifically do *in this sector* |
| 🤖 **AI-powered research** | Real tickers, revenue figures, supply tension ratings, investment theses |

---

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/parkpineventure/market-mindmap
cd market-mindmap
pip install -r requirements.txt
```

### 2. Set Your Anthropic API Key

```powershell
# Windows PowerShell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

```bash
# Mac / Linux
export ANTHROPIC_API_KEY="sk-ant-..."
```

Get a key at [console.anthropic.com](https://console.anthropic.com).

### 3. Generate Any Topic

```bash
python generate.py "AI Infrastructure buildout"
python generate.py "GLP-1 / Ozempic drug ecosystem" --output glp1.html
python generate.py "Copper & critical minerals supply chain"
python generate.py "US defence tech post-Ukraine narrative"
python generate.py "India consumer internet boom"
python generate.py "Nuclear energy renaissance"
```

The script creates a single self-contained HTML file. Open it in any browser — no server needed.

---

## Output Structure

Each generated mindmap includes:

**Upstream nodes** (supply chain inputs, bottlenecks, enabling tech)
- Raw materials, components, IP, manufacturing capacity constraints
- Color-coded by supply tension: 🔴 Critical → 🟡 High → 🟢 Demand-led

**Downstream nodes** (end markets, beneficiaries, platforms)
- Application sectors, companies that benefit from the theme
- Revenue data, growth rates, market cap, investment signal

**Per node Investment Brief**:
- Public firms table with Ticker · Company · Role · Revenue · Growth · Cap · Signal
- Private / IPO watch list
- Investment thesis
- Bull vs Bear case

---

## Options

```
python generate.py --help

positional arguments:
  topic                 The sector, narrative, or theme to analyse

options:
  --output, -o FILE     Output HTML filename (default: auto-named from topic)
  --model, -m MODEL     Claude model: claude-opus-4-5 (default, best quality)
                                      claude-sonnet-4-5 (faster, cheaper)
  --template, -t FILE   Custom template.html path
```

---

## Examples

| Command | What you get |
|---------|-------------|
| `python generate.py "NVIDIA AI chip supply chain"` | Full GPU ecosystem from CoWoS packaging to hyperscaler capex |
| `python generate.py "EV battery supply chain"` | Lithium → cathode → cell → pack → OEM → charging infrastructure |
| `python generate.py "Biotech / gene therapy platforms"` | CRISPR supply chain from viral vectors to CDMOs to payer access |
| `python generate.py "Southeast Asia digital economy"` | Grab/Sea/GoTo ecosystem + fintech + logistics + underlying infra |
| `python generate.py "Water infrastructure crisis"` | Pipe replacement + desalination + smart metering + utilities |

---

## File Structure

```
market-mindmap/
├── generate.py          # Generator script (run this)
├── template.html        # D3.js mindmap template
├── requirements.txt     # pip: anthropic
├── index.html           # GitHub Pages landing page
├── examples/
│   └── space-economy.html   # Live demo — Space Economy / Starlink
└── .github/
    └── workflows/
        └── pages.yml    # Auto-deploy to GitHub Pages on push
```

---

## How It Works

1. **You provide** a topic string (any sector, narrative, macro theme)
2. **Claude researches** the supply chain — upstream inputs, downstream beneficiaries, bottlenecks
3. **Claude generates** structured JSON: real tickers, revenue, growth, signals, theses
4. **The template** injects the JSON into a D3.js radial tree visualization
5. **Output** is a single portable HTML file, fully interactive, no server required

The prompt instructs Claude to use real ticker symbols, current revenue figures, and write specific investment theses — not generic descriptions.

---

## Disclaimer

Data is AI-generated for research and educational purposes only. Not financial advice. Always verify figures independently before making investment decisions.

---

## Built With

- [Anthropic Claude](https://www.anthropic.com) — AI research and data generation
- [D3.js v7](https://d3js.org) — Interactive data visualisation
- ParkPine Venture — Investment research

---

*Pull requests welcome. Open an issue to request example mindmaps.*
