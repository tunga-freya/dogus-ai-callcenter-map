#!/usr/bin/env python3
"""
Doğuş Otomotiv x Freya Labs — Call Center AI Operating Model
Single SVG, monochrome blueprint aesthetic, dense and data-heavy.
Designed to read like a senior consultant's deliverable, not a presentation.
"""

W, H = 3600, 4400
PAD = 80

# Palette — restrained, two ink colors only
PAPER = "#fbfbf7"
INK = "#111111"
NAVY = "#1c2c4a"
GRAY = "#5a5a5a"
LIGHT = "#9a9a9a"
LINE = "#cfcec8"
SOFT = "#f0efe8"
HEAVY = "#e3e2dc"
RED = "#7a1a1a"

# Typography
SERIF = "'Source Serif Pro', 'EB Garamond', 'Georgia', 'Times New Roman', serif"
SANS = "'Inter', 'Helvetica Neue', 'Arial', sans-serif"
MONO = "'IBM Plex Mono', 'Menlo', 'Consolas', monospace"

out = []
def w(s): out.append(s)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# Header
w('<?xml version="1.0" encoding="UTF-8"?>')
w(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{SANS}">')
w('<defs>')
w('<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">')
w(f'  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{HEAVY}" stroke-width="0.4"/>')
w('</pattern>')
w('</defs>')

# Paper background
w(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
# very faint grid
w(f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.6"/>')
# Margin frame
w(f'<rect x="40" y="40" width="{W-80}" height="{H-80}" fill="none" stroke="{INK}" stroke-width="1.5"/>')
w(f'<rect x="50" y="50" width="{W-100}" height="{H-100}" fill="none" stroke="{INK}" stroke-width="0.5"/>')

# ===================== Title block =====================
ty = 130
w(f'<text x="{PAD}" y="{ty}" fill="{INK}" font-family="{SERIF}" font-size="22" font-weight="600" letter-spacing="6">CONFIDENTIAL · FOR DOĞUŞ OTOMOTİV LEADERSHIP REVIEW</text>')
w(f'<line x1="{PAD}" y1="{ty+24}" x2="{W-PAD}" y2="{ty+24}" stroke="{INK}" stroke-width="1"/>')

ty = 220
w(f'<text x="{PAD}" y="{ty}" fill="{INK}" font-family="{SERIF}" font-size="76" font-weight="700">Call Center AI Operating Model</text>')
w(f'<text x="{PAD}" y="{ty+62}" fill="{NAVY}" font-family="{SERIF}" font-size="42" font-weight="500" font-style="italic">A 12-month transformation blueprint for the multi-brand contact center</text>')

# Sub-meta line
mty = 360
w(f'<line x1="{PAD}" y1="{mty}" x2="{W-PAD}" y2="{mty}" stroke="{INK}" stroke-width="0.5"/>')
meta = [
    ("CLIENT", "Doğuş Otomotiv"),
    ("BRANDS", "Volkswagen · Audi · Škoda · SEAT · Porsche · Bentley · Lamborghini"),
    ("PREPARED BY", "Freya Labs, ML Performance & Voice"),
    ("REVISION", "1.1 · April 2026"),
]
mx = PAD
for i, (k, v) in enumerate(meta):
    w(f'<text x="{mx}" y="{mty+30}" fill="{LIGHT}" font-family="{SANS}" font-size="13" letter-spacing="2.5" font-weight="600">{k}</text>')
    w(f'<text x="{mx}" y="{mty+58}" fill="{INK}" font-family="{SANS}" font-size="20" font-weight="500">{esc(v)}</text>')
    if i < len(meta) - 1:
        # vertical separator
        sep_x = mx + (260 if i == 0 else 760 if i == 1 else 360)
        w(f'<line x1="{sep_x}" y1="{mty+10}" x2="{sep_x}" y2="{mty+70}" stroke="{LINE}" stroke-width="0.5"/>')
        mx = sep_x + 30
w(f'<line x1="{PAD}" y1="{mty+90}" x2="{W-PAD}" y2="{mty+90}" stroke="{INK}" stroke-width="0.5"/>')

# ===================== Section helper =====================
def sec_header(y, num, title, subtitle):
    w(f'<text x="{PAD}" y="{y}" fill="{NAVY}" font-family="{SERIF}" font-size="64" font-weight="700">{num}</text>')
    w(f'<text x="{PAD+110}" y="{y}" fill="{INK}" font-family="{SERIF}" font-size="40" font-weight="600">{title}</text>')
    w(f'<text x="{PAD+110}" y="{y+34}" fill="{GRAY}" font-family="{SERIF}" font-size="22" font-style="italic">{subtitle}</text>')
    w(f'<line x1="{PAD}" y1="{y+62}" x2="{W-PAD}" y2="{y+62}" stroke="{INK}" stroke-width="0.5"/>')

# ===================== 01 — Engagement frame =====================
y_cur = 540
sec_header(y_cur, "01", "Engagement Frame", "Scope, baseline, and the one-line thesis we are testing.")

ey = y_cur + 100
# Two columns: thesis (left, larger), facts (right)
w(f'<text x="{PAD}" y="{ey+20}" fill="{LIGHT}" font-family="{SANS}" font-size="13" letter-spacing="2.5" font-weight="600">THESIS</text>')
w(f'<text x="{PAD}" y="{ey+72}" fill="{INK}" font-family="{SERIF}" font-size="38" font-weight="500" font-style="italic">A specialized voice agent layered on top of the existing</text>')
w(f'<text x="{PAD}" y="{ey+118}" fill="{INK}" font-family="{SERIF}" font-size="38" font-weight="500" font-style="italic">contact center can absorb 70% of inbound volume in 12 months,</text>')
w(f'<text x="{PAD}" y="{ey+164}" fill="{INK}" font-family="{SERIF}" font-size="38" font-weight="500" font-style="italic">while lifting service-channel revenue by 22% via outbound automation,</text>')
w(f'<text x="{PAD}" y="{ey+210}" fill="{INK}" font-family="{SERIF}" font-size="38" font-weight="500" font-style="italic">at a 45% lower cost-to-serve and without dealer disruption.</text>')

# right facts column
fx = W - PAD - 1100
w(f'<text x="{fx}" y="{ey+20}" fill="{LIGHT}" font-family="{SANS}" font-size="13" letter-spacing="2.5" font-weight="600">BASELINE FACTS (FY 2025)</text>')
facts = [
    ("Inbound calls / year, group-wide", "≈ 12.4 million"),
    ("Inbound calls / year, service-only", "≈ 6.8 million"),
    ("Outbound calls / year (NPS, recall, reminder)", "≈ 2.1 million"),
    ("Live agents / FTEs (in-house + dealer BDC)", "≈ 1{,}450"),
    ("Average inbound handle time, all intents", "4 min 12 sec"),
    ("Service-appointment requests / year", "≈ 3.1 million"),
    ("Roadside / emergency calls / year", "≈ 380{,}000"),
    ("Active recall campaigns Q1 2026", "11"),
]
for i, (k, v) in enumerate(facts):
    yy = ey + 60 + i * 32
    w(f'<text x="{fx}" y="{yy}" fill="{INK}" font-family="{SANS}" font-size="16">{esc(k)}</text>')
    w(f'<text x="{fx+1080}" y="{yy}" fill="{INK}" font-family="{MONO}" font-size="16" font-weight="600" text-anchor="end">{esc(v)}</text>')
    w(f'<line x1="{fx}" y1="{yy+8}" x2="{fx+1080}" y2="{yy+8}" stroke="{LINE}" stroke-width="0.4" stroke-dasharray="2 3"/>')

# ===================== 02 — Operating model diagram =====================
y_cur = 1080
sec_header(y_cur, "02", "Operating Model", "Single horizontal flow from caller to outcome, with the AI tier sitting between the IVR and the dealer DMS.")

dy = y_cur + 130
# Six rectangles in a horizontal chain
nodes = [
    ("CALLER\n(retail / fleet)", "Phone, WhatsApp, App, Web"),
    ("CHANNEL\nGATEWAY", "Cisco UCM · WhatsApp BSP\nSession orchestration"),
    ("INTENT\nROUTER", "Lightweight classifier\nidentifies intent, brand,\nVIP, urgency"),
    ("AI VOICE\nAGENT", "Specialized per use case\nFreya STT/TTS + LLM\n+ tools"),
    ("ACTION\nSYSTEMS", "SAP CRM · Dealer DMS\nService catalogue · Parts API\nRecall registry"),
    ("OUTCOME", "Booking confirmed\nLead captured\nIssue resolved or escalated"),
]
node_w = (W - 2*PAD - 5*32) / 6
node_h = 220
for i, (title, body) in enumerate(nodes):
    x = PAD + i * (node_w + 32)
    w(f'<rect x="{x}" y="{dy}" width="{node_w}" height="{node_h}" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
    w(f'<rect x="{x}" y="{dy}" width="{node_w}" height="50" fill="{NAVY}"/>')
    title_lines = title.split("\n")
    for j, t in enumerate(title_lines):
        w(f'<text x="{x+node_w/2}" y="{dy+22+j*22}" fill="white" font-family="{SANS}" font-size="14" font-weight="700" letter-spacing="1.5" text-anchor="middle">{esc(t)}</text>')
    body_lines = body.split("\n")
    for j, b in enumerate(body_lines):
        w(f'<text x="{x+node_w/2}" y="{dy+92+j*26}" fill="{INK}" font-family="{SANS}" font-size="14" text-anchor="middle">{esc(b)}</text>')
    # arrow to next
    if i < len(nodes) - 1:
        ax = x + node_w
        ay = dy + node_h/2
        w(f'<line x1="{ax}" y1="{ay}" x2="{ax+22}" y2="{ay}" stroke="{INK}" stroke-width="1.5"/>')
        w(f'<polygon points="{ax+22},{ay-6} {ax+32},{ay} {ax+22},{ay+6}" fill="{INK}"/>')

# Decision-fork callout below the AI Voice Agent box
fork_y = dy + node_h + 40
ai_x = PAD + 3 * (node_w + 32) + node_w/2
w(f'<line x1="{ai_x}" y1="{dy+node_h}" x2="{ai_x}" y2="{fork_y+10}" stroke="{INK}" stroke-width="1" stroke-dasharray="3 3"/>')
w(f'<text x="{ai_x}" y="{fork_y+34}" fill="{INK}" font-family="{SERIF}" font-size="18" font-style="italic" text-anchor="middle">If confidence &lt; 70% or sentiment &lt; 0.2 → escalate to live agent</text>')
w(f'<text x="{ai_x}" y="{fork_y+58}" fill="{GRAY}" font-family="{SERIF}" font-size="16" font-style="italic" text-anchor="middle">If KVKK consent missing → route to scripted IVR with operator-only path</text>')
w(f'<text x="{ai_x}" y="{fork_y+82}" fill="{GRAY}" font-family="{SERIF}" font-size="16" font-style="italic" text-anchor="middle">If brand = Porsche / Bentley / Lamborghini → premium voice profile + dedicated queue</text>')

# ===================== 03 — AI agent matrix =====================
y_cur = 1660
sec_header(y_cur, "03", "AI Agent Matrix", "Ten specialized agents. Each owns one intent, end to end.")

ty = y_cur + 110
agents = [
    # name, dir, channel, phase, AHT target, containment, primary KPI, secondary KPI
    ("Service Appointment",      "Inbound",  "Phone, WA, App", "Phase 1", "85 s",  "70%", "Booking conv.",        "Reschedule rate"),
    ("Service Reminder",         "Outbound", "Phone, WA",       "Phase 1", "55 s",  "n/a", "Service revenue",      "Pickup rate"),
    ("NPS / CX Survey",          "Outbound", "Phone, WA",       "Phase 1", "70 s",  "n/a", "Closed-loop CX",       "Detractor follow-up"),
    ("Sales Lead Qualifier",     "Inbound",  "Phone, Web",      "Phase 2", "110 s", "55%", "MQL→SQL conversion",   "Test-drive booked"),
    ("Recall Campaign",          "Outbound", "Phone, SMS",      "Phase 2", "75 s",  "n/a", "Recall completion %",  "OEM compliance"),
    ("Complaint Tier-1",         "Inbound",  "All channels",    "Phase 2", "95 s",  "60%", "Complaints logged %",  "Resolution within SLA"),
    ("Parts Inquiry",            "Inbound",  "Phone, WA",       "Phase 3", "90 s",  "65%", "Order conversion",     "Stock-check accuracy"),
    ("Warranty Renewal",         "Outbound", "Phone, WA",       "Phase 3", "100 s", "n/a", "Renewal rate",         "Extended-warranty upsell"),
    ("Roadside Triage",          "Inbound",  "Phone",           "Phase 4", "65 s",  "40%", "Time-to-dispatch",     "Customer reassurance"),
    ("Insurance Cross-sell",     "Outbound", "Phone, WA",       "Phase 4", "120 s", "n/a", "Bind rate",            "Cross-sell margin"),
]
cols = [
    ("AGENT",            520),
    ("DIRECTION",        180),
    ("CHANNEL",          280),
    ("PHASE",            140),
    ("AHT TARGET",       180),
    ("CONTAINMENT",      200),
    ("PRIMARY KPI",      460),
    ("SECONDARY KPI",    480),
]
total_w = sum(c[1] for c in cols)
# Header row
hx = PAD
w(f'<rect x="{PAD}" y="{ty}" width="{total_w}" height="48" fill="{NAVY}"/>')
cx = hx
for label, cw in cols:
    w(f'<text x="{cx+18}" y="{ty+30}" fill="white" font-family="{SANS}" font-size="13" font-weight="700" letter-spacing="2">{label}</text>')
    cx += cw

# Rows
row_h = 56
for i, row in enumerate(agents):
    ry = ty + 48 + i * row_h
    bg = SOFT if i % 2 == 1 else PAPER
    w(f'<rect x="{PAD}" y="{ry}" width="{total_w}" height="{row_h}" fill="{bg}"/>')
    cx = PAD
    for j, (val, (label, cw)) in enumerate(zip(row, cols)):
        font_w = "600" if j == 0 else "400"
        size = "17" if j == 0 else "16"
        color = INK if j == 0 else GRAY if j in (1, 2, 3) else INK
        w(f'<text x="{cx+18}" y="{ry+34}" fill="{color}" font-family="{SANS}" font-size="{size}" font-weight="{font_w}">{esc(str(val))}</text>')
        cx += cw

# Table border
total_h = 48 + len(agents) * row_h
w(f'<rect x="{PAD}" y="{ty}" width="{total_w}" height="{total_h}" fill="none" stroke="{INK}" stroke-width="1"/>')

# ===================== 04 — Phased rollout (Gantt) =====================
y_cur = ty + total_h + 100
sec_header(y_cur, "04", "Phased Rollout", "Twelve months. Each phase carries a quantified gate before the next opens.")

gy = y_cur + 130
months = list(range(1, 13))
# Gantt grid
left = PAD + 380
right = W - PAD - 200
month_w = (right - left) / 12
# Months header
for i, m in enumerate(months):
    mx = left + i * month_w
    w(f'<line x1="{mx}" y1="{gy-30}" x2="{mx}" y2="{gy + 9*44 + 10}" stroke="{LINE}" stroke-width="0.4"/>')
    w(f'<text x="{mx + month_w/2}" y="{gy-12}" fill="{LIGHT}" font-family="{SANS}" font-size="13" font-weight="600" text-anchor="middle" letter-spacing="1">M{m:02d}</text>')
# right border
w(f'<line x1="{right}" y1="{gy-30}" x2="{right}" y2="{gy + 9*44 + 10}" stroke="{LINE}" stroke-width="0.4"/>')

# Workstreams
streams = [
    ("Discovery & PoC scope",                0,  1, "Discovery"),
    ("Service Appointment Agent",            1,  3, "Phase 1"),
    ("Service Reminder + NPS (outbound)",    1,  3, "Phase 1"),
    ("Sales Lead + Complaint Tier-1",        3,  6, "Phase 2"),
    ("Recall Campaign",                      3,  6, "Phase 2"),
    ("Parts Inquiry",                        6,  9, "Phase 3"),
    ("Warranty Renewal",                     6,  9, "Phase 3"),
    ("Roadside Triage",                      9, 12, "Phase 4"),
    ("Insurance Cross-sell",                 9, 12, "Phase 4"),
]
for i, (name, m_start, m_end, tag) in enumerate(streams):
    ry = gy + i * 44
    w(f'<text x="{PAD}" y="{ry+22}" fill="{INK}" font-family="{SANS}" font-size="16" font-weight="500">{esc(name)}</text>')
    bx = left + m_start * month_w
    bw = (m_end - m_start) * month_w
    w(f'<rect x="{bx}" y="{ry+8}" width="{bw}" height="22" fill="{NAVY}"/>')
    # gate diamond at end
    gx = bx + bw
    w(f'<polygon points="{gx-9},{ry+19} {gx},{ry+10} {gx+9},{ry+19} {gx},{ry+28}" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
    # tag
    w(f'<text x="{right + 14}" y="{ry+22}" fill="{GRAY}" font-family="{SANS}" font-size="13" font-weight="600" letter-spacing="1.5">{esc(tag.upper())}</text>')

# Gates legend
gly = gy + 9*44 + 36
w(f'<text x="{PAD}" y="{gly}" fill="{LIGHT}" font-family="{SANS}" font-size="13" letter-spacing="2.5" font-weight="600">GATES (END OF EACH PHASE)</text>')
gates = [
    ("M1 → Phase 1", "Compliance sign-off, mock-API ready, 100 reference calls captured"),
    ("M3 → Phase 2", "Containment ≥ 60% on Service Appointment, CSAT ≥ 4.0, zero P0 incidents"),
    ("M6 → Phase 3", "WER < 8% sustained, 4 brands live, dealer council unblocking changes"),
    ("M9 → Phase 4", "Cost-to-serve −30%, NPS uplift +10, Porsche queue accepted by brand owner"),
    ("M12 → Steady state", "Cost-to-serve −45%, 70% containment, 24/7 SLA 99.5%, recall coverage 100%"),
]
for i, (when, criteria) in enumerate(gates):
    yy = gly + 30 + i * 28
    w(f'<text x="{PAD}" y="{yy}" fill="{INK}" font-family="{MONO}" font-size="14" font-weight="700">{esc(when)}</text>')
    w(f'<text x="{PAD+260}" y="{yy}" fill="{GRAY}" font-family="{SANS}" font-size="14">{esc(criteria)}</text>')

# ===================== 05 — KPI scorecard (proper table, replaces colored boxes) =====================
y_cur = gly + 30 + len(gates)*28 + 80
sec_header(y_cur, "05", "KPI Scorecard", "What we measure, where we read it, and what good looks like at month 12.")

ky = y_cur + 130
kpi_cols = [
    ("METRIC",         420),
    ("DEFINITION",     660),
    ("BASELINE",       180),
    ("MONTH 3",        160),
    ("MONTH 6",        160),
    ("MONTH 12",       180),
    ("READ FROM",      460),
    ("OWNER",          220),
]
kpis = [
    ("Containment",        "% inbound calls resolved end-to-end by AI",                  "0%",       "60%",    "65%",    "70%",     "Langfuse + CRM disposition", "Freya Delivery"),
    ("Avg. Handle Time",   "Mean inbound call duration, all intents",                    "252 s",    "150 s",  "110 s",  "<90 s",   "Telephony CDR",              "Doğuş Ops"),
    ("CSAT",               "Post-call survey, scale 1–5",                                "3.6",      "4.0",    "4.2",    "≥ 4.3",   "Freya outbound NPS bot",     "Doğuş CX"),
    ("Net Promoter Score", "Standard 0–10 NPS, calculated quarterly",                    "+24",      "+30",    "+35",    "+39",     "Quarterly NPS programme",    "Doğuş CX"),
    ("24/7 Availability",  "p50 service availability across calendar year",              "92%",      "97%",    "99%",    "99.5%",   "Datadog uptime monitor",     "Freya SRE"),
    ("Cost-to-Serve",      "Fully-loaded cost per resolved customer interaction",        "TRY 38",   "TRY 26", "TRY 22", "TRY 21",  "Finance reconciliation",     "Doğuş Finance"),
    ("Service Revenue",    "Service-channel revenue lift attributable to outbound bot",  "Index 100","Index 108","Index 116","Index 122","DMS reporting",          "Doğuş Service"),
    ("Recall Coverage",    "% of eligible base contacted within campaign window",        "62%",      "85%",    "95%",    "100%",    "OEM recall registry",        "Doğuş Compliance"),
]
total_w = sum(c[1] for c in kpi_cols)
w(f'<rect x="{PAD}" y="{ky}" width="{total_w}" height="48" fill="{NAVY}"/>')
cx = PAD
for label, cw in kpi_cols:
    w(f'<text x="{cx+16}" y="{ky+30}" fill="white" font-family="{SANS}" font-size="13" font-weight="700" letter-spacing="2">{label}</text>')
    cx += cw

row_h = 50
for i, row in enumerate(kpis):
    ry = ky + 48 + i * row_h
    bg = SOFT if i % 2 == 1 else PAPER
    w(f'<rect x="{PAD}" y="{ry}" width="{total_w}" height="{row_h}" fill="{bg}"/>')
    cx = PAD
    for j, (val, (label, cw)) in enumerate(zip(row, kpi_cols)):
        font_w = "600" if j == 0 else "400"
        font = MONO if j in (2,3,4,5) else SANS
        color = INK if j == 0 or j == 5 else GRAY if j in (1, 6, 7) else INK
        size = "16" if j == 0 else "15"
        w(f'<text x="{cx+16}" y="{ry+32}" fill="{color}" font-family="{font}" font-size="{size}" font-weight="{font_w}">{esc(str(val))}</text>')
        cx += cw

# table border
total_h = 48 + len(kpis) * row_h
w(f'<rect x="{PAD}" y="{ky}" width="{total_w}" height="{total_h}" fill="none" stroke="{INK}" stroke-width="1"/>')
# vertical column dividers
cx = PAD
for label, cw in kpi_cols[:-1]:
    cx += cw
    w(f'<line x1="{cx}" y1="{ky}" x2="{cx}" y2="{ky+total_h}" stroke="{LINE}" stroke-width="0.4"/>')

# ===================== 06 — Decision rights (RACI) =====================
y_cur = ky + total_h + 100
sec_header(y_cur, "06", "Decision Rights", "Who is Responsible, Accountable, Consulted, Informed. RACI without ambiguity.")

ry0 = y_cur + 130
raci_decisions = [
    ("Adding a new agent / use case",                "C", "A", "R", "C", "I"),
    ("Changing a workflow prompt in production",     "I", "C", "R", "I", "I"),
    ("Releasing to a new dealer or new brand",       "A", "R", "C", "C", "C"),
    ("Pricing / commercial changes",                 "A", "R", "C", "I", "I"),
    ("KVKK / data-protection decisions",             "C", "C", "C", "A", "I"),
    ("Killing the AI on a single line (kill-switch)","I", "C", "R", "I", "I"),
    ("Quarterly KPI review and reset",               "A", "R", "R", "C", "C"),
    ("OEM-mandated recall execution",                "A", "R", "C", "C", "C"),
]
raci_cols = [
    ("DECISION", 980),
    ("DOĞUŞ EXEC SPONSOR", 380),
    ("DOĞUŞ PROGRAM PM", 380),
    ("FREYA DELIVERY LEAD", 380),
    ("LEGAL / COMPLIANCE", 380),
    ("DEALER COUNCIL", 380),
]
total_w = sum(c[1] for c in raci_cols)
w(f'<rect x="{PAD}" y="{ry0}" width="{total_w}" height="48" fill="{NAVY}"/>')
cx = PAD
for label, cw in raci_cols:
    w(f'<text x="{cx + (16 if cw>600 else cw/2)}" y="{ry0+30}" fill="white" font-family="{SANS}" font-size="13" font-weight="700" letter-spacing="2" text-anchor="{("start" if cw>600 else "middle")}">{label}</text>')
    cx += cw

row_h = 50
for i, row in enumerate(raci_decisions):
    ry = ry0 + 48 + i * row_h
    bg = SOFT if i % 2 == 1 else PAPER
    w(f'<rect x="{PAD}" y="{ry}" width="{total_w}" height="{row_h}" fill="{bg}"/>')
    cx = PAD
    for j, val in enumerate(row):
        cw = raci_cols[j][1]
        if j == 0:
            w(f'<text x="{cx+16}" y="{ry+32}" fill="{INK}" font-family="{SANS}" font-size="16" font-weight="500">{esc(val)}</text>')
        else:
            tx = cx + cw/2
            # circle for emphasis on R/A
            radius = 16 if val in ("A","R") else 0
            color_fill = NAVY if val == "A" else (INK if val == "R" else "none")
            text_fill = "white" if val in ("A","R") else GRAY
            if radius:
                w(f'<circle cx="{tx}" cy="{ry+row_h/2}" r="{radius}" fill="{color_fill}" stroke="{INK}" stroke-width="1"/>')
            w(f'<text x="{tx}" y="{ry+row_h/2+6}" fill="{text_fill}" font-family="{MONO}" font-size="16" font-weight="700" text-anchor="middle">{esc(val)}</text>')
        cx += cw

# borders + verticals
total_h = 48 + len(raci_decisions) * row_h
w(f'<rect x="{PAD}" y="{ry0}" width="{total_w}" height="{total_h}" fill="none" stroke="{INK}" stroke-width="1"/>')
cx = PAD
for label, cw in raci_cols[:-1]:
    cx += cw
    w(f'<line x1="{cx}" y1="{ry0}" x2="{cx}" y2="{ry0+total_h}" stroke="{LINE}" stroke-width="0.4"/>')

# Legend below RACI
ly = ry0 + total_h + 24
w(f'<text x="{PAD}" y="{ly}" fill="{LIGHT}" font-family="{SANS}" font-size="13" letter-spacing="2.5" font-weight="600">LEGEND</text>')
w(f'<circle cx="{PAD+150}" cy="{ly-6}" r="14" fill="{NAVY}"/>')
w(f'<text x="{PAD+150}" y="{ly}" fill="white" font-family="{MONO}" font-size="14" font-weight="700" text-anchor="middle">A</text>')
w(f'<text x="{PAD+170}" y="{ly}" fill="{GRAY}" font-family="{SANS}" font-size="14">Accountable, single point</text>')
w(f'<circle cx="{PAD+460}" cy="{ly-6}" r="14" fill="{INK}"/>')
w(f'<text x="{PAD+460}" y="{ly}" fill="white" font-family="{MONO}" font-size="14" font-weight="700" text-anchor="middle">R</text>')
w(f'<text x="{PAD+480}" y="{ly}" fill="{GRAY}" font-family="{SANS}" font-size="14">Responsible, does the work</text>')
w(f'<text x="{PAD+800}" y="{ly}" fill="{INK}" font-family="{MONO}" font-size="14" font-weight="700">C</text>')
w(f'<text x="{PAD+822}" y="{ly}" fill="{GRAY}" font-family="{SANS}" font-size="14">Consulted, before decision</text>')
w(f'<text x="{PAD+1140}" y="{ly}" fill="{INK}" font-family="{MONO}" font-size="14" font-weight="700">I</text>')
w(f'<text x="{PAD+1156}" y="{ly}" fill="{GRAY}" font-family="{SANS}" font-size="14">Informed, after decision</text>')

# ===================== 07 — Risk register =====================
y_cur = ly + 70
sec_header(y_cur, "07", "Risk Register", "What can break, how likely, what we do about it. Reviewed weekly.")

rry = y_cur + 130
risks = [
    ("R1", "Dealer DMS heterogeneity blocks integration",          "High",   "High",   "Standardize on top 3 DMS profiles, build adapters; manual fallback for tail",    "Doğuş IT"),
    ("R2", "Turkish-language quality drifts at the edge",          "Medium", "High",   "Continuous fine-tune on captured calls; weekly WER monitoring with alerts",    "Freya ML"),
    ("R3", "KVKK / voice biometrics challenge",                    "Medium", "High",   "Legal opinion week 1; opt-in capture in IVR; data residency in TR region",    "Compliance"),
    ("R4", "Peak-hour overflow exceeds capacity",                  "Medium", "Medium", "Continuous batching, autoscale on H100/H200, queue with ETA broadcasted",     "Freya SRE"),
    ("R5", "Dealer change-management resistance",                  "High",   "Medium", "Champion dealers in council, monthly wins published, opt-in per dealer",      "Doğuş PM"),
    ("R6", "OEM compliance gap on recall execution",               "Low",    "High",   "Per-call audit trail, weekly OEM reporting, exception escalation in 24h",      "Compliance"),
    ("R7", "Brand-tier mix dilutes premium experience (Porsche)",  "Medium", "Medium", "Dedicated voice profile, shorter scripts, premium dialer pool",                "Doğuş Brand"),
    ("R8", "Hallucination on price / availability quotes",         "Low",    "High",   "Tool-calling for any quote; LLM reads from system, never composes numerals",  "Freya ML"),
]
risk_cols = [
    ("#",         70),
    ("RISK",      900),
    ("LIKELIHOOD",180),
    ("IMPACT",    140),
    ("MITIGATION",1500),
    ("OWNER",     290),
]
total_w = sum(c[1] for c in risk_cols)
w(f'<rect x="{PAD}" y="{rry}" width="{total_w}" height="48" fill="{NAVY}"/>')
cx = PAD
for label, cw in risk_cols:
    w(f'<text x="{cx+16}" y="{rry+30}" fill="white" font-family="{SANS}" font-size="13" font-weight="700" letter-spacing="2">{label}</text>')
    cx += cw

row_h = 60
for i, row in enumerate(risks):
    ry = rry + 48 + i * row_h
    bg = SOFT if i % 2 == 1 else PAPER
    w(f'<rect x="{PAD}" y="{ry}" width="{total_w}" height="{row_h}" fill="{bg}"/>')
    cx = PAD
    for j, val in enumerate(row):
        cw = risk_cols[j][1]
        # color severity
        color = INK
        font_w = "500" if j == 1 else "400"
        if j in (2, 3) and val == "High":
            color = RED
            font_w = "700"
        if j == 0:
            font_w = "700"
        font = MONO if j == 0 else SANS
        size = "15" if j == 4 else "16"
        w(f'<text x="{cx+16}" y="{ry+38}" fill="{color}" font-family="{font}" font-size="{size}" font-weight="{font_w}">{esc(val)}</text>')
        cx += cw

total_h = 48 + len(risks) * row_h
w(f'<rect x="{PAD}" y="{rry}" width="{total_w}" height="{total_h}" fill="none" stroke="{INK}" stroke-width="1"/>')
cx = PAD
for label, cw in risk_cols[:-1]:
    cx += cw
    w(f'<line x1="{cx}" y1="{rry}" x2="{cx}" y2="{rry+total_h}" stroke="{LINE}" stroke-width="0.4"/>')

# ===================== 08 — Assumptions & Dependencies =====================
y_cur = rry + total_h + 100
sec_header(y_cur, "08", "Assumptions & Dependencies", "What must hold for the plan to land. If any breaks, the schedule re-baselines.")

ay = y_cur + 120
assumptions = [
    "API access to SAP CRM and the three highest-volume Dealer DMS instances is in place by week 2.",
    "Existing Cisco UCM admits SIP egress to a Freya endpoint without disrupting the legacy IVR.",
    "Doğuş Compliance issues a written opinion on voice biometrics and KVKK consent before pilot launch.",
    "A pilot cohort of three dealerships (one VW, one Audi, one Škoda) commits to be primary references.",
    "Freya is permitted to retain de-identified call audio for fine-tuning, separate from PII storage.",
    "Brand owners (Porsche, Bentley, Lamborghini) accept a separate premium voice profile by month 9.",
    "Annual call volume forecast (12.4M inbound) does not change by more than ±15% during the engagement.",
]
for i, a in enumerate(assumptions):
    yy = ay + i*38
    w(f'<text x="{PAD}" y="{yy}" fill="{INK}" font-family="{MONO}" font-size="15" font-weight="700">A{i+1:02d}</text>')
    w(f'<text x="{PAD+72}" y="{yy}" fill="{INK}" font-family="{SERIF}" font-size="20">{esc(a)}</text>')

# ===================== Footer / sign-off block =====================
fy = H - 240
w(f'<line x1="{PAD}" y1="{fy}" x2="{W-PAD}" y2="{fy}" stroke="{INK}" stroke-width="1"/>')
# signature blocks
sig_w = (W - 2*PAD - 60) / 3
sigs = [
    ("DOĞUŞ OTOMOTİV", "Executive Sponsor", "Name, title"),
    ("FREYA LABS", "Engagement Lead, Tunga Bayrak", "CEO and Co-Founder"),
    ("LEGAL / COMPLIANCE", "Officer of record", "Name, title"),
]
for i, (org, role, sub) in enumerate(sigs):
    sx = PAD + i * (sig_w + 30)
    w(f'<text x="{sx}" y="{fy+38}" fill="{LIGHT}" font-family="{SANS}" font-size="13" letter-spacing="2.5" font-weight="600">{org}</text>')
    w(f'<line x1="{sx}" y1="{fy+90}" x2="{sx+sig_w}" y2="{fy+90}" stroke="{INK}" stroke-width="0.6"/>')
    w(f'<text x="{sx}" y="{fy+114}" fill="{INK}" font-family="{SERIF}" font-size="18">{esc(role)}</text>')
    w(f'<text x="{sx}" y="{fy+138}" fill="{GRAY}" font-family="{SANS}" font-size="14">{esc(sub)}</text>')

# bottom info bar
w(f'<line x1="{PAD}" y1="{H-80}" x2="{W-PAD}" y2="{H-80}" stroke="{INK}" stroke-width="0.4"/>')
w(f'<text x="{PAD}" y="{H-50}" fill="{LIGHT}" font-family="{SANS}" font-size="12" letter-spacing="2">REV 1.1 · APRIL 2026 · ISSUED BY FREYA LABS · NOT FOR EXTERNAL DISTRIBUTION</text>')
w(f'<text x="{W-PAD}" y="{H-50}" fill="{LIGHT}" font-family="{SANS}" font-size="12" letter-spacing="2" text-anchor="end">FREYAVOICE.AI · TUNGA@FREYAVOICE.AI · +90 536 467 3603</text>')

w('</svg>')

import pathlib
out_path = pathlib.Path(__file__).parent / "dogus_ai_call_center_blueprint.svg"
out_path.write_text("\n".join(out), encoding="utf-8")
print(f"Wrote {out_path} ({out_path.stat().st_size:,} bytes)")
