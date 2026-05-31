#!/usr/bin/env python3
"""
Market Intelligence Mindmap Generator
======================================
Generates an interactive D3.js supply-chain & investment mindmap
for any sector, company, market narrative, or macro theme.

Usage:
  python generate.py "AI Infrastructure buildout"
  python generate.py "EV battery supply chain" --output ev-batteries.html
  python generate.py "Ozempic / GLP-1 drug ecosystem" --output glp1.html

Requirements:
  pip install anthropic

Set your API key:
  export ANTHROPIC_API_KEY=sk-ant-...   (Mac/Linux)
  $env:ANTHROPIC_API_KEY="sk-ant-..."  (Windows PowerShell)
"""

import anthropic
import json
import sys
import os
import re
import argparse
from pathlib import Path
from datetime import datetime

# ── Prompt templates ──────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a senior investment analyst and market strategist at a top-tier hedge fund.
You generate comprehensive, research-backed investment intelligence for supply chain mindmaps.
Your data is specific, current, and actionable — real ticker symbols, real revenue figures, real theses.
Always respond with valid JSON only. No markdown. No code blocks. No explanations outside the JSON."""

DATA_PROMPT = """Generate a detailed investment intelligence mindmap for the topic: "{topic}"

Return a single JSON object following this EXACT schema. Every field is required.

Schema:
{{
  "title": "Short title for browser tab (e.g. 'AI Infrastructure — Investment Guide')",
  "subtitle": "Headline narrative (e.g. 'NVIDIA GB200 · $400B capex cycle · Upstream bottlenecks · Downstream beneficiaries')",
  "headerBadge": "Key stat badge (e.g. 'NVDA: $130B rev · 78% data-center · 57% gross margin')",
  "root": {{
    "id": "root",
    "name": "Short Topic Name\\nSubtitle Line",
    "type": "root",
    "risk": 0,
    "conviction": 0,
    "tam": "—",
    "supplyTension": "hub",
    "tickers": [],
    "desc": "2-sentence overview of the ecosystem and its investment significance.",
    "publicFirms": [],
    "privateFirms": [
      {{"name": "Key Private Co", "meta": "~$XB val · key role"}}
    ],
    "thesis": "3-4 sentence master investment thesis covering the macro narrative.",
    "bull": ["Bull case point 1", "Bull case point 2", "Bull case point 3"],
    "bear": ["Bear case point 1", "Bear case point 2"],
    "children": [
      {{
        "id": "unique-kebab-id",
        "name": "Sector Name\\nSubsector or Focus",
        "type": "upstream",
        "risk": 3,
        "conviction": 4,
        "tam": "$XXB by 20XX",
        "supplyTension": "high",
        "tickers": ["TICK1", "TICK2"],
        "desc": "1-2 sentence description of this sector's role and bottleneck status.",
        "publicFirms": [
          {{
            "ticker": "TICK",
            "name": "Company Name (specific division or product)",
            "rev": "$XB",
            "growth": "+X%",
            "cap": "$XB",
            "signal": "sig-buy",
            "role": "One precise sentence: what this company specifically does within THIS sector for this narrative"
          }}
        ],
        "privateFirms": [
          {{"name": "Private Company", "meta": "$XB val · stage · key note"}}
        ],
        "thesis": "2-3 sentence investment thesis specific to this sector node.",
        "bull": ["Specific bull point with data", "Another bull point"],
        "bear": ["Specific bear risk"],
        "children": []
      }}
    ]
  }}
}}

MANDATORY RULES:
1. Include 3-6 UPSTREAM nodes (supply chain inputs, enabling technology, bottlenecks, raw materials)
2. Include 3-6 DOWNSTREAM nodes (end markets, beneficiaries, applications, platforms)
3. Each node should have 2-4 publicFirms where relevant (fewer for niche/private sectors)
4. Ticker symbols must be real and currently traded (no invented tickers)
5. Revenue, growth, and market cap must be real/estimated figures with appropriate precision
6. "signal" must be exactly one of: sig-sb, sig-buy, sig-hold, sig-cau, sig-avd, sig-spec
   (sb=strong buy, buy, hold, cau=cautious, avd=avoid, spec=speculative)
