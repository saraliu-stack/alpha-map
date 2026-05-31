# /mindmap — Market Intelligence Mindmap Generator

> Generates a self-contained interactive HTML investment mindmap for any sector, company, narrative, or macro theme. Output is a single portable file — no server required.

---

## Invocation

```
/mindmap <topic>
/mindmap <topic> --output <filename>
```

**Examples:**
```
/mindmap AI infrastructure buildout
/mindmap GLP-1 / Ozempic drug ecosystem
/mindmap Copper and critical minerals supply chain
/mindmap US defence tech post-Ukraine narrative
/mindmap India consumer internet boom
/mindmap Nuclear energy renaissance
/mindmap SpaceX Starlink ecosystem
```

---

## What This Skill Does

When invoked, the agent will:

1. **Research** the topic — identify upstream supply chain inputs (bottlenecks, raw materials, enabling tech) and downstream beneficiaries (end markets, platforms, applications)
2. **Generate** structured investment data: real tickers, revenue, growth rates, market caps, investment signals, theses, bull/bear cases, and a one-line role description for each firm
3. **Inject** the data into `template.html` (located alongside this SKILL.md)
4. **Write** the output as a self-contained HTML file
5. **Report** the output path so the user can open it in any browser

---

## Step-by-Step Execution

### Step 1 — Resolve output filename

If `--output` is provided, use that. Otherwise derive a slug:
- Lowercase the topic, replace non-alphanumeric with hyphens, trim to 60 chars
- Append `-mindmap.html`
- Example: `"AI infrastructure buildout"` → `ai-infrastructure-buildout-mindmap.html`

### Step 2 — Research the topic

Think through the full supply chain before generating any data:

**Upstream** (inputs, bottlenecks, enabling technology, raw materials):
- What raw materials or components does this theme depend on?
- Where are the manufacturing or supply chokepoints?
- Which companies control critical upstream inputs?
- What IP, regulation, or capacity constraints exist?

**Downstream** (end markets, beneficiaries, platforms, applications):
- Who benefits most as this narrative plays out?
- Which sectors or companies are the primary demand drivers?
- What adjacent markets are pulled along?

For each sector node, identify:
- 2–4 publicly traded companies (real tickers only)
- Revenue, YoY growth rate, approximate market cap
- An investment signal (see signal table below)
- A one-sentence role: what this company specifically does *in this sector for this narrative*
- 1–3 private companies or IPO candidates where relevant
- A 2–3 sentence investment thesis
- 2–3 bull points and 1–2 bear points

### Step 3 — Generate the DATA object

Produce a single JSON object following this schema **exactly**. All fields are required. Use `null` only where data is genuinely unavailable.

```json
{
  "title":       "Topic Name — Investment Guide",
  "subtitle":    "Key Stat · Key Stat · Upstream bottlenecks · Downstream beneficiaries",
  "headerBadge": "Primary Company/Index: $XB rev · X% margin · X% market share",

  "id": "root",
  "name": "Short Topic\nSubtitle",
  "type": "root",
  "risk": 0,
  "conviction": 0,
  "tam": "—",
  "supplyTension": "hub",
  "tickers": [],
  "desc": "2-sentence overview of the ecosystem and investment significance.",
  "publicFirms": [],
  "privateFirms": [
    { "name": "Key Private Co", "meta": "~$XB val · key role · stage" }
  ],
  "thesis": "3-4 sentence master investment thesis covering the macro narrative.",
  "bull": ["Bull point with specific data", "Bull point 2", "Bull point 3"],
  "bear": ["Bear risk 1", "Bear risk 2"],
  "children": [

    {
      "id":           "unique-kebab-id",
      "name":         "Sector Name\nSubsector or Focus",
      "type":         "upstream",
      "risk":         3,
      "conviction":   4,
      "tam":          "$XXB by 20XX",
      "supplyTension": "high",
      "tickers":      ["TICK1", "TICK2"],
      "desc":         "1-2 sentence description of this sector's role and constraint status.",
      "publicFirms": [
        {
          "ticker": "TICK",
          "name":   "Company Name (specific division or product)",
          "rev":    "$XB",
          "growth": "+X%",
          "cap":    "$XB",
          "signal": "sig-buy",
          "role":   "One precise sentence: what this company specifically does in THIS sector for this narrative"
        }
      ],
      "privateFirms": [
        { "name": "Private Co", "meta": "$XB val · stage · key note" }
      ],
      "thesis": "2-3 sentence investment thesis for this sector node.",
      "bull":   ["Specific bull point with data", "Another bull point"],
      "bear":   ["Specific bear risk"],
      "children": []
    }

  ]
}
```

