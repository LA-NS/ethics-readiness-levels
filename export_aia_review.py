"""
Generate a reviewable DOCX of the AI in Public Administration AIA questions.
Run: python3 export_aia_review.py
Output: AIA_Expert_Review.docx
"""

import sqlite3
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

DATABASE = "lperl_local.sqlite"
OUTPUT = "AIA_Expert_Review.docx"

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY       = RGBColor(0x1a, 0x3a, 0x5c)
NAVY_LIGHT = RGBColor(0xe8, 0xf0, 0xf8)
MID_BLUE   = RGBColor(0x4a, 0x90, 0xd9)
CHILD_BG   = RGBColor(0xf4, 0xf7, 0xfb)
GRANDCHILD_BG = RGBColor(0xfa, 0xfc, 0xff)
DARK_TEXT  = RGBColor(0x1a, 0x1a, 0x1a)
GREY_TEXT  = RGBColor(0x55, 0x55, 0x55)
COMMENT_BG = RGBColor(0xff, 0xff, 0xf0)
WHITE      = RGBColor(0xff, 0xff, 0xff)

# ── Thematic dimension labels (101–114) ─────────────────────────────────────
DIMENSION_LABELS = {
    "101": "Legal Basis & Citizen Rights",
    "102": "Non-Discrimination & Bias",
    "103": "Transparency & Citizen Information",
    "104": "Explainability",
    "105": "Human Review & Appeal",
    "106": "Meaningful Human Oversight",
    "107": "Data Protection & Privacy",
    "108": "Accuracy & Reliability",
    "109": "Democratic Accountability",
    "110": "Auditability",
    "111": "Private Sector Procurement",
    "112": "Digital Inclusion",
    "113": "Accountability & Redress",
    "114": "Workforce Impact",
}

SCORING_NOTE = {
    "risk":     "Risk — YES activates this dimension (score decreases)",
    "mandatory":"Mandatory — NO at any level decreases the score",
    "mitigation":"Mitigation — YES partially restores the score",
    "validation":"Validation — NO confirms the mitigation fell short",
    "bonus":    "Bonus — YES grants a small additional credit",
}


