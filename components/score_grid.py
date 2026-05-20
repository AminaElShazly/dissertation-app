"""
Score-display components — each checklist / error item is a labelled row with
the full description visible inline (not just an opaque code).
"""

import streamlit as st

from data.loader import (
    CHECKLIST_CODES,
    ERROR_CODES,
    image_path,
)


# ─────────────────────────────────────────────────────────────
# FULL DESCRIPTIONS (shown inline next to each row)
# ─────────────────────────────────────────────────────────────

CHECKLIST_FULL = {
    'c1': ('Chart type',
           'Is the chart correctly named (bar, line, scatter, etc.)?'),
    'c2': ('X-axis',
           'Is the x-axis variable and units correctly identified?'),
    'c3': ('Y-axis',
           'Is the y-axis variable and units correctly identified?'),
    'c4': ('Highest value',
           'Is the maximum or peak value correctly identified?'),
    'c5': ('Lowest value',
           'Is the minimum or trough value correctly identified?'),
    'c6': ('Trend direction',
           'Is the overall direction (rise / fall / flat) stated correctly?'),
    'c7': ('Trend pattern',
           'Is the shape (linear, curved, volatile, monotonic) described correctly?'),
    'c8': ('Comparisons',
           'Are any stated comparisons between groups or values accurate?'),
    'c9': ('No fabrication',
           'Is the explanation free of invented data, causes, or context?'),
    'c10': ('Primary finding',
            "Does the explanation capture the chart's headline takeaway?"),
}

ERROR_FULL = {
    'fe1': ('Value error',
            'A stated numeric value does not match the chart.'),
    'fe2': ('Label error',
            'An axis label, category, or unit is named incorrectly.'),
    'fe3a': ('Trend direction',
             'A trend direction (rising / falling / flat) is reversed.'),
    'fe3b': ('Trend pattern',
             'A trend pattern (linear / curved / volatile) is misdescribed.'),
    'fe4': ('Magnitude',
            'The size of a difference or change is misstated.'),
    'fe5': ('Extremum',
            'The highest or lowest value is misidentified.'),
    'hm1': ('Fabricated content',
            'A data point, year, or entity not on the chart appears in the text.'),
    'hm2': ('Unsupported inference',
            'An unsupported causal or interpretive claim is added.'),
    'oe1': ('Critical omission',
            'A finding central to the chart is omitted from the explanation.'),
}


# ─────────────────────────────────────────────────────────────
# CORE RENDER FUNCTIONS
# ─────────────────────────────────────────────────────────────

def _highlight_errors(text: str, errors_present: dict[str, bool]) -> str:
    """
    Mark places in an AI explanation that *might* correspond to errors.

    Conservative heuristic: if HM2 is flagged, highlight obvious causal phrases.
    The authoritative coding is the score grid below the text.
    """
    if errors_present.get('hm2'):
        causal_phrases = [
            'driven by', 'caused by', 'due to', 'as a result of',
            'led to', 'attributable to', 'because of', 'resulting from',
        ]
        for phrase in causal_phrases:
            for variant in [phrase, phrase.capitalize()]:
                if variant in text:
                    idx = text.find(variant)
                    end = text.find('.', idx)
                    if end == -1:
                        end = min(len(text), idx + 80)
                    if '<span class="err"' in text[max(0, idx - 30):idx]:
                        continue
                    text = (
                        text[:idx]
                        + f'<span class="err">{text[idx:end]}</span>'
                        + text[end:]
                    )
    return text


