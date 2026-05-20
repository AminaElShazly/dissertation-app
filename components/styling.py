"""All custom CSS for the Confidence Trap app — Sheffield brand identity."""

import streamlit as st


_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,300;8..60,400;8..60,500;8..60,600;8..60,700&family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

  :root {
    /* Sheffield brand palette */
    --violet: #440099;          /* brand violet */
    --violet-dark: #2e006b;     /* dark violet */
    --violet-electric: #7c3aed; /* electric violet */
    --violet-pale: #ede9fe;     /* pale violet */
    --violet-powder: #f5f3ff;   /* powder violet */
    --amber: #ffb81c;           /* secondary amber accent */
    --amber-soft: #fff7e0;

    /* Neutrals */
    --paper: #ffffff;
    --canvas: #fafafa;
    --ink: #1a1a1a;
    --ink-soft: #4a4a4a;
    --ink-faint: #7a7a7a;
    --rule: #e5e5e5;

    /* Status */
    --good: #14a34a;
    --good-soft: #e8f5ee;
    --warn: #d97706;
    --error: #dc2626;
    --error-soft: #fee2e2;
  }

  .stApp {
    background: var(--paper);
  }
  .block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1280px;
  }

  /* Typography */
  html, body, [class*="css"] {
    font-family: 'Source Sans 3', -apple-system, sans-serif;
    color: var(--ink);
  }
  h1 {
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-weight: 400 !important;
    letter-spacing: -0.02em !important;
    line-height: 1.05 !important;
    color: var(--ink) !important;
  }
  h2 {
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-weight: 500 !important;
    letter-spacing: -0.015em !important;
    color: var(--ink) !important;
  }
  h3 {
    font-family: 'Source Serif 4', Georgia, serif !important;
    font-weight: 600 !important;
    color: var(--ink) !important;
  }
  p, li, span, div {
    font-family: 'Source Sans 3', sans-serif;
    color: var(--ink);
  }

  /* ============ SIDEBAR ============ */
  [data-testid="stSidebar"] { background: var(--violet); }
  [data-testid="stSidebar"] * { color: #ffffff !important; }
  [data-testid="stSidebar"] .stRadio > label {
    font-family: 'Source Sans 3', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
  }
  [data-testid="stSidebar"] h1,
  [data-testid="stSidebar"] h2,
  [data-testid="stSidebar"] h3 { color: #ffffff !important; }

  /* ============ MASTHEAD ============ */
  .masthead {
    border-top: 4px solid var(--violet);
    border-bottom: 1px solid var(--rule);
    padding: 16px 0;
    margin-bottom: 48px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--ink-faint);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .masthead-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: var(--amber);
    border-radius: 50%;
    margin-right: 10px;
    vertical-align: middle;
  }

  /* ============ SECTION MARKERS ============ */
  .sectnum {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    color: var(--violet);
    margin-bottom: 16px;
    margin-top: 32px;
    display: flex;
    align-items: center;
    gap: 12px;
    text-transform: uppercase;
    font-weight: 600;
  }
  .sectnum::before {
    content: '';
    width: 32px;
    height: 2px;
    background: var(--violet);
  }
  .eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    color: var(--violet);
    text-transform: uppercase;
    margin-bottom: 24px;
    font-weight: 600;
  }

  /* ============ HERO ============ */
  .hero-title {
    font-family: 'Source Serif 4', Georgia, serif;
    font-weight: 400;
    font-size: clamp(40px, 6vw, 68px);
    line-height: 1.05;
    letter-spacing: -0.025em;
    margin-bottom: 32px;
    color: var(--ink);
  }
  .hero-title em {
    font-style: italic;
    color: var(--violet);
    font-weight: 500;
  }
  .hero-title .strike {
    position: relative;
    display: inline-block;
    color: var(--ink-faint);
  }
  .hero-title .strike::after {
    content: '';
    position: absolute;
    left: -4%; right: -4%; top: 52%;
    height: 4px;
    background: var(--amber);
    transform: rotate(-2deg);
  }
  .deck {
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 19px;
    line-height: 1.55;
    color: var(--ink-soft);
    margin-bottom: 48px;
    max-width: 820px;
  }

  /* ============ FINDING CARDS ============ */
  .finding {
    background: var(--canvas);
    border: 1px solid var(--rule);
    border-radius: 8px;
    padding: 32px;
    margin-bottom: 16px;
    min-height: 280px;
  }
  .finding.critical {
    background: var(--violet);
    color: #ffffff;
    border-color: var(--violet-dark);
  }
  .finding.critical .finding-label,
  .finding.critical .finding-detail,
  .finding.critical .finding-suffix { color: rgba(255, 255, 255, 0.85); }
  .finding-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    font-weight: 500;
  }
  .finding-stat {
    font-family: 'Source Serif 4', serif;
    font-weight: 300;
    font-size: 68px;
    line-height: 0.95;
    letter-spacing: -0.03em;
    margin-bottom: 16px;
    color: var(--violet);
  }
  .finding.critical .finding-stat { color: var(--amber); }
  .finding-suffix { font-size: 24px; color: var(--ink-faint); font-weight: 400; }
  .finding-headline {
    font-family: 'Source Serif 4', serif;
    font-size: 18px;
    font-weight: 500;
    line-height: 1.3;
    margin-bottom: 12px;
  }
  .finding-headline em {
    color: var(--violet);
    font-style: italic;
  }
  .finding.critical .finding-headline em {
    color: var(--amber);
    font-style: italic;
  }
  .finding-detail {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  /* ============ EXPLANATION PANELS ============ */
  .ai-panel {
    background: var(--canvas);
    border-left: 3px solid var(--violet);
    border-radius: 4px;
    padding: 20px 24px;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 14.5px;
    line-height: 1.65;
    color: var(--ink);
  }
  .ai-panel .err {
    background: var(--amber-soft);
    border-bottom: 2px solid var(--amber);
    padding: 0 2px;
    border-radius: 2px;
  }
  .ai-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--violet);
    margin-bottom: 12px;
    font-weight: 600;
  }
  .ai-label::before {
    content: '●';
    margin-right: 8px;
    color: var(--amber);
  }

  .source-panel {
    background: var(--violet-powder);
    border-left: 3px solid var(--violet-electric);
    border-radius: 4px;
    padding: 20px 24px;
    font-family: 'Source Serif 4', serif;
    font-size: 14.5px;
    line-height: 1.6;
    color: var(--ink-soft);
  }
  .source-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--violet-electric);
    margin-bottom: 12px;
    font-weight: 600;
  }
  .source-label::before {
    content: '●';
    margin-right: 8px;
    color: var(--violet-electric);
  }

  /* ============ INLINE-LABELLED SCORE ROWS ============ */
  .scoreitem {
    display: grid;
    grid-template-columns: 64px 1fr 100px 100px;
    align-items: center;
    gap: 16px;
    padding: 10px 0;
    border-bottom: 1px solid var(--rule);
  }
  .scoreitem:last-child { border-bottom: none; }
  .scoreitem-header {
    display: grid;
    grid-template-columns: 64px 1fr 100px 100px;
    align-items: center;
    gap: 16px;
    padding: 8px 0 12px;
    border-bottom: 2px solid var(--ink);
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--ink-faint);
    font-weight: 600;
  }
  .scoreitem-code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    color: var(--violet);
    letter-spacing: 0.05em;
  }
  .scoreitem-label {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 14px;
    line-height: 1.4;
    color: var(--ink);
  }
  .scoreitem-label .desc {
    color: var(--ink-faint);
    font-size: 12.5px;
    display: block;
    margin-top: 2px;
  }
  .scoreitem-cell {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    padding: 6px 0;
    border-radius: 4px;
  }
  .scoreitem-cell.pass {
    background: var(--good-soft);
    color: var(--good);
  }
  .scoreitem-cell.fail {
    background: var(--error-soft);
    color: var(--error);
  }

  /* Totals row */
  .scoreitem-total {
    display: grid;
    grid-template-columns: 64px 1fr 100px 100px;
    align-items: center;
    gap: 16px;
    padding: 16px 0 8px;
    border-top: 2px solid var(--ink);
    margin-top: 8px;
  }
  .scoreitem-total .label {
    font-family: 'Source Serif 4', serif;
    font-size: 15px;
    font-weight: 600;
    color: var(--ink);
  }
  .scoreitem-total .val {
    text-align: center;
    font-family: 'Source Serif 4', serif;
    font-size: 22px;
    font-weight: 500;
    color: var(--violet);
  }
  .scoreitem-total .val .unit {
    font-size: 13px;
    color: var(--ink-faint);
    margin-left: 2px;
  }

  /* ============ BIG METRIC ============ */
  .bigmetric {
    text-align: left;
    padding: 24px;
    background: var(--canvas);
    border: 1px solid var(--rule);
    border-radius: 8px;
  }
  .bigmetric-value {
    font-family: 'Source Serif 4', serif;
    font-weight: 400;
    font-size: 48px;
    line-height: 1;
    letter-spacing: -0.02em;
    color: var(--violet);
  }
  .bigmetric-suffix {
    font-size: 18px;
    color: var(--ink-faint);
    font-weight: 400;
  }
  .bigmetric-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin-top: 8px;
    font-weight: 600;
  }

  /* ============ GUIDELINE CARDS ============ */
  .guideline-card {
    background: var(--canvas);
    border: 1px solid var(--rule);
    border-left: 3px solid var(--violet);
    border-radius: 4px;
    padding: 24px 28px 24px 80px;
    margin-bottom: 16px;
    position: relative;
  }
  .guideline-num {
    position: absolute;
    left: 24px;
    top: 26px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    font-weight: 700;
    color: var(--violet);
    letter-spacing: 0.02em;
  }
  .guideline-title {
    font-family: 'Source Serif 4', serif;
    font-size: 19px;
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: 8px;
    color: var(--ink);
  }
  .guideline-body {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: var(--ink-soft);
  }
  .guideline-body strong { color: var(--ink); font-weight: 600; }

  /* ============ AUDIENCE HEADERS ============ */
  .audience-header {
    padding: 24px 0 8px;
    border-top: 2px solid var(--violet);
    margin-bottom: 24px;
  }
  .audience-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin-bottom: 8px;
    font-weight: 600;
  }
  .audience-name {
    font-family: 'Source Serif 4', serif;
    font-size: 30px;
    font-weight: 500;
    line-height: 1.15;
    margin-bottom: 6px;
    color: var(--ink);
  }
  .audience-name em { font-style: italic; color: var(--violet); }
  .audience-tagline {
    font-family: 'Source Serif 4', serif;
    font-size: 15px;
    color: var(--ink-soft);
    margin-bottom: 16px;
  }

  /* ============ RED FLAG CARDS ============ */
  .redflag {
    background: var(--canvas);
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 20px 24px;
    margin-bottom: 12px;
    position: relative;
  }
  .redflag-code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    color: var(--violet);
    margin-bottom: 6px;
  }
  .redflag-rate {
    position: absolute;
    top: 20px; right: 24px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--ink-faint);
    letter-spacing: 0.02em;
  }
  .redflag-title {
    font-family: 'Source Serif 4', serif;
    font-size: 16px;
    font-weight: 600;
    line-height: 1.3;
    margin-bottom: 6px;
    padding-right: 60px;
    color: var(--ink);
  }
  .redflag-detail {
    font-family: 'Source Sans 3', sans-serif;
    font-size: 13px;
    line-height: 1.55;
    color: var(--ink-soft);
  }

  /* Hide Streamlit chrome */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }

  /* ============ TABS ============ */
  .stTabs [data-baseweb="tab-list"] {
    gap: 0;
    border-bottom: 1px solid var(--rule);
  }
  .stTabs [data-baseweb="tab"] {
    font-family: 'Source Sans 3', sans-serif !important;
    font-size: 13px !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    padding: 14px 24px !important;
    background: transparent !important;
    border-radius: 0 !important;
    color: var(--ink-faint) !important;
    font-weight: 600 !important;
  }
  .stTabs [aria-selected="true"] {
    background: var(--violet) !important;
    color: #ffffff !important;
  }

  /* ============ FORM ELEMENTS ============ */
  .stSelectbox label, .stMultiSelect label, .stSlider label, .stRadio > label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: var(--ink-faint) !important;
    font-weight: 600 !important;
  }

  /* Section dividers */
  .sect-divider {
    border-top: 1px solid var(--rule);
    margin: 56px 0 0 0;
  }

  /* Expander */
  .streamlit-expanderHeader {
    font-family: 'Source Serif 4', serif !important;
    font-style: italic !important;
    color: var(--violet) !important;
  }

  /* Caption styling */
  .scaption {
    font-family: 'Source Serif 4', serif;
    font-style: italic;
    font-size: 15px;
    color: var(--ink-soft);
    margin: 16px 0 24px;
    max-width: 740px;
    line-height: 1.55;
  }
</style>
"""


def inject_styles() -> None:
    """Inject the app's custom CSS into the current Streamlit page."""
    st.markdown(_CSS, unsafe_allow_html=True)