def set_cell_bg(cell, rgb: RGBColor):
    hex_color = "{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def set_cell_border(cell, **kwargs):
    """kwargs: top/bottom/left/right = (size_pt, color_hex)"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement("w:tcBorders")
    for side, (sz, color) in kwargs.items():
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz * 8))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        tcBorders.append(el)
    tcPr.append(tcBorders)


def add_run(para, text, bold=False, italic=False, color=None, size_pt=None):
    run = para.add_run(text)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color
    if size_pt:
        run.font.size = Pt(size_pt)
    return run


def classify(number: str):
    """Return 'parent' | 'child' | 'grandchild' based on dot depth."""
    parts = number.split(".")
    if len(parts) == 1:
        return "parent"
    elif len(parts) == 2:
        return "child"
    else:
        return "grandchild"


def score_label(yes_score, no_score, level):
    parts = []
    if yes_score != 0:
        sign = "+" if yes_score > 0 else ""
        parts.append(f"YES → {sign}{yes_score:g}")
    if no_score != 0:
        sign = "+" if no_score > 0 else ""
        parts.append(f"NO → {sign}{no_score:g}")
    return "  |  ".join(parts) if parts else "YES/NO → 0"


def fetch_questions():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute(
        "SELECT number, question, yes_score, no_score "
        "FROM questions WHERE block='pub_admin_aia' ORDER BY id"
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def build_doc():
    doc = Document()

    # ── Page margins ────────────────────────────────────────────────────────
    for section in doc.sections:
        section.top_margin    = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin   = Cm(2.2)
        section.right_margin  = Cm(2.2)

    # ── Title block ─────────────────────────────────────────────────────────
    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    add_run(title_para, "AI in Public Administration\n",
            bold=True, color=NAVY, size_pt=18)
    add_run(title_para, "Algorithmic Impact Assessment — Expert Review Draft",
            bold=False, color=GREY_TEXT, size_pt=11)

    doc.add_paragraph()

    # ── Instructions box (table with single cell) ───────────────────────────
    instr_tbl = doc.add_table(rows=1, cols=1)
    instr_tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    cell = instr_tbl.cell(0, 0)
    set_cell_bg(cell, NAVY_LIGHT)
    set_cell_border(cell,
                    top=(1, "4A90D9"), bottom=(1, "4A90D9"),
                    left=(3, "1A3A5C"), right=(1, "4A90D9"))

    cp = cell.paragraphs[0]
    add_run(cp, "How to read this document\n", bold=True, color=NAVY, size_pt=10)
    add_run(cp,
        "Each row is one indicator. The assessment follows a tree structure:\n"
        "  •  Parent indicators (bold, white background) establish whether a risk or obligation applies.\n"
        "  •  Child indicators (indented, light blue) probe mitigations or requirements if the parent triggered.\n"
        "  •  Grandchild indicators (further indented, near-white) validate that child measures are effective.\n\n"
        "Scoring direction is shown in the Score column. A negative YES score means the risk is present; "
        "a positive YES score means a mitigation is in place. "
        "If a parent is answered NO, its children are skipped.\n\n"
        "The Comment column is for reviewers to note concerns, proposed amendments, or alternative formulations. "
        "Use the Rating column to flag each indicator: ✓ Keep  |  ~ Revise  |  ✗ Remove  |  + Add below",
        italic=False, color=DARK_TEXT, size_pt=9.5)

    doc.add_paragraph()

    # ── Question table ───────────────────────────────────────────────────────
    questions = fetch_questions()

    # Column widths (total ≈ 17.6 cm usable after margins)
    col_widths = [Cm(1.0), Cm(8.8), Cm(2.2), Cm(5.2), Cm(1.4)]
    col_headers = ["#", "Indicator", "Score", "Expert Comment", "Rating"]

    tbl = doc.add_table(rows=1, cols=len(col_widths))
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT

    # Set column widths
    for i, w in enumerate(col_widths):
        for cell in tbl.columns[i].cells:
            cell.width = w

    # Header row
    hdr_cells = tbl.rows[0].cells
    for i, (cell, header) in enumerate(zip(hdr_cells, col_headers)):
        set_cell_bg(cell, NAVY)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_run(p, header, bold=True, color=WHITE, size_pt=9)

    current_dimension = None

    for number, question, yes_score, no_score in questions:
        dim_key = number.split(".")[0]
        level = classify(number)

        # ── Dimension separator row ─────────────────────────────────────────
        if dim_key != current_dimension:
            current_dimension = dim_key
            dim_label = DIMENSION_LABELS.get(dim_key, f"Dimension {dim_key}")

            sep_row = tbl.add_row()
            merged = sep_row.cells[0].merge(sep_row.cells[-1])
            set_cell_bg(merged, NAVY)
            p = merged.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            add_run(p, f"  {dim_key}  —  {dim_label.upper()}",
                    bold=True, color=WHITE, size_pt=8.5)

        # ── Question row ────────────────────────────────────────────────────
        q_row = tbl.add_row()
        cells = q_row.cells

        # Set column widths per row
        for i, w in enumerate(col_widths):
            cells[i].width = w

        # Background by level
        if level == "parent":
            row_bg = WHITE
        elif level == "child":
            row_bg = CHILD_BG
        else:
            row_bg = GRANDCHILD_BG

        for c in cells:
            set_cell_bg(c, row_bg)

        # Col 0: number
        p0 = cells[0].paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cells[0].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        add_run(p0, number,
                bold=(level == "parent"), color=NAVY if level == "parent" else GREY_TEXT,
                size_pt=8.5)

        # Col 1: question text with visual indent
        indent_cm = {"parent": 0, "child": 0.4, "grandchild": 0.8}[level]
        p1 = cells[1].paragraphs[0]
        p1.paragraph_format.left_indent = Cm(indent_cm)
        cells[1].vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        # Prefix symbol for children/grandchildren
        if level == "child":
            add_run(p1, "↳ ", bold=False, color=MID_BLUE, size_pt=9)
        elif level == "grandchild":
            add_run(p1, "  ↳ ", bold=False, color=GREY_TEXT, size_pt=9)

        add_run(p1, question,
                bold=(level == "parent"),
                color=DARK_TEXT if level == "parent" else GREY_TEXT,
                size_pt=9 if level == "parent" else 8.5)

        # Col 2: score
        p2 = cells[2].paragraphs[0]
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cells[2].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        sl = score_label(yes_score, no_score, level)
        score_color = GREY_TEXT
        if yes_score < 0 or no_score < 0:
            score_color = RGBColor(0xb0, 0x30, 0x20)
        elif yes_score > 0 or no_score > 0:
            score_color = RGBColor(0x1a, 0x6b, 0x3c)
        add_run(p2, sl, bold=False, color=score_color, size_pt=8)

        # Col 3: comment (empty, for reviewers)
        set_cell_bg(cells[3], COMMENT_BG)
        cells[3].paragraphs[0].add_run("")

        # Col 4: rating
        p4 = cells[4].paragraphs[0]
        p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cells[4].paragraphs[0].add_run("")

    doc.save(OUTPUT)
    print(f"Saved: {OUTPUT}  ({len(questions)} indicators)")


if __name__ == "__main__":
    build_doc()