### Signal values (exact strings only)

| Signal | Meaning | When to use |
|--------|---------|-------------|
| `sig-sb` | STRONG BUY | Highest conviction; structural moat + catalyst |
| `sig-buy` | BUY | Clear upside; well-positioned for narrative |
| `sig-hold` | HOLD | Exposure to theme but not the cleanest play |
| `sig-cau` | CAUTIOUS | Declining or disrupted by the narrative |
| `sig-avd` | AVOID | Existential threat from this narrative |
| `sig-spec` | SPECULATIVE | Pre-revenue, binary outcome, high risk/reward |

### supplyTension values (exact strings only)

| Value | Meaning |
|-------|---------|
| `critical` | Severe bottleneck; <6 months of buffer; single-source risk |
| `high` | Tight supply; 12–18 month lag to add capacity |
| `medium` | Manageable constraints; competitive but not acute |
| `demand-led` | Demand is the binding constraint, not supply |
| `hub` | Root node only |

### risk and conviction scale

- `risk`: 0 (root) to 5 (most critical bottleneck / highest failure risk)
- `conviction`: 0 (root/non-investable) to 5 (highest investment conviction)

### Content rules

1. **Real tickers only** — no invented symbols. If a sector has no good public pure-plays, say so in `thesis` and use fewer `publicFirms`.
2. **Revenue and cap** — use real figures (fiscal year most recently reported). Approximate is fine: `$4.2B`, `~$20B`, `AUD$700M`. Avoid made-up precision.
3. **growth** — always prefix: `+12%` or `-8% (cycle)` or `+X% est.` Use `N/A` only for pre-revenue.
4. **role** — must explain *this company's specific function within this sector node*, not a generic company description. Bad: "NVIDIA makes GPUs." Good: "NVIDIA H100/B200 GPUs are the primary training and inference compute for all frontier AI models — ~90% data-center AI workload share."
5. **name** — use `\n` for a line break in the node label. Keep each line under ~18 chars.
6. **Include 3–6 upstream nodes** and **3–6 downstream nodes** as direct children of root.
7. **Children depth**: Add 1–3 sub-nodes to any top-level node where a meaningful sub-sector exists. Max depth: 3 levels total.
8. **privateFirms** — include at least 1–2 per node (IPO candidates, private leaders, incumbents being disrupted).

### Step 4 — Read the template

Read the file `skills/mindmap/template.html` from this repository. It contains these four placeholder strings:

```
__TITLE__
__SUBTITLE__
__HEADER_BADGE__
__MINDMAP_DATA__
```

### Step 5 — Inject and write

- Replace `__TITLE__` with `data.title`
- Replace `__SUBTITLE__` with `data.subtitle`
- Replace `__HEADER_BADGE__` with `data.headerBadge`
- Replace `__MINDMAP_DATA__` with the full JSON object (without the `title`, `subtitle`, `headerBadge` wrapper — just the root node starting with `"id": "root"`)
- Also replace the footer date string `May 2026 — Generated by Market Mindmap` with today's month/year + `— Generated by /mindmap`
- Write the result to the output filename resolved in Step 1

### Step 6 — Report

Tell the user:
- The output file path (absolute if possible)
- How many top-level sector nodes were generated (upstream + downstream count)
- Any tickers or sectors where data was uncertain (flag for review)
- One sentence summary of the master thesis

---

## Output Format Rules

1. **Write the file first**, then report — do not output the HTML to the chat.
2. Keep the in-chat report short: filename, node count, thesis summary, any caveats.
3. Do not reproduce the full JSON in the chat.
4. If you cannot write a file (e.g. agent has no filesystem access), output the full HTML as a fenced code block with language `html` so the user can save it manually.

---

## What This Skill Does NOT Do

- Does not provide personalised financial advice
- Does not guarantee accuracy of revenue or price data — always verify before trading
- Does not access real-time market data or live APIs
- Does not generate fake ticker symbols

---

## Compatibility

This skill is designed to work on any agent that can:
- Read files from the repository (to load `template.html`)
- Write files to the local filesystem (to save the output)
- Make in-context reasoning calls (to generate the investment data)

Tested on: Claude Code, Cursor, GitHub Copilot (agent mode), Windsurf, OpenClaw

---

## Version

`/mindmap v1.0.0` · Built by ParkPine Venture · MIT License