def _render_score_table(chart_row, kind: str) -> None:
    """
    Render a labelled score table with full inline descriptions.

    kind='checklist' uses C1-C10 (1=pass green, 0=fail red).
    kind='errors' uses FE/HM/OE codes (1=error present red, 0=clean green; semantics flipped for color).
    """
    if kind == 'checklist':
        codes = CHECKLIST_CODES
        descriptions = CHECKLIST_FULL
        gpt_total = int(chart_row['gpt4o_total'])
        claude_total = int(chart_row['claude_total'])
        total_unit = '/10'
        invert = False  # 1 = pass = green
    else:
        codes = ERROR_CODES
        descriptions = ERROR_FULL
        gpt_total = int(chart_row['gpt4o_err_count'])
        claude_total = int(chart_row['claude_err_count'])
        total_unit = '/9 errors'
        invert = True  # 1 = error present = red

    # Header row
    st.markdown(
        '<div class="scoreitem-header">'
        '<span>Code</span>'
        '<span>Description</span>'
        '<span style="text-align:center;">GPT-4o</span>'
        '<span style="text-align:center;">Claude</span>'
        '</div>',
        unsafe_allow_html=True,
    )

    # Item rows
    rows_html = []
    for code in codes:
        gpt_val = int(chart_row[f'gpt4o_{code}'])
        claude_val = int(chart_row[f'claude_{code}'])

        if invert:
            gpt_pass = (gpt_val == 0)
            claude_pass = (claude_val == 0)
            gpt_cell_text = 'Present' if gpt_val == 1 else 'Absent'
            claude_cell_text = 'Present' if claude_val == 1 else 'Absent'
        else:
            gpt_pass = (gpt_val == 1)
            claude_pass = (claude_val == 1)
            gpt_cell_text = 'Pass' if gpt_pass else 'Fail'
            claude_cell_text = 'Pass' if claude_pass else 'Fail'

        gpt_cls = 'pass' if gpt_pass else 'fail'
        claude_cls = 'pass' if claude_pass else 'fail'

        short_label, full_desc = descriptions[code]
        code_label = code.upper()

        rows_html.append(
            f'<div class="scoreitem">'
            f'<span class="scoreitem-code">{code_label}</span>'
            f'<span class="scoreitem-label"><strong>{short_label}</strong>'
            f'<span class="desc">{full_desc}</span></span>'
            f'<span class="scoreitem-cell {gpt_cls}">{gpt_cell_text}</span>'
            f'<span class="scoreitem-cell {claude_cls}">{claude_cell_text}</span>'
            f'</div>'
        )

    st.markdown(''.join(rows_html), unsafe_allow_html=True)

    # Totals row
    st.markdown(
        f'<div class="scoreitem-total">'
        f'<span></span>'
        f'<span class="label">{"Total checklist score" if kind == "checklist" else "Total errors flagged"}</span>'
        f'<span class="val">{gpt_total}<span class="unit">{total_unit}</span></span>'
        f'<span class="val">{claude_total}<span class="unit">{total_unit}</span></span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def render_chart_detail(chart_row, show_image: bool = True) -> None:
    """
    Render the full detail view for one chart.

    Used by:
      - Visualisation Explorer when a chart is selected
      - Model Evaluation Dashboard's drill-down panel
    """
    # Image
    if show_image:
        img = image_path(int(chart_row['chart_id']))
        if img.exists():
            st.image(str(img), use_container_width=True)
        else:
            st.warning(f"Image not found: {img.name}")

    # Title + metadata
    st.markdown(
        f"""
        <div style="margin-top: 16px;">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 10px;
                      letter-spacing: 0.15em; text-transform: uppercase; color: var(--ink-faint);
                      margin-bottom: 6px; font-weight: 600;">
            Chart #{chart_row['chart_id']} · {chart_row['chart_type']} · {chart_row['complexity']}
          </div>
          <div style="font-family: 'Source Serif 4', serif; font-size: 22px; font-weight: 500;
                      line-height: 1.3; color: var(--ink); margin-bottom: 24px;">
            {chart_row['title']}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Source caption (ground truth)
    st.markdown(
        f"""
        <div class="source-panel">
          <div class="source-label">Source paper · ground truth</div>
          {chart_row['source_caption']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div style="margin-top: 32px;"></div>', unsafe_allow_html=True)

    # Two-column AI explanations
    col_g, col_c = st.columns(2)

    with col_g:
        gpt_errors = {code: bool(chart_row[f'gpt4o_{code}']) for code in ERROR_CODES}
        highlighted = _highlight_errors(str(chart_row['gpt4o_explanation']), gpt_errors)
        st.markdown(
            f"""
            <div class="ai-panel">
              <div class="ai-label">GPT-4o explanation</div>
              {highlighted.replace(chr(10), '<br>')}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c:
        claude_errors = {code: bool(chart_row[f'claude_{code}']) for code in ERROR_CODES}
        highlighted = _highlight_errors(str(chart_row['claude_explanation']), claude_errors)
        st.markdown(
            f"""
            <div class="ai-panel">
              <div class="ai-label">Claude Sonnet 4.6 explanation</div>
              {highlighted.replace(chr(10), '<br>')}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="sect-divider"></div>', unsafe_allow_html=True)

    # Checklist scoring
    st.markdown(
        '<div class="sectnum">Checklist scoring · C1–C10</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="scaption">Ten accuracy items. A score of 1 means the model handled the item correctly.</p>',
        unsafe_allow_html=True,
    )
    _render_score_table(chart_row, kind='checklist')

    # Error taxonomy scoring
    st.markdown(
        '<div class="sectnum" style="margin-top: 40px;">Error taxonomy · 9 categories</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="scaption">Nine binary error categories from Huang et al. (2024). '
        '"Absent" means the error was not found in the explanation.</p>',
        unsafe_allow_html=True,
    )
    _render_score_table(chart_row, kind='errors')


# Kept for backwards compatibility — no longer needed but referenced in some places
def render_score_grid(*args, **kwargs):
    pass
