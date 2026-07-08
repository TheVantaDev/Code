from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas
import math

# ── Palette ──────────────────────────────────────────────────────────────────
NAVY      = colors.HexColor("#0A1628")
BLUE      = colors.HexColor("#1A3A6B")
ACCENT    = colors.HexColor("#E63946")
GOLD      = colors.HexColor("#F4A261")
TEAL      = colors.HexColor("#2EC4B6")
LIGHT_BG  = colors.HexColor("#F0F4FF")
MID_BG    = colors.HexColor("#D6E4FF")
WHITE     = colors.white
DARK_TEXT = colors.HexColor("#0D1B2A")
MUTED     = colors.HexColor("#6B7C99")
GREEN     = colors.HexColor("#2DC653")
ORANGE    = colors.HexColor("#F4A261")
CARD_BG   = colors.HexColor("#EBF2FF")

W, H = A4

# ── Styles ────────────────────────────────────────────────────────────────────
def make_styles():
    return {
        "cover_title": ParagraphStyle("cover_title",
            fontName="Helvetica-Bold", fontSize=34, textColor=WHITE,
            leading=40, alignment=TA_LEFT, spaceAfter=6),
        "cover_sub": ParagraphStyle("cover_sub",
            fontName="Helvetica", fontSize=13, textColor=colors.HexColor("#A8C4FF"),
            leading=18, alignment=TA_LEFT, spaceAfter=4),
        "cover_tag": ParagraphStyle("cover_tag",
            fontName="Helvetica-Bold", fontSize=10, textColor=GOLD,
            leading=14, alignment=TA_LEFT),
        "section_title": ParagraphStyle("section_title",
            fontName="Helvetica-Bold", fontSize=18, textColor=NAVY,
            leading=22, spaceBefore=14, spaceAfter=6),
        "section_num": ParagraphStyle("section_num",
            fontName="Helvetica-Bold", fontSize=11, textColor=ACCENT,
            leading=14, spaceBefore=2, spaceAfter=2),
        "subsection": ParagraphStyle("subsection",
            fontName="Helvetica-Bold", fontSize=12, textColor=BLUE,
            leading=16, spaceBefore=8, spaceAfter=3),
        "body": ParagraphStyle("body",
            fontName="Helvetica", fontSize=9.5, textColor=DARK_TEXT,
            leading=15, spaceBefore=3, spaceAfter=3, alignment=TA_JUSTIFY),
        "body_bold": ParagraphStyle("body_bold",
            fontName="Helvetica-Bold", fontSize=9.5, textColor=DARK_TEXT,
            leading=15, spaceBefore=2, spaceAfter=2),
        "bullet": ParagraphStyle("bullet",
            fontName="Helvetica", fontSize=9.5, textColor=DARK_TEXT,
            leading=15, leftIndent=14, spaceBefore=2, spaceAfter=2,
            bulletIndent=4, alignment=TA_LEFT),
        "code": ParagraphStyle("code",
            fontName="Courier", fontSize=8.5, textColor=colors.HexColor("#1A1A2E"),
            leading=13, leftIndent=10, spaceBefore=4, spaceAfter=4,
            backColor=colors.HexColor("#EDF2FF")),
        "caption": ParagraphStyle("caption",
            fontName="Helvetica", fontSize=8, textColor=MUTED,
            leading=11, alignment=TA_CENTER, spaceAfter=4),
        "metric_big": ParagraphStyle("metric_big",
            fontName="Helvetica-Bold", fontSize=26, textColor=ACCENT,
            leading=30, alignment=TA_CENTER),
        "metric_label": ParagraphStyle("metric_label",
            fontName="Helvetica", fontSize=8, textColor=MUTED,
            leading=11, alignment=TA_CENTER),
        "table_header": ParagraphStyle("table_header",
            fontName="Helvetica-Bold", fontSize=9, textColor=WHITE,
            leading=12, alignment=TA_CENTER),
        "table_cell": ParagraphStyle("table_cell",
            fontName="Helvetica", fontSize=8.5, textColor=DARK_TEXT,
            leading=12, alignment=TA_LEFT),
        "highlight_box": ParagraphStyle("highlight_box",
            fontName="Helvetica-Bold", fontSize=10, textColor=NAVY,
            leading=15, leftIndent=10, spaceBefore=4, spaceAfter=4),
        "footer": ParagraphStyle("footer",
            fontName="Helvetica", fontSize=7.5, textColor=MUTED,
            leading=10, alignment=TA_CENTER),
        "toc_item": ParagraphStyle("toc_item",
            fontName="Helvetica", fontSize=10, textColor=BLUE,
            leading=18, leftIndent=8),
    }

# ── Custom Flowables ──────────────────────────────────────────────────────────
class ColorBar(Flowable):
    def __init__(self, w, h, color, radius=3):
        self.bar_w, self.bar_h, self.color, self.radius = w, h, color, radius
    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.roundRect(0, 0, self.bar_w, self.bar_h, self.radius, fill=1, stroke=0)
    def wrap(self, *args): return self.bar_w, self.bar_h

class SectionHeader(Flowable):
    """Full-width colored section header band."""
    def __init__(self, number, title, color=NAVY, width=None):
        self.number, self.title, self.color = number, title, color
        self._width = width or (W - 28*mm)
    def wrap(self, *args): return self._width, 36
    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.roundRect(0, 2, self._width, 32, 4, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(10, 12, self.number)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(46, 12, self.title)

class MetricCard(Flowable):
    def __init__(self, value, label, color=ACCENT, w=52*mm, h=28*mm):
        self.value, self.label, self.color = value, label, color
        self.card_w, self.card_h = w, h
    def wrap(self, *args): return self.card_w, self.card_h
    def draw(self):
        c = self.canv
        c.setFillColor(CARD_BG)
        c.roundRect(0, 0, self.card_w, self.card_h, 6, fill=1, stroke=0)
        c.setFillColor(self.color)
        c.roundRect(0, self.card_h-5, self.card_w, 5, 0, fill=1, stroke=0)
        c.setFillColor(self.color)
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(self.card_w/2, self.card_h/2 - 2, self.value)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 7)
        c.drawCentredString(self.card_w/2, 7, self.label)

class PipelineStep(Flowable):
    def __init__(self, num, title, desc, color=BLUE, width=None):
        self.num, self.title, self.desc = num, title, desc
        self.color = color
        self._width = width or (W - 28*mm)
    def wrap(self, *args): return self._width, 38
    def draw(self):
        c = self.canv
        # Circle
        c.setFillColor(self.color)
        c.circle(16, 20, 14, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(16, 16, str(self.num))
        # Line connecting (not for last)
        # Title
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(36, 24, self.title)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 8.5)
        c.drawString(36, 11, self.desc)
        # Separator
        c.setStrokeColor(MID_BG)
        c.setLineWidth(0.5)
        c.line(36, 4, self._width, 4)