7. "supplyTension" must be exactly one of: critical, high, medium, demand-led, hub
8. "risk" and "conviction" are integers 0-5
9. The "role" field must explain what the company specifically does in THIS sector, not general company description
10. You may add 1-3 children to any depth-1 node for important sub-sectors
11. Use \\n in "name" fields to create line breaks in the mindmap node labels
12. Return ONLY the JSON object. No preamble, no markdown, no code fences.
"""

# ── Generator ─────────────────────────────────────────────────────────────────

def generate_mindmap_data(topic: str, client: anthropic.Anthropic, model: str) -> dict:
    """Call Claude to produce structured mindmap data for the given topic."""
    print(f"  Generating mindmap data for: {topic!r} ...")
    prompt = DATA_PROMPT.format(topic=topic)

    message = client.messages.create(
        model=model,
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()

    # Strip accidental markdown code fences
    raw = re.sub(r'^```(?:json)?\s*\n?', '', raw)
    raw = re.sub(r'\n?```\s*$', '', raw)
    raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        # Attempt to extract JSON from surrounding text
        match = re.search(r'\{[\s\S]+\}', raw)
        if match:
            return json.loads(match.group(0))
        raise ValueError(f"Claude returned invalid JSON: {e}\n\nRaw output (first 500 chars):\n{raw[:500]}") from e


def render_html(data: dict, template_path: Path) -> str:
    """Inject generated data into the HTML template."""
    template = template_path.read_text(encoding='utf-8')

    title        = data.get('title', 'Market Intelligence Mindmap')
    subtitle     = data.get('subtitle', '')
    header_badge = data.get('headerBadge', '')
    root_data    = data.get('root', data)  # support both wrapped and unwrapped

    # Inject dynamic metadata
    html = template.replace('__TITLE__',        title)
    html = html.replace('__SUBTITLE__',         subtitle)
    html = html.replace('__HEADER_BADGE__',     header_badge)

    # Serialise the root node as the D3 DATA object
    root_json = json.dumps(root_data, ensure_ascii=False, indent=2)
    html = html.replace('__MINDMAP_DATA__', root_json)

    # Stamp generation date in the info bar
    today = datetime.now().strftime('%B %Y')
    html = html.replace('May 2026 — ParkPine Venture Research',
                        f'{today} — Generated by Market Mindmap')

    return html


def main():
    parser = argparse.ArgumentParser(
        description='Generate an investment mindmap website for any sector or narrative.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate.py "AI Infrastructure buildout"
  python generate.py "GLP-1 / Ozempic drug ecosystem" --output glp1-mindmap.html
  python generate.py "Copper supply chain" --model claude-opus-4-5
        """
    )
    parser.add_argument('topic',
                        help='The sector, narrative, or theme to analyse')
    parser.add_argument('--output', '-o', default=None,
                        help='Output HTML filename (default: auto-generated from topic)')
    parser.add_argument('--model', '-m', default='claude-opus-4-5',
                        choices=['claude-opus-4-5', 'claude-sonnet-4-5', 'claude-haiku-4-5'],
                        help='Claude model to use (default: claude-opus-4-5 for best quality)')
    parser.add_argument('--template', '-t', default=None,
                        help='Path to template.html (default: same directory as generate.py)')
    args = parser.parse_args()

    # Locate template
    script_dir = Path(__file__).parent
    template_path = Path(args.template) if args.template else script_dir / 'template.html'
    if not template_path.exists():
        print(f"ERROR: template.html not found at {template_path}")
        sys.exit(1)

    # Resolve output filename
    if args.output:
        out_path = Path(args.output)
    else:
        slug = re.sub(r'[^a-zA-Z0-9]+', '-', args.topic.lower()).strip('-')[:60]
        out_path = Path(f'{slug}-mindmap.html')

    # Resolve API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("  Windows: $env:ANTHROPIC_API_KEY='sk-ant-...'")
        print("  Mac/Linux: export ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print(f"\n Market Mindmap Generator")
    print(f" Topic  : {args.topic}")
    print(f" Model  : {args.model}")
    print(f" Output : {out_path}\n")

    # Generate
    data = generate_mindmap_data(args.topic, client, args.model)
    print(f"  Data generated — {len(data.get('root', {}).get('children', []))} top-level sectors")

    html = render_html(data, template_path)
    out_path.write_text(html, encoding='utf-8')

    print(f"\n Done! Open in your browser:")
    print(f"  {out_path.resolve()}\n")


if __name__ == '__main__':
    main()