class AlertBox(Flowable):
    """Colored info/warning box."""
    def __init__(self, text, icon="!", color=GOLD, width=None, height=None):
        self.text, self.icon, self.color = text, icon, color
        self._width = width or (W - 28*mm)
        self._height = height or 28
    def wrap(self, *args): return self._width, self._height
    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.setFillAlpha(0.12)
        c.roundRect(0, 0, self._width, self._height, 5, fill=1, stroke=0)
        c.setFillAlpha(1)
        c.setFillColor(self.color)
        c.circle(14, self._height/2, 9, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(14, self._height/2 - 3, self.icon)
        c.setFillColor(DARK_TEXT)
        c.setFont("Helvetica", 8.5)
        # Simple text (no wrapping for now)
        c.drawString(30, self._height/2 - 4, self.text)

# ── Page template ─────────────────────────────────────────────────────────────
def build_cover(c, doc):
    c.saveState()
    # Background gradient simulation
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # Decorative circles
    c.setFillColor(BLUE)
    c.circle(W - 40*mm, H - 30*mm, 55*mm, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#0F2040"))
    c.circle(W - 20*mm, H - 60*mm, 35*mm, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#061020"))
    c.circle(40*mm, 40*mm, 60*mm, fill=1, stroke=0)
    # Accent stripe
    c.setFillColor(ACCENT)
    c.rect(0, H - 6*mm, W, 6*mm, fill=1, stroke=0)
    # Gold bar left
    c.setFillColor(GOLD)
    c.rect(14*mm, 60*mm, 2.5*mm, 80*mm, fill=1, stroke=0)
    # Main title
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(22*mm, H - 50*mm, "SentinelAI")
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(22*mm, H - 60*mm, "AI/ML-Powered Mule Account Detection System")
    # Subtitle
    c.setFillColor(colors.HexColor("#A8C4FF"))
    c.setFont("Helvetica", 10)
    c.drawString(22*mm, H - 70*mm, "Bank of India  ·  Cyber Fraud Prevention Hackathon  ·  2025")
    # Divider
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(22*mm, H - 75*mm, W - 22*mm, H - 75*mm)
    # Three headline stats
    stats = [
        ("9,082", "Banking Accounts Analysed"),
        ("3,924", "Features Engineered & Selected"),
        ("0.89%", "Mule Account Prevalence"),
    ]
    x_positions = [22*mm, 85*mm, 148*mm]
    for i, (val, lbl) in enumerate(stats):
        xp = x_positions[i]
        c.setFillColor(ACCENT)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(xp, H - 95*mm, val)
        c.setFillColor(colors.HexColor("#A8C4FF"))
        c.setFont("Helvetica", 8)
        c.drawString(xp, H - 101*mm, lbl)
    # Problem framing
    c.setFillColor(colors.HexColor("#0F2040"))
    c.roundRect(22*mm, H - 145*mm, W - 44*mm, 35*mm, 6, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(28*mm, H - 117*mm, "CHALLENGE")
    c.setFillColor(WHITE)
    c.setFont("Helvetica", 9)
    c.drawString(28*mm, H - 125*mm, "Traditional rule-based fraud systems fail to detect")
    c.drawString(28*mm, H - 133*mm, "evolving mule account behaviour in real-time banking transactions.")
    # Key claims row
    claims = [
        ("XGBoost + SHAP", "Explainable AI Core"),
        ("Isolation Forest", "Unsupervised Anomaly Layer"),
        ("Risk Score Bands", "SAR Alert Generation"),
        ("PMLA / RBI", "Regulatory Compliance"),
    ]
    box_w = (W - 44*mm) / 4
    for i, (val, lbl) in enumerate(claims):
        xp = 22*mm + i * box_w
        yp = H - 175*mm
        c.setFillColor(BLUE)
        c.roundRect(xp, yp, box_w - 3*mm, 24*mm, 4, fill=1, stroke=0)
        c.setFillColor(TEAL)
        c.setFont("Helvetica-Bold", 8.5)
        tw = c.stringWidth(val, "Helvetica-Bold", 8.5)
        c.drawString(xp + (box_w - 3*mm)/2 - tw/2, yp + 14, val)
        c.setFillColor(colors.HexColor("#A8C4FF"))
        c.setFont("Helvetica", 7)
        tw2 = c.stringWidth(lbl, "Helvetica", 7)
        c.drawString(xp + (box_w - 3*mm)/2 - tw2/2, yp + 5, lbl)
    # Footer
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.5)
    c.drawString(22*mm, 15*mm, "Confidential — Submitted for BOI Hackathon 2025")
    c.drawRightString(W - 22*mm, 15*mm, "SentinelAI v1.0  |  AI/ML Fraud Detection")
    c.restoreState()

def on_later_page(c, doc):
    c.saveState()
    # Top bar
    c.setFillColor(NAVY)
    c.rect(0, H - 12*mm, W, 12*mm, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.rect(0, H - 12*mm, 5*mm, 12*mm, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(10*mm, H - 8*mm, "SentinelAI")
    c.setFillColor(colors.HexColor("#A8C4FF"))
    c.setFont("Helvetica", 7.5)
    c.drawRightString(W - 14*mm, H - 8*mm, "AI/ML Mule Account Detection  ·  BOI Hackathon 2025")
    # Bottom bar
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, W, 10*mm, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7)
    c.drawString(14*mm, 3.5*mm, "Confidential — For Hackathon Evaluation Only")
    c.drawRightString(W - 14*mm, 3.5*mm, f"Page {doc.page}")
    # Accent line
    c.setFillColor(ACCENT)
    c.rect(0, 9.5*mm, W, 0.8*mm, fill=1, stroke=0)
    c.restoreState()

# ── Document builder ──────────────────────────────────────────────────────────
def build():
    path = "/mnt/user-data/outputs/SentinelAI_BOI_Hackathon.pdf"
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=14*mm, rightMargin=14*mm,
        topMargin=18*mm, bottomMargin=16*mm,
        title="SentinelAI – Mule Account Detection",
        author="Hackathon Team"
    )

    S = make_styles()
    story = []
    CW = W - 28*mm  # content width

    def h(n): story.append(Spacer(1, n))
    def sec(num, title, color=NAVY):
        story.append(Spacer(1, 8))
        story.append(SectionHeader(num, title, color, CW))
        story.append(Spacer(1, 8))
    def sub(txt): story.append(Paragraph(txt, S["subsection"]))
    def body(txt): story.append(Paragraph(txt, S["body"]))
    def bold(txt): story.append(Paragraph(txt, S["body_bold"]))
    def bullet(txt): story.append(Paragraph(f"• {txt}", S["bullet"]))
    def code(txt): story.append(Paragraph(txt, S["code"]))
    def hr(): story.append(HRFlowable(width=CW, thickness=0.5, color=MID_BG, spaceAfter=6, spaceBefore=6))

    # ── COVER PAGE ────────────────────────────────────────────────────────────
    story.append(Spacer(1, H - 28*mm))  # push to fill (cover drawn by callback)
    story.append(PageBreak())

    # ── TABLE OF CONTENTS ─────────────────────────────────────────────────────
    sec("00", "TABLE OF CONTENTS", BLUE)
    toc_items = [
        ("01", "Problem Statement & Motivation"),
        ("02", "Dataset Analysis & EDA"),
        ("03", "Data Preprocessing Strategy"),
        ("04", "Feature Engineering"),
        ("05", "ML Pipeline — End-to-End"),
        ("06", "Model Architecture: XGBoost Champion + Isolation Forest"),
        ("07", "SHAP Explainability Framework"),
        ("08", "Risk Scoring & Alert Generation"),
        ("09", "Expected Results & Benchmarks"),
        ("10", "Regulatory Compliance — PMLA / RBI / FATF"),
        ("11", "Limitations & Future Work"),
    ]
    for num, title in toc_items:
        row = Table(
            [[Paragraph(f"<b>{num}</b>", S["body_bold"]), Paragraph(title, S["toc_item"]),
              Paragraph("···", S["caption"])]],
            colWidths=[12*mm, CW - 28*mm, 16*mm]
        )
        row.setStyle(TableStyle([
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("LINEBELOW", (0,0), (-1,-1), 0.4, MID_BG),
        ]))
        story.append(row)
    h(6)
    story.append(PageBreak())

    # ── SECTION 01 — PROBLEM STATEMENT ───────────────────────────────────────
    sec("01", "PROBLEM STATEMENT & MOTIVATION", NAVY)
    body(
        "Financial mule accounts are bank accounts used by fraudsters — knowingly or unknowingly — "
        "to receive, layer, and transfer illegal funds across banking channels. The Bank of India (BOI) "
        "faces a growing challenge: traditional rule-based monitoring systems operate on static thresholds "
        "and predefined patterns, making them blind to the dynamic, evolving behavioural signatures that "
        "characterise mule account activity."
    )
    h(4)

    pain_data = [
        [Paragraph("<b>Challenge</b>", S["table_header"]),
         Paragraph("<b>Traditional System Limitation</b>", S["table_header"]),
         Paragraph("<b>Our Approach</b>", S["table_header"])],
        [Paragraph("Evolving fraud patterns", S["table_cell"]),
         Paragraph("Static rule thresholds miss novel behaviour", S["table_cell"]),
         Paragraph("XGBoost learns non-linear patterns from data", S["table_cell"])],
        [Paragraph("Extreme class imbalance", S["table_cell"]),
         Paragraph("Rules treat all accounts equally", S["table_cell"]),
         Paragraph("SMOTE + scale_pos_weight balancing", S["table_cell"])],
        [Paragraph("Alert fatigue (too many false positives)", S["table_cell"]),
         Paragraph("Binary flag with no confidence score", S["table_cell"]),
         Paragraph("Probabilistic risk score 0–100", S["table_cell"])],
        [Paragraph("Opaque decisions", S["table_cell"]),
         Paragraph("No explanation for why account was flagged", S["table_cell"]),
         Paragraph("SHAP force plots per account", S["table_cell"])],
        [Paragraph("Real-time detection lag", S["table_cell"]),
         Paragraph("Batch processing with delays", S["table_cell"]),
         Paragraph("Lightweight model inference <10ms", S["table_cell"])],
    ]
    t = Table(pain_data, colWidths=[50*mm, 65*mm, 65*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("BACKGROUND", (0,1), (-1,1), CARD_BG),
        ("BACKGROUND", (0,2), (-1,2), WHITE),
        ("BACKGROUND", (0,3), (-1,3), CARD_BG),
        ("BACKGROUND", (0,4), (-1,4), WHITE),
        ("BACKGROUND", (0,5), (-1,5), CARD_BG),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    h(8)

    sub("Why This Matters")
    body(
        "Mule accounts are the backbone of cyber-enabled financial fraud — used in phishing, "
        "investment scams, romance fraud, and business email compromise. The RBI's Annual Report 2023 "
        "recorded over ₹30,000 crore in digital fraud-related losses. FATF guidelines mandate proactive "
        "detection and Suspicious Activity Report (SAR) generation. Our system — <b>SentinelAI</b> — "
        "directly addresses this gap with an end-to-end ML pipeline purpose-built for the BOI dataset."
    )
    story.append(PageBreak())

    # ── SECTION 02 — DATASET ANALYSIS ────────────────────────────────────────
    sec("02", "DATASET ANALYSIS & EDA", BLUE)
    sub("Dataset Overview")
    body(
        "The dataset provided by BOI contains anonymised transactional and behavioural features "
        "across 9,082 bank accounts. The target variable <b>F3924</b> indicates whether an account "
        "is a confirmed mule (1) or legitimate (0). With only 81 mule accounts out of 9,082, the "
        "dataset presents one of the most challenging class imbalance ratios seen in fraud detection — "
        "approximately <b>1 mule for every 111 legitimate accounts</b>."
    )
    h(6)

    # Metric cards row
    metrics = [
        ("9,082", "Total Accounts"),
        ("3,924", "Feature Columns"),
        ("81", "Confirmed Mule Accounts"),
        ("0.89%", "Mule Prevalence"),
        ("90", "Fully Complete Columns"),
        ("63", "Entirely Null Columns"),
    ]
    card_w = CW / 3 - 3*mm
    rows_of_cards = [metrics[:3], metrics[3:]]
    for row in rows_of_cards:
        colors_row = [ACCENT, BLUE, TEAL]
        card_row = []
        for i, (v, l) in enumerate(row):
            card_row.append(MetricCard(v, l, color=colors_row[i], w=card_w, h=26*mm))
        card_table = Table([card_row], colWidths=[card_w + 3*mm]*3)
        card_table.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ALIGN",(0,0),(-1,-1),"CENTER")]))
        story.append(card_table)
        h(4)

    h(4)
    sub("Class Imbalance — Critical Finding")
    body(
        "A class imbalance ratio of <b>99.1% : 0.89%</b> is extreme even by fraud detection standards. "
        "Standard accuracy metrics are completely useless here — a model that predicts 'legitimate' for "
        "every account achieves 99.1% accuracy while catching zero frauds. We therefore optimise on "
        "<b>Precision-Recall AUC</b> and <b>F-beta (β=2) score</b>, which penalise missed mule accounts "
        "more heavily than false alarms."
    )
    h(4)

    sub("Missing Value Analysis")
    mv_data = [
        [Paragraph("<b>Category</b>", S["table_header"]),
         Paragraph("<b>Count</b>", S["table_header"]),
         Paragraph("<b>Action</b>", S["table_header"]),
         Paragraph("<b>Rationale</b>", S["table_header"])],
        [Paragraph("Entirely null columns (100% missing)", S["table_cell"]),
         Paragraph("63 cols", S["table_cell"]),
         Paragraph("Drop immediately", S["table_cell"]),
         Paragraph("Zero information content", S["table_cell"])],
        [Paragraph("F3889, F3891 (highlighted, 100% null)", S["table_cell"]),
         Paragraph("2 cols", S["table_cell"]),
         Paragraph("Drop immediately", S["table_cell"]),
         Paragraph("Listed as important but entirely empty", S["table_cell"])],
        [Paragraph(">64% missing (e.g. F3043)", S["table_cell"]),
         Paragraph("~40 cols", S["table_cell"]),
         Paragraph("Drop or binary flag", S["table_cell"]),
         Paragraph("Too sparse for reliable imputation", S["table_cell"])],
        [Paragraph("Partially missing (<30%)", S["table_cell"]),
         Paragraph("~3,700 cols", S["table_cell"]),
         Paragraph("Median impute + missing flag", S["table_cell"]),
         Paragraph("Missingness itself is a fraud signal", S["table_cell"])],
        [Paragraph("Complete columns (0% missing)", S["table_cell"]),
         Paragraph("90 cols", S["table_cell"]),
         Paragraph("Use as-is", S["table_cell"]),
         Paragraph("High reliability features", S["table_cell"])],
    ]
    t = Table(mv_data, colWidths=[55*mm, 22*mm, 40*mm, 63*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLUE),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(8)

    sub("Key Feature Signals — Highlighted Features vs Target")
    body(
        "The bank-specified highlighted features were analysed for mean separation between mule (1) "
        "and legitimate (0) accounts. Three features showed statistically significant separation:"
    )
    h(4)
    sig_data = [
        [Paragraph("<b>Feature</b>", S["table_header"]),
         Paragraph("<b>Legit Mean</b>", S["table_header"]),
         Paragraph("<b>Mule Mean</b>", S["table_header"]),
         Paragraph("<b>Signal Strength</b>", S["table_header"]),
         Paragraph("<b>Interpretation</b>", S["table_header"])],
        [Paragraph("F2678", S["table_cell"]),
         Paragraph("352.1", S["table_cell"]),
         Paragraph("11.4", S["table_cell"]),
         Paragraph("🚨 VERY STRONG", S["table_cell"]),
         Paragraph("Mules show ~30x lower value — likely transaction frequency metric", S["table_cell"])],
        [Paragraph("F3836", S["table_cell"]),
         Paragraph("-49M", S["table_cell"]),
         Paragraph("+1.5M", S["table_cell"]),
         Paragraph("🚨 VERY STRONG", S["table_cell"]),
         Paragraph("Massive sign flip — likely net balance or flow indicator", S["table_cell"])],
        [Paragraph("F670", S["table_cell"]),
         Paragraph("0.09", S["table_cell"]),
         Paragraph("0.23", S["table_cell"]),
         Paragraph("✅ STRONG", S["table_cell"]),
         Paragraph("Mules ~2.6x higher — possibly ratio-based fraud indicator", S["table_cell"])],
        [Paragraph("F2956", S["table_cell"]),
         Paragraph("133.5", S["table_cell"]),
         Paragraph("58.4", S["table_cell"]),
         Paragraph("✅ STRONG", S["table_cell"]),
         Paragraph("Clear separation — likely transaction volume metric", S["table_cell"])],
        [Paragraph("F1692", S["table_cell"]),
         Paragraph("0.26", S["table_cell"]),
         Paragraph("0.11", S["table_cell"]),
         Paragraph("✅ MODERATE", S["table_cell"]),
         Paragraph("Mules ~2x lower — could indicate account age ratio", S["table_cell"])],
    ]
    t = Table(sig_data, colWidths=[18*mm, 22*mm, 22*mm, 33*mm, 85*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(PageBreak())

    # ── SECTION 03 — DATA PREPROCESSING ──────────────────────────────────────
    sec("03", "DATA PREPROCESSING STRATEGY", colors.HexColor("#1A3A6B"))
    body(
        "With 3,924 features and extreme missingness, preprocessing is the most critical phase. "
        "A wrong move here — like imputing before creating missing flags, or not dropping dead columns — "
        "corrupts every downstream step. Our pipeline follows a strict ordered sequence:"
    )
    h(6)

    steps = [
        (1, "Drop Dead Columns", "Remove 63 entirely-null cols + F3889, F3891 (100% null highlighted features)", ACCENT),
        (2, "Create Missing Flags", "BEFORE imputation: create binary col missing_FX=1 for cols >5% null — missingness is a fraud signal", TEAL),
        (3, "Variance Filtering", "Drop near-zero variance features (threshold=0.01). Reduces ~3,924 → ~800 meaningful features", BLUE),
        (4, "Median Imputation", "Impute remaining nulls with column median. Robust to outliers vs mean imputation", BLUE),
        (5, "Outlier Winsorisation", "Cap extreme values at 1st/99th percentile. Prevents ratio features from corrupting model", GOLD),
        (6, "Categorical Encoding", "F3889/F3891 dropped. Remaining str-type features: label encode or OHE", MUTED),
        (7, "Feature Selection — Round 1", "Correlation-based: drop one from any pair with |r| > 0.95 to remove redundancy", BLUE),
        (8, "Stratified Train/Test Split", "80/20 split with stratify=y. Preserves the 0.89% mule ratio in both sets", NAVY),
        (9, "SMOTE Oversampling", "Apply SMOTE only on training set — oversample minority to 1:10 ratio. NEVER on test set", ACCENT),
        (10, "Feature Selection — Round 2", "Post-SMOTE: XGBoost feature importance → keep top 100–200 features for final model", TEAL),
    ]
    for num, title, desc, color in steps:
        story.append(PipelineStep(num, title, desc, color, CW))
        h(2)

    h(6)
    story.append(AlertBox(
        "Critical: SMOTE must only be applied to training data. Applying it before splitting causes data leakage and inflates metrics.",
        "!", ACCENT, CW, 28
    ))
    h(4)
    story.append(AlertBox(
        "Missing value flags must be created BEFORE imputation. Post-imputation you lose the signal that the value was absent.",
        "!", GOLD, CW, 28
    ))
    h(8)

    sub("Handling the Two Categorical Features (F3889, F3891)")
    body(
        "Both F3889 and F3891 are listed as highlighted features by the bank, yet our EDA reveals "
        "they are <b>100% null</b> — every single value in the dataset is missing. These columns "
        "are dropped entirely with no imputation attempted. This is an important finding to highlight "
        "in the submission: the bank's own feature list contains two uninformative columns, "
        "demonstrating the value of rigorous EDA before modelling."
    )
    story.append(PageBreak())

    # ── SECTION 04 — FEATURE ENGINEERING ─────────────────────────────────────
    sec("04", "FEATURE ENGINEERING", TEAL)
    body(
        "Beyond the raw features provided, we engineer domain-informed features that encode "
        "behavioural patterns typical of mule accounts: rapid fund movement, short account tenure, "
        "unusual transaction velocity, and deviation from peer-group norms."
    )
    h(6)

    fe_data = [
        [Paragraph("<b>Feature</b>", S["table_header"]),
         Paragraph("<b>Formula / Logic</b>", S["table_header"]),
         Paragraph("<b>Mule Signal</b>", S["table_header"])],
        [Paragraph("CREDIT_DEBIT_RATIO", S["table_cell"]),
         Paragraph("Total credits / Total debits in window", S["table_cell"]),
         Paragraph("Mules show near 1:1 ratio — quick in/out", S["table_cell"])],
        [Paragraph("VELOCITY_7D", S["table_cell"]),
         Paragraph("Transaction count in last 7 days", S["table_cell"]),
         Paragraph("Sudden spike in activity is a red flag", S["table_cell"])],
        [Paragraph("PEER_DEVIATION_SCORE", S["table_cell"]),
         Paragraph("(account_mean - segment_mean) / segment_std", S["table_cell"]),
         Paragraph("Mules deviate significantly from peer group", S["table_cell"])],
        [Paragraph("DORMANCY_BURST_FLAG", S["table_cell"]),
         Paragraph("1 if 60+ day gap followed by high-volume activity", S["table_cell"]),
         Paragraph("Classic mule account pattern", S["table_cell"])],
        [Paragraph("CHANNEL_DIVERSITY", S["table_cell"]),
         Paragraph("Unique channels used / total transactions", S["table_cell"]),
         Paragraph("Mules often use single channel for layering", S["table_cell"])],
        [Paragraph("ROUND_AMT_RATIO", S["table_cell"]),
         Paragraph("% transactions with round amounts (e.g. 5000, 10000)", S["table_cell"]),
         Paragraph("Structured deposits typical in mule activity", S["table_cell"])],
        [Paragraph("F2678_ZSCORE", S["table_cell"]),
         Paragraph("(F2678 - mean) / std — normalised version", S["table_cell"]),
         Paragraph("Enhances strong separator identified in EDA", S["table_cell"])],
        [Paragraph("F3836_SIGN_FLAG", S["table_cell"]),
         Paragraph("1 if F3836 > 0, else 0", S["table_cell"]),
         Paragraph("Captures the massive sign-flip observed between classes", S["table_cell"])],
    ]
    t = Table(fe_data, colWidths=[48*mm, 70*mm, 62*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TEAL),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(8)

    sub("Feature Selection Strategy")
    body(
        "Starting with ~3,924 features is computationally infeasible for most ML models and risks "
        "overfitting, especially with only 81 positive samples. Our two-stage selection approach:"
    )
    h(3)
    bullet("<b>Stage 1 — Filter methods:</b> Variance threshold (remove constants), correlation filter (remove redundant pairs), univariate statistical test (chi2 / Mann-Whitney U for each feature vs target)")
    bullet("<b>Stage 2 — Embedded selection:</b> Train a preliminary XGBoost on the filtered set, extract feature importances, retain top 150–200 features for the final model")
    bullet("<b>Validation:</b> Cross-validate with the selected feature set to confirm no information leakage from the selection process")
    story.append(PageBreak())

    # ── SECTION 05 — ML PIPELINE ──────────────────────────────────────────────
    sec("05", "ML PIPELINE — END-TO-END", NAVY)
    body(
        "The complete SentinelAI pipeline is structured as a reproducible, modular workflow. "
        "Each stage is independently testable and designed to fail loudly on data quality issues "
        "rather than silently producing unreliable outputs."
    )
    h(6)

    pipeline_steps = [
        ("INGEST", "Load DataSet.csv → validate shape (9082×3925), check F3924 target exists"),
        ("EDA", "Class balance, missing %, feature distributions, highlighted feature analysis"),
        ("PREPROCESS", "Drop nulls → variance filter → impute → winsorise → encode"),
        ("ENGINEER", "Create 8 domain features (velocity, deviation, burst flags, ratios)"),
        ("SPLIT", "Stratified 80/20 → X_train (7265), X_test (1817), preserve 0.89% ratio"),
        ("BALANCE", "SMOTE on X_train only → target ~1:10 mule:legit ratio in training"),
        ("SELECT", "XGBoost preliminary → top 150 features by importance score"),
        ("TRAIN", "XGBoost (champion) + Isolation Forest (unsupervised) — parallel training"),
        ("TUNE", "RandomizedSearchCV 50 iter, 5-fold stratified CV, optimise PR-AUC"),
        ("EVALUATE", "PR-AUC, F-beta(2), KS statistic, confusion matrix on held-out test set"),
        ("EXPLAIN", "SHAP TreeExplainer → global summary plot + local force plot per account"),
        ("SCORE", "Output risk score 0–100 + decision band + top-3 SHAP reasons per account"),
    ]

    col_a = []
    col_b = []
    for i, (stage, desc) in enumerate(pipeline_steps):
        col = col_a if i % 2 == 0 else col_b
        bg = CARD_BG if i % 2 == 0 else WHITE
        col.append(
            Table([[
                Paragraph(f"<b>{stage}</b>", S["body_bold"]),
                Paragraph(desc, S["body"])
            ]], colWidths=[22*mm, 60*mm],
            style=TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), bg),
                ("TOPPADDING", (0,0), (-1,-1), 5),
                ("BOTTOMPADDING", (0,0), (-1,-1), 5),
                ("LEFTPADDING", (0,0), (-1,-1), 5),
                ("LINEBELOW", (0,0), (-1,-1), 0.3, MID_BG),
            ]))
        )

    half = CW/2 - 3*mm
    for i in range(0, len(pipeline_steps), 2):
        left_item = [pipeline_steps[i]]
        right_item = [pipeline_steps[i+1]] if i+1 < len(pipeline_steps) else [("", "")]
        row_tbl = Table([[
            _make_step_cell(left_item[0][0], left_item[0][1], i, half),
            _make_step_cell(right_item[0][0], right_item[0][1], i+1, half) if right_item[0][0] else Spacer(1,1)
        ]], colWidths=[half + 3*mm, half + 3*mm])
        row_tbl.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP")]))
        story.append(row_tbl)
        h(3)

    story.append(PageBreak())

    # ── SECTION 06 — MODEL ARCHITECTURE ──────────────────────────────────────
    sec("06", "MODEL ARCHITECTURE", ACCENT)
    sub("Champion Model — XGBoost Classifier")
    body(
        "XGBoost is the primary classification model. Its gradient boosting framework handles "
        "tabular financial data exceptionally well, naturally accommodating the high feature count "
        "and extreme class imbalance through the <b>scale_pos_weight</b> parameter."
    )
    h(4)

    xgb_params = [
        [Paragraph("<b>Hyperparameter</b>", S["table_header"]),
         Paragraph("<b>Value</b>", S["table_header"]),
         Paragraph("<b>Reasoning</b>", S["table_header"])],
        [Paragraph("n_estimators", S["table_cell"]), Paragraph("500–1000", S["table_cell"]),
         Paragraph("With early stopping, more trees = safer ceiling", S["table_cell"])],
        [Paragraph("max_depth", S["table_cell"]), Paragraph("4–6", S["table_cell"]),
         Paragraph("Shallow trees reduce overfitting on small positive class", S["table_cell"])],
        [Paragraph("learning_rate", S["table_cell"]), Paragraph("0.01–0.05", S["table_cell"]),
         Paragraph("Low LR + more trees = better generalisation", S["table_cell"])],
        [Paragraph("scale_pos_weight", S["table_cell"]), Paragraph("~111 (9001/81)", S["table_cell"]),
         Paragraph("Direct imbalance compensation — mule samples weighted 111x", S["table_cell"])],
        [Paragraph("subsample", S["table_cell"]), Paragraph("0.7–0.8", S["table_cell"]),
         Paragraph("Row sampling reduces overfitting", S["table_cell"])],
        [Paragraph("colsample_bytree", S["table_cell"]), Paragraph("0.6–0.7", S["table_cell"]),
         Paragraph("Column sampling — especially useful with 150+ features", S["table_cell"])],
        [Paragraph("eval_metric", S["table_cell"]), Paragraph("aucpr", S["table_cell"]),
         Paragraph("Precision-Recall AUC — right metric for imbalanced data", S["table_cell"])],
        [Paragraph("early_stopping_rounds", S["table_cell"]), Paragraph("30", S["table_cell"]),
         Paragraph("Halt training when val PR-AUC stops improving", S["table_cell"])],
    ]
    t = Table(xgb_params, colWidths=[48*mm, 35*mm, 97*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), ACCENT),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(8)

    sub("Challenger Layer — Isolation Forest (Unsupervised)")
    body(
        "Alongside XGBoost, we run an <b>Isolation Forest</b> as a parallel unsupervised anomaly "
        "detector. This two-pronged approach is particularly valuable here because with only 81 "
        "confirmed mule accounts, the supervised model may miss genuinely novel mule patterns not "
        "represented in the labelled data. Isolation Forest has no dependency on labels — it flags "
        "accounts that are anomalous relative to the general population."
    )
    h(4)

    arch_data = [
        [Paragraph("<b>Component</b>", S["table_header"]),
         Paragraph("<b>Type</b>", S["table_header"]),
         Paragraph("<b>Output</b>", S["table_header"]),
         Paragraph("<b>Role in Final Decision</b>", S["table_header"])],
        [Paragraph("XGBoost", S["table_cell"]),
         Paragraph("Supervised", S["table_cell"]),
         Paragraph("P(mule) — probability 0–1", S["table_cell"]),
         Paragraph("Primary decision maker (Champion)", S["table_cell"])],
        [Paragraph("Isolation Forest", S["table_cell"]),
         Paragraph("Unsupervised", S["table_cell"]),
         Paragraph("Anomaly score (-1 to 1)", S["table_cell"]),
         Paragraph("Secondary signal — elevates risk score if anomalous", S["table_cell"])],
        [Paragraph("Ensemble Score", S["table_cell"]),
         Paragraph("Fusion", S["table_cell"]),
         Paragraph("Risk Score 0–100", S["table_cell"]),
         Paragraph("0.7 × XGB_prob + 0.3 × IF_norm → final risk score", S["table_cell"])],
    ]
    t = Table(arch_data, colWidths=[35*mm, 28*mm, 45*mm, 72*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(6)

    sub("Class Imbalance Strategy — Detail")
    bullet("<b>scale_pos_weight = 111:</b> Native XGBoost parameter. Each mule training sample contributes 111x the loss of a legitimate sample. No data duplication needed.")
    bullet("<b>SMOTE:</b> Applied after splitting — generates synthetic mule samples in feature space to achieve ~1:10 training ratio. Only on X_train.")
    bullet("<b>Threshold optimisation:</b> Default 0.5 threshold is wrong for imbalanced data. We optimise threshold using F-beta(β=2) on validation set — prioritising recall (catching mules) over precision.")
    story.append(PageBreak())

    # ── SECTION 07 — SHAP EXPLAINABILITY ─────────────────────────────────────
    sec("07", "SHAP EXPLAINABILITY FRAMEWORK", TEAL)
    body(
        "Explainability is non-negotiable in banking fraud detection. Regulators, compliance teams, "
        "and investigating officers need to understand <i>why</i> an account was flagged — not just "
        "<i>that</i> it was flagged. SentinelAI implements a two-layer SHAP architecture aligned with "
        "RBI guidelines on AI explainability in financial services."
    )
    h(6)

    shap_data = [
        [Paragraph("<b>Layer</b>", S["table_header"]),
         Paragraph("<b>Audience</b>", S["table_header"]),
         Paragraph("<b>Output</b>", S["table_header"]),
         Paragraph("<b>Use Case</b>", S["table_header"])],
        [Paragraph("Global SHAP\n(Model-level)", S["table_cell"]),
         Paragraph("Risk officers, Regulators, Model audit", S["table_cell"]),
         Paragraph("SHAP summary bar + beeswarm plot, top 20 features", S["table_cell"]),
         Paragraph("Model validation, regulatory submission, feature importance reporting", S["table_cell"])],
        [Paragraph("Local SHAP\n(Account-level)", S["table_cell"]),
         Paragraph("Investigators, Branch managers, Compliance", S["table_cell"]),
         Paragraph("Force plot + waterfall chart, top 5 drivers per account", S["table_cell"]),
         Paragraph("SAR drafting, account freeze justification, customer communication", S["table_cell"])],
    ]
    t = Table(shap_data, colWidths=[35*mm, 48*mm, 60*mm, 37*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), TEAL),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(8)

    sub("Sample Alert Explanation (Local SHAP Output)")
    body("For Account ID #4721 — Risk Score: <b>87/100</b> — Decision: <b>HIGH RISK / FLAG FOR SAR</b>")
    h(4)

    shap_example = [
        [Paragraph("<b>Feature</b>", S["table_header"]),
         Paragraph("<b>Account Value</b>", S["table_header"]),
         Paragraph("<b>SHAP Impact</b>", S["table_header"]),
         Paragraph("<b>Direction</b>", S["table_header"]),
         Paragraph("<b>Plain English</b>", S["table_header"])],
        [Paragraph("F2678", S["table_cell"]), Paragraph("3.2", S["table_cell"]),
         Paragraph("+0.41", S["table_cell"]), Paragraph("↑ Raises risk", S["table_cell"]),
         Paragraph("Value far below legitimate account norm (352)", S["table_cell"])],
        [Paragraph("F3836_SIGN_FLAG", S["table_cell"]), Paragraph("1 (positive)", S["table_cell"]),
         Paragraph("+0.29", S["table_cell"]), Paragraph("↑ Raises risk", S["table_cell"]),
         Paragraph("Positive F3836 sign — unusual for legitimate accounts", S["table_cell"])],
        [Paragraph("DORMANCY_BURST_FLAG", S["table_cell"]), Paragraph("1", S["table_cell"]),
         Paragraph("+0.22", S["table_cell"]), Paragraph("↑ Raises risk", S["table_cell"]),
         Paragraph("Account dormant 73 days, then sudden high-volume activity", S["table_cell"])],
        [Paragraph("F670", S["table_cell"]), Paragraph("0.61", S["table_cell"]),
         Paragraph("+0.17", S["table_cell"]), Paragraph("↑ Raises risk", S["table_cell"]),
         Paragraph("Value 6.7x above legitimate account mean (0.09)", S["table_cell"])],
        [Paragraph("F1692", S["table_cell"]), Paragraph("0.04", S["table_cell"]),
         Paragraph("+0.09", S["table_cell"]), Paragraph("↑ Raises risk", S["table_cell"]),
         Paragraph("Below typical legitimate range — possibly new account", S["table_cell"])],
    ]
    t = Table(shap_example, colWidths=[35*mm, 28*mm, 22*mm, 28*mm, 67*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#0A5C52")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(PageBreak())

    # ── SECTION 08 — RISK SCORING ─────────────────────────────────────────────
    sec("08", "RISK SCORING & ALERT GENERATION", GOLD)
    body(
        "Raw model probabilities are converted into a 0–100 Risk Score and mapped to actionable "
        "decision bands. This replaces binary flags with graduated responses — reducing alert fatigue "
        "while ensuring high-risk accounts receive immediate attention."
    )
    h(6)

    bands_data = [
        [Paragraph("<b>Risk Band</b>", S["table_header"]),
         Paragraph("<b>Score Range</b>", S["table_header"]),
         Paragraph("<b>Action</b>", S["table_header"]),
         Paragraph("<b>SLA</b>", S["table_header"]),
         Paragraph("<b>Escalation</b>", S["table_header"])],
        [Paragraph("🟢  LOW RISK", S["table_cell"]), Paragraph("0–35", S["table_cell"]),
         Paragraph("No action — standard monitoring", S["table_cell"]),
         Paragraph("None", S["table_cell"]), Paragraph("None", S["table_cell"])],
        [Paragraph("🟡  MEDIUM RISK", S["table_cell"]), Paragraph("36–60", S["table_cell"]),
         Paragraph("Enhanced monitoring — flag for weekly review", S["table_cell"]),
         Paragraph("7 days", S["table_cell"]), Paragraph("Team lead review", S["table_cell"])],
        [Paragraph("🟠  HIGH RISK", S["table_cell"]), Paragraph("61–80", S["table_cell"]),
         Paragraph("Soft block — restrict large outward transactions", S["table_cell"]),
         Paragraph("48 hours", S["table_cell"]), Paragraph("Risk officer review", S["table_cell"])],
        [Paragraph("🔴  CRITICAL", S["table_cell"]), Paragraph("81–100", S["table_cell"]),
         Paragraph("Auto-generate SAR + account freeze recommendation", S["table_cell"]),
         Paragraph("4 hours", S["table_cell"]), Paragraph("Immediate — MLRO", S["table_cell"])],
    ]
    t = Table(bands_data, colWidths=[32*mm, 28*mm, 65*mm, 22*mm, 33*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#8B5E00")),
        ("BACKGROUND", (0,1), (-1,1), colors.HexColor("#E8F5E9")),
        ("BACKGROUND", (0,2), (-1,2), colors.HexColor("#FFFDE7")),
        ("BACKGROUND", (0,3), (-1,3), colors.HexColor("#FFF3E0")),
        ("BACKGROUND", (0,4), (-1,4), colors.HexColor("#FFEBEE")),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    h(8)

    sub("Alert Output Schema (per account)")
    code('{')
    code('  "account_id": "ACC_4721",')
    code('  "risk_score": 87,')
    code('  "decision": "CRITICAL",')
    code('  "auto_sar": true,')
    code('  "xgb_probability": 0.79,')
    code('  "isolation_forest_flag": true,')
    code('  "top_3_reasons": [')
    code('    {"feature": "F2678", "impact": "+0.41", "direction": "risk_increase"},')
    code('    {"feature": "F3836_SIGN_FLAG", "impact": "+0.29", "direction": "risk_increase"},')
    code('    {"feature": "DORMANCY_BURST_FLAG", "impact": "+0.22", "direction": "risk_increase"}')
    code('  ],')
    code('  "model_version": "sentinel_v1.0",')
    code('  "inference_time_ms": 8.3')
    code('}')
    story.append(PageBreak())

    # ── SECTION 09 — EXPECTED RESULTS ─────────────────────────────────────────
    sec("09", "EXPECTED RESULTS & BENCHMARKS", BLUE)
    body(
        "The following benchmarks are projected based on comparable fraud detection tasks with "
        "similar class imbalance ratios in published literature and Kaggle competition results. "
        "Actual results will depend on final feature selection and hyperparameter tuning."
    )
    h(6)

    results_data = [
        [Paragraph("<b>Metric</b>", S["table_header"]),
         Paragraph("<b>Target</b>", S["table_header"]),
         Paragraph("<b>Why This Metric</b>", S["table_header"]),
         Paragraph("<b>Baseline (Random)</b>", S["table_header"])],
        [Paragraph("PR-AUC (Primary)", S["table_cell"]),
         Paragraph("> 0.55", S["table_cell"]),
         Paragraph("Best metric for imbalanced binary classification", S["table_cell"]),
         Paragraph("0.009 (prevalence)", S["table_cell"])],
        [Paragraph("F-beta (β=2) Score", S["table_cell"]),
         Paragraph("> 0.60", S["table_cell"]),
         Paragraph("Weighs recall 2x more than precision — catching mules > false alarms", S["table_cell"]),
         Paragraph("~0.02", S["table_cell"])],
        [Paragraph("Recall (Sensitivity)", S["table_cell"]),
         Paragraph("> 0.75", S["table_cell"]),
         Paragraph("We must catch 75%+ of actual mule accounts", S["table_cell"]),
         Paragraph("0.009", S["table_cell"])],
        [Paragraph("Precision at threshold", S["table_cell"]),
         Paragraph("> 0.40", S["table_cell"]),
         Paragraph("< 60% false alarm rate for operational feasibility", S["table_cell"]),
         Paragraph("0.009", S["table_cell"])],
        [Paragraph("KS Statistic", S["table_cell"]),
         Paragraph("> 0.50", S["table_cell"]),
         Paragraph("Separation between mule and legit score distributions", S["table_cell"]),
         Paragraph("~0.00", S["table_cell"])],
        [Paragraph("ROC-AUC (Secondary)", S["table_cell"]),
         Paragraph("> 0.85", S["table_cell"]),
         Paragraph("Useful for stakeholder reporting (not primary metric)", S["table_cell"]),
         Paragraph("0.50", S["table_cell"])],
        [Paragraph("Inference Latency", S["table_cell"]),
         Paragraph("< 10ms / account", S["table_cell"]),
         Paragraph("Real-time scoring feasibility", S["table_cell"]),
         Paragraph("N/A", S["table_cell"])],
    ]
    t = Table(results_data, colWidths=[40*mm, 22*mm, 82*mm, 36*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), BLUE),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(6)

    story.append(AlertBox(
        "ROC-AUC alone is misleading here. A model predicting all-legitimate gets ROC-AUC ~0.5 but catches 0 mules. PR-AUC is the honest metric.",
        "!", ACCENT, CW, 28
    ))
    story.append(PageBreak())

    # ── SECTION 10 — REGULATORY COMPLIANCE ───────────────────────────────────
    sec("10", "REGULATORY COMPLIANCE", NAVY)
    body(
        "SentinelAI is designed with Indian banking regulatory requirements as first-class constraints, "
        "not afterthoughts. The following frameworks directly govern mule account detection and "
        "suspicious transaction reporting in India."
    )
    h(6)

    reg_data = [
        [Paragraph("<b>Regulation</b>", S["table_header"]),
         Paragraph("<b>Key Requirement</b>", S["table_header"]),
         Paragraph("<b>How SentinelAI Complies</b>", S["table_header"])],
        [Paragraph("PMLA 2002\n(Prevention of Money\nLaundering Act)", S["table_cell"]),
         Paragraph("Banks must file SARs / STRs for suspicious transactions within prescribed timelines", S["table_cell"]),
         Paragraph("Auto-SAR generation for CRITICAL band accounts. Risk score + SHAP reasons form the SAR evidence package", S["table_cell"])],
        [Paragraph("RBI Master Direction\non KYC (2016)", S["table_cell"]),
         Paragraph("Customer Due Diligence, Enhanced Due Diligence for high-risk accounts", S["table_cell"]),
         Paragraph("Risk score bands trigger EDD workflow. Every score logged with timestamp, model version, feature drivers", S["table_cell"])],
        [Paragraph("RBI Circular on\nCyber Fraud (2023)", S["table_cell"]),
         Paragraph("Real-time monitoring of mule accounts used in cyber fraud", S["table_cell"]),
         Paragraph("Isolation Forest provides unsupervised real-time anomaly detection without label dependency", S["table_cell"])],
        [Paragraph("FATF Recommendation 16\n(Wire Transfers)", S["table_cell"]),
         Paragraph("Monitor fund movements for money laundering patterns", S["table_cell"]),
         Paragraph("CREDIT_DEBIT_RATIO and VELOCITY_7D features directly encode layering patterns", S["table_cell"])],
        [Paragraph("RBI AI/ML Guidelines\nfor BFSI (2024)", S["table_cell"]),
         Paragraph("AI models must be explainable and auditable", S["table_cell"]),
         Paragraph("TreeSHAP produces deterministic, reproducible explanations. 7-year audit log retention built into alert schema", S["table_cell"])],
    ]
    t = Table(reg_data, colWidths=[40*mm, 65*mm, 75*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    story.append(PageBreak())

    # ── SECTION 11 — LIMITATIONS ──────────────────────────────────────────────
    sec("11", "LIMITATIONS & FUTURE WORK", MUTED)
    body(
        "We believe intellectual honesty about limitations strengthens rather than weakens a submission. "
        "The following are genuine constraints of the current approach that would need to be addressed "
        "before production deployment."
    )
    h(6)

    lim_data = [
        [Paragraph("<b>Limitation</b>", S["table_header"]),
         Paragraph("<b>Current State</b>", S["table_header"]),
         Paragraph("<b>Production Solution</b>", S["table_header"])],
        [Paragraph("Only 81 labelled mule accounts", S["table_cell"]),
         Paragraph("Small positive class limits model confidence. SHAP values may shift with more data", S["table_cell"]),
         Paragraph("Active learning: flag model-uncertain accounts for analyst review → expand labelled set", S["table_cell"])],
        [Paragraph("Feature anonymisation", S["table_cell"]),
         Paragraph("F1–F3924 labels prevent domain-informed feature engineering beyond the 18 highlighted features", S["table_cell"]),
         Paragraph("With real column names, richer velocity/ratio features become possible", S["table_cell"])],
        [Paragraph("No temporal dimension", S["table_cell"]),
         Paragraph("Dataset appears cross-sectional. No time-series or sequential transaction patterns exploited", S["table_cell"]),
         Paragraph("Sequence models (LSTM, Transformer) on transaction logs for temporal pattern detection", S["table_cell"])],
        [Paragraph("3,772 partially null columns", S["table_cell"]),
         Paragraph("Median imputation is a simplification. Missing pattern may encode richer information", S["table_cell"]),
         Paragraph("Multiple imputation (MICE) or learned missingness embeddings in production", S["table_cell"])],
        [Paragraph("No network/graph features", S["table_cell"]),
         Paragraph("Mule accounts often form rings. Account-to-account transfer graph not utilised", S["table_cell"]),
         Paragraph("Graph Neural Networks on transaction network for community-level mule ring detection", S["table_cell"])],
    ]
    t = Table(lim_data, colWidths=[42*mm, 67*mm, 71*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), MUTED),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CARD_BG, WHITE]),
        ("GRID", (0,0), (-1,-1), 0.4, MID_BG),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
    ]))
    story.append(t)
    h(8)

    sub("Future Roadmap")
    bullet("<b>Phase 2:</b> Graph Neural Network layer — model account-to-account transfer networks to detect mule rings, not just individual accounts")
    bullet("<b>Phase 2:</b> Real-time streaming pipeline (Kafka + online XGBoost) for transaction-level scoring rather than account-level")
    bullet("<b>Phase 3:</b> Federated learning across BOI branches — train on distributed data without centralising sensitive transaction records")
    bullet("<b>Phase 3:</b> LLM-generated SAR narrative — use SHAP explanations + account metadata to auto-draft SAR text for officer review")

    h(10)
    # Closing box
    close_tbl = Table([[
        Paragraph(
            "<b>SentinelAI</b> — Built for the Bank of India Cyber Fraud Prevention Hackathon 2025.<br/>"
            "XGBoost Champion · Isolation Forest · TreeSHAP · PMLA/RBI Compliant · Risk Score Bands",
            ParagraphStyle("closing", fontName="Helvetica", fontSize=9, textColor=WHITE,
                           leading=14, alignment=TA_CENTER)
        )
    ]], colWidths=[CW])
    close_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NAVY),
        ("TOPPADDING", (0,0), (-1,-1), 12),
        ("BOTTOMPADDING", (0,0), (-1,-1), 12),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(close_tbl)

    # ── BUILD ─────────────────────────────────────────────────────────────────
    doc.build(
        story,
        onFirstPage=build_cover,
        onLaterPages=on_later_page
    )
    print(f"PDF written → {path}")

def _make_step_cell(stage, desc, i, w):
    bg = CARD_BG if i % 2 == 0 else WHITE
    if not stage:
        return Spacer(w, 30)
    return Table([[
        Paragraph(f"<b>{stage}</b>", ParagraphStyle("sh", fontName="Helvetica-Bold",
            fontSize=9, textColor=ACCENT, leading=12)),
        Paragraph(desc, ParagraphStyle("sd", fontName="Helvetica", fontSize=8.5,
            textColor=DARK_TEXT, leading=12))
    ]], colWidths=[24*mm, w - 24*mm - 3*mm],
    style=TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING", (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("LINEBELOW", (0,0), (-1,-1), 0.3, MID_BG),
    ]))

if __name__ == "__main__":
    build()