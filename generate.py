#!/usr/bin/env python3
"""
Generate the Doğuş Otomotiv x Freya Voice AI Call Center Transformation Blueprint
as a single self-contained SVG poster, designed for whiteboard / large-format viewing.

Output:
  dogus_ai_call_center_blueprint.svg  — single large SVG, infinitely zoomable
"""

W, H = 3600, 2700
PAD = 48

NAVY = "#0a2540"
INK = "#1f2937"
SUB = "#6b7280"
LINE = "#e5e7eb"
BG = "#f8f9fc"
CARD = "#ffffff"
BLUE = "#2563eb"
LIGHT_BLUE = "#dbeafe"
AMBER = "#f59e0b"
LIGHT_AMBER = "#fef3c7"
GREEN = "#10b981"
LIGHT_GREEN = "#d1fae5"
RED = "#ef4444"
LIGHT_RED = "#fee2e2"
PURPLE = "#7c3aed"
LIGHT_PURPLE = "#ede9fe"
TEAL = "#0d9488"
LIGHT_TEAL = "#ccfbf1"

FONT = "Inter, 'Segoe UI', system-ui, -apple-system, sans-serif"

out = []
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") if isinstance(s, str) else s
def w(s):
    # Only escape inside text, not full markup
    out.append(s)

# ===================== Header =====================
w(f'<?xml version="1.0" encoding="UTF-8"?>')
w(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">')

# Defs: filters, markers, gradients
w('<defs>')
w('<filter id="shadow" x="-2%" y="-2%" width="104%" height="108%">')
w('  <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>')
w('  <feOffset dx="0" dy="2" result="offsetblur"/>')
w('  <feComponentTransfer><feFuncA type="linear" slope="0.10"/></feComponentTransfer>')
w('  <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>')
w('</filter>')
w('<marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">')
w(f'  <path d="M0,0 L0,12 L10,6 z" fill="{NAVY}"/>')
w('</marker>')
w('<marker id="arrow-blue" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">')
w(f'  <path d="M0,0 L0,12 L10,6 z" fill="{BLUE}"/>')
w('</marker>')
w(f'<linearGradient id="header-grad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="{NAVY}"/><stop offset="100%" stop-color="#143b66"/></linearGradient>')
w('</defs>')

# Background
w(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# ===================== Top Header Band =====================
w(f'<rect x="0" y="0" width="{W}" height="200" fill="url(#header-grad)"/>')
w(f'<text x="{PAD+24}" y="86" fill="white" font-size="64" font-weight="800" letter-spacing="-1">Doğuş Otomotiv × Freya Labs</text>')
w(f'<text x="{PAD+24}" y="146" fill="#cbd5e1" font-size="36" font-weight="500">Call Center AI Transformation Blueprint, 12-Month Operating Model</text>')
w(f'<text x="{PAD+24}" y="184" fill="#94a3b8" font-size="22" font-weight="400">VW · Audi · Skoda · SEAT · Porsche · Bentley · Lamborghini   |   400+ dealers, ~3M active customers, 24/7 service line</text>')

# Right side stats
stats_x = W - 760
w(f'<rect x="{stats_x}" y="40" width="700" height="120" fill="rgba(255,255,255,0.08)" rx="12"/>')
w(f'<text x="{stats_x+24}" y="74" fill="white" font-size="20" font-weight="600">Engagement Summary</text>')
w(f'<text x="{stats_x+24}" y="106" fill="#cbd5e1" font-size="18">Phase 1 PoC: Service Appointment Agent · 60-day pilot</text>')
w(f'<text x="{stats_x+24}" y="134" fill="#cbd5e1" font-size="18">Target: 70% containment, &lt;90s AHT, 24/7 coverage</text>')

# Version badge
w(f'<rect x="{W-220}" y="170" width="180" height="28" fill="rgba(255,255,255,0.15)" rx="14"/>')
w(f'<text x="{W-130}" y="190" fill="white" font-size="14" text-anchor="middle">Rev 1.0 · April 2026</text>')

# ===================== Section helpers =====================
def section_header(x, y, w_, title, subtitle=None, color=NAVY):
    w(f'<rect x="{x}" y="{y}" width="{w_}" height="6" fill="{color}" rx="3"/>')
    w(f'<text x="{x}" y="{y+44}" fill="{INK}" font-size="30" font-weight="800">{title}</text>')
    if subtitle:
        w(f'<text x="{x}" y="{y+74}" fill="{SUB}" font-size="18" font-weight="400">{subtitle}</text>')

def card(x, y, w_, h, title, body_lines, accent=BLUE, fill=CARD, accent_strip_height=8):
    w(f'<rect x="{x}" y="{y}" width="{w_}" height="{h}" fill="{fill}" stroke="{LINE}" stroke-width="1" rx="10" filter="url(#shadow)"/>')
    w(f'<rect x="{x}" y="{y}" width="{w_}" height="{accent_strip_height}" fill="{accent}" rx="10"/>')
    w(f'<text x="{x+20}" y="{y+44}" fill="{INK}" font-size="20" font-weight="700">{title}</text>')
    for i, line in enumerate(body_lines):
        if line.startswith("•"):
            w(f'<text x="{x+20}" y="{y+78+i*26}" fill="{INK}" font-size="15">{line}</text>')
        elif line.startswith("→"):
            w(f'<text x="{x+20}" y="{y+78+i*26}" fill="{BLUE}" font-size="15" font-weight="600">{line}</text>')
        elif line.startswith("**"):
            w(f'<text x="{x+20}" y="{y+78+i*26}" fill="{INK}" font-size="15" font-weight="700">{line[2:-2] if line.endswith("**") else line[2:]}</text>')
        else:
            w(f'<text x="{x+20}" y="{y+78+i*26}" fill="{SUB}" font-size="14">{line}</text>')

def metric_card(x, y, w_, h, value, label, accent=BLUE):
    w(f'<rect x="{x}" y="{y}" width="{w_}" height="{h}" fill="{CARD}" stroke="{LINE}" rx="10" filter="url(#shadow)"/>')
    w(f'<text x="{x+w_/2}" y="{y+h/2}" fill="{accent}" font-size="42" font-weight="800" text-anchor="middle">{value}</text>')
    w(f'<text x="{x+w_/2}" y="{y+h/2+30}" fill="{SUB}" font-size="14" text-anchor="middle">{label}</text>')

# ===================== Section 1: Customer journey + channels =====================
y_cur = 240
section_header(PAD, y_cur, W-2*PAD, "01 · Inbound &amp; Outbound Channels", "Where customers reach us, where we reach customers", color=BLUE)

ch_y = y_cur + 96
ch_w = (W - 2*PAD - 6*16) / 7
channels = [
    ("📞 Phone", "Cisco IVR\n444 0 X", "Main line, 24/7"),
    ("💬 WhatsApp", "Business API", "High-volume, async"),
    ("🌐 Web Chat", "dogusoto.com.tr", "Pre-sale & support"),
    ("✉ Email", "Service ticket", "Lower priority"),
    ("📱 App", "DOD app", "Authenticated users"),
    ("🚗 Roadside", "112-style", "Emergency triage"),
    ("🤖 Outbound", "AI-driven", "Reminders, NPS, recalls"),
]
for i, (name, sub, desc) in enumerate(channels):
    x = PAD + i * (ch_w + 16)
    w(f'<rect x="{x}" y="{ch_y}" width="{ch_w}" height="160" fill="{CARD}" stroke="{LINE}" rx="10" filter="url(#shadow)"/>')
    w(f'<rect x="{x}" y="{ch_y}" width="{ch_w}" height="6" fill="{BLUE}" rx="10"/>')
    w(f'<text x="{x+20}" y="{ch_y+50}" fill="{INK}" font-size="22" font-weight="700">{name}</text>')
    for j, line in enumerate(sub.split("\n")):
        w(f'<text x="{x+20}" y="{ch_y+82+j*22}" fill="{INK}" font-size="14">{line}</text>')
    w(f'<text x="{x+20}" y="{ch_y+138}" fill="{SUB}" font-size="13">{desc}</text>')

# ===================== Section 2: AI Agent Map (centerpiece) =====================
y_cur = 540
section_header(PAD, y_cur, W-2*PAD, "02 · AI Agent Map", "10 specialized voice agents grouped by intent. Each owns a use case end-to-end.", color=NAVY)

agents = [
    # row 1: inbound primary
    ("Service Appointment", "Inbound · Phase 1", BLUE, LIGHT_BLUE,
     ["• Vehicle plate lookup", "• Slot booking by dealer", "• Service type triage",
      "• SMS confirmation", "• Reschedule / cancel", "→ ROI: ~40% containment"]),
    ("Sales Lead Qualifier", "Inbound · Phase 2", BLUE, LIGHT_BLUE,
     ["• Brand & model interest", "• Budget + financing", "• Test-drive booking",
      "• Dealer routing", "• Lead scoring", "→ ROI: faster handoff"]),
    ("Parts Inquiry", "Inbound · Phase 3", BLUE, LIGHT_BLUE,
     ["• Part number lookup", "• Stock check at dealer", "• Price quote",
      "• Order placement", "• Pickup scheduling", "→ ROI: dealer staff offload"]),
    ("Complaint Tier-1", "Inbound · Phase 2", AMBER, LIGHT_AMBER,
     ["• Capture details", "• Sentiment routing", "• Acknowledgement",
      "• Promise of callback", "• Escalation flag", "→ ROI: 100% logged"]),
    ("Roadside Triage", "Inbound · Phase 4", RED, LIGHT_RED,
     ["• Location + situation", "• Severity scoring", "• Tow vs on-site",
      "• Dispatch hand-off", "• ETA tracking", "→ ROI: faster response"]),
    # row 2: outbound primary
    ("Service Reminder", "Outbound · Phase 1", GREEN, LIGHT_GREEN,
     ["• Mileage / time-based", "• Personalized timing", "• Slot offer",
      "• Reschedule loop", "• Multi-attempt", "→ ROI: +20% service revenue"]),
    ("Recall Campaign", "Outbound · Phase 2", PURPLE, LIGHT_PURPLE,
     ["• Compliance-driven", "• Bulk eligible list", "• Booking with priority",
      "• Audit trail", "• Reporting to OEM", "→ ROI: regulatory cover"]),
    ("Warranty Renewal", "Outbound · Phase 3", PURPLE, LIGHT_PURPLE,
     ["• 60/30/15 day reminders", "• Quote on call", "• Upsell extended",
      "• Payment link", "• Cross-sell insurance", "→ ROI: renewal lift"]),
    ("NPS / CX Survey", "Outbound · Phase 1", TEAL, LIGHT_TEAL,
     ["• Post-service callback", "• 3-question script", "• Open-text capture",
      "• Sentiment scored", "• Detractor escalation", "→ ROI: closed-loop CX"]),
    ("Insurance Cross-sell", "Outbound · Phase 4", TEAL, LIGHT_TEAL,
     ["• Telematics-triggered", "• Quote in conversation", "• Bind-on-call",
      "• Dealer commission", "• KVKK opt-in capture", "→ ROI: new revenue line"]),
]

cols = 5
gap = 18
agent_w = (W - 2*PAD - (cols-1)*gap) / cols
agent_h = 280
ay0 = y_cur + 110
for i, (name, tag, accent, fill, bullets) in enumerate(agents):
    row = i // cols
    col = i % cols
    x = PAD + col * (agent_w + gap)
    y = ay0 + row * (agent_h + gap)
    w(f'<rect x="{x}" y="{y}" width="{agent_w}" height="{agent_h}" fill="{CARD}" stroke="{LINE}" rx="12" filter="url(#shadow)"/>')
    w(f'<rect x="{x}" y="{y}" width="{agent_w}" height="56" fill="{accent}" rx="12"/>')
    w(f'<rect x="{x}" y="{y+44}" width="{agent_w}" height="12" fill="{accent}"/>')
    w(f'<text x="{x+20}" y="{y+36}" fill="white" font-size="22" font-weight="800">{name}</text>')
    # tag pill
    w(f'<rect x="{x+20}" y="{y+72}" width="180" height="26" fill="{fill}" rx="13"/>')
    w(f'<text x="{x+110}" y="{y+90}" fill="{accent}" font-size="13" font-weight="700" text-anchor="middle">{tag}</text>')
    for j, b in enumerate(bullets):
        if b.startswith("→"):
            w(f'<text x="{x+20}" y="{y+128+j*26}" fill="{accent}" font-size="14" font-weight="700">{b}</text>')
        else:
            w(f'<text x="{x+20}" y="{y+128+j*26}" fill="{INK}" font-size="14">{b}</text>')

# ===================== Section 3: Tech Stack =====================
y_cur = ay0 + 2*agent_h + gap + 80
section_header(PAD, y_cur, W-2*PAD, "03 · Technology Stack", "Layered view from telephony to analytics. Freya owns voice + LLM + workflow; Doğuş owns CRM + DMS.", color=PURPLE)

stack_y = y_cur + 110
layers = [
    ("Telephony", "Cisco UCM · SIP trunk · 444-0-X", "Doğuş incumbent", "#1e293b"),
    ("Voice I/O", "Freya STT (Qwen3-ASR-TR, 50ms p50) · Freya TTS (BiCodec)", "Freya", BLUE),
    ("LLM Routing", "Gemma-Banking-3 (TR-tuned) · Gemini-3-Flash · Claude Haiku 4.5 fallback", "Freya", PURPLE),
    ("Workflow Engine", "Freya state machine · per-agent flows · API-call nodes", "Freya", PURPLE),
    ("Knowledge &amp; Tools", "Service catalog · Parts catalog · Recall list · Pricing API", "Doğuş", AMBER),
    ("CRM / DMS", "SAP CRM · DOD app · Dealer DMS (heterogeneous)", "Doğuş", AMBER),
    ("Observability", "Langfuse traces · Datadog · QA sample reviews · WER/CER monitoring", "Freya", GREEN),
    ("Compliance", "KVKK consent capture · voice biometrics · 90-day retention · SOC2", "Joint", RED),
]
layer_h = 64
for i, (name, tech, owner, color) in enumerate(layers):
    y = stack_y + i * (layer_h + 8)
    w(f'<rect x="{PAD}" y="{y}" width="{W-2*PAD}" height="{layer_h}" fill="{CARD}" stroke="{LINE}" rx="8" filter="url(#shadow)"/>')
    w(f'<rect x="{PAD}" y="{y}" width="14" height="{layer_h}" fill="{color}" rx="8"/>')
    w(f'<text x="{PAD+34}" y="{y+layer_h/2-4}" fill="{INK}" font-size="20" font-weight="700">{name}</text>')
    w(f'<text x="{PAD+34}" y="{y+layer_h/2+22}" fill="{SUB}" font-size="15">{tech}</text>')
    # owner pill on right
    pill_x = W - PAD - 180
    pill_color = color
    w(f'<rect x="{pill_x}" y="{y+layer_h/2-16}" width="160" height="32" fill="{color}" rx="16" opacity="0.15"/>')
    w(f'<text x="{pill_x+80}" y="{y+layer_h/2+5}" fill="{color}" font-size="14" font-weight="700" text-anchor="middle">Owner: {owner}</text>')

# ===================== Section 4: Phased Rollout =====================
y_cur = stack_y + 8 * (layer_h + 8) + 60
section_header(PAD, y_cur, W-2*PAD, "04 · Phased Rollout · 12 Months", "From single-agent PoC to multi-brand premium scale, gated by KPIs.", color=AMBER)

phases = [
    ("Phase 0", "Discover", "Week 0-4",
     ["Volume audit, top-10 intents", "Existing IVR mining", "DMS API discovery",
      "Compliance & KVKK sign-off", "PoC scope locked", "Baseline KPIs captured"], LIGHT_BLUE, BLUE),
    ("Phase 1", "Pilot", "Month 1-3",
     ["Service Appointment Agent", "Service Reminder (outbound)", "NPS Survey",
      "1 brand × 3 dealer pilots", "Live monitoring + war room", "Gate: 70% containment"], LIGHT_GREEN, GREEN),
    ("Phase 2", "Expand", "Month 4-6",
     ["Sales Lead + Complaint", "Recall Campaign", "Multi-dealer routing",
      "Brand 2 + Brand 3", "Analytics dashboard live", "Gate: stable WER < 8%"], LIGHT_AMBER, AMBER),
    ("Phase 3", "Deepen", "Month 7-9",
     ["Parts Inquiry", "Warranty Renewal", "Telematics integration",
      "Premium brands (Porsche)", "Cross-sell modules", "Gate: NPS uplift +5"], LIGHT_PURPLE, PURPLE),
    ("Phase 4", "Scale", "Month 10-12",
     ["Roadside Triage", "Insurance Cross-sell", "Full multi-brand",
      "All channels integrated", "Self-service knowledge", "Gate: cost-to-serve -45%"], LIGHT_RED, RED),
]
ph_w = (W - 2*PAD - 4*16) / 5
ph_h = 380
phy = y_cur + 110
for i, (label, name, when, items, fill, accent) in enumerate(phases):
    x = PAD + i * (ph_w + 16)
    w(f'<rect x="{x}" y="{phy}" width="{ph_w}" height="{ph_h}" fill="{CARD}" stroke="{LINE}" rx="12" filter="url(#shadow)"/>')
    # accent banner
    w(f'<rect x="{x}" y="{phy}" width="{ph_w}" height="80" fill="{fill}" rx="12"/>')
    w(f'<rect x="{x}" y="{phy+68}" width="{ph_w}" height="12" fill="{fill}"/>')
    w(f'<text x="{x+20}" y="{phy+34}" fill="{accent}" font-size="14" font-weight="800" letter-spacing="1.5">{label.upper()}</text>')
    w(f'<text x="{x+20}" y="{phy+62}" fill="{INK}" font-size="26" font-weight="800">{name}</text>')
    w(f'<text x="{x+ph_w-20}" y="{phy+62}" fill="{accent}" font-size="14" font-weight="700" text-anchor="end">{when}</text>')
    # items
    for j, it in enumerate(items):
        w(f'<circle cx="{x+24}" cy="{phy+118+j*40}" r="3" fill="{accent}"/>')
        w(f'<text x="{x+38}" y="{phy+123+j*40}" fill="{INK}" font-size="14">{it}</text>')
    # arrow to next phase
    if i < len(phases)-1:
        ax = x + ph_w
        ay = phy + 60
        w(f'<path d="M {ax+1} {ay} L {ax+13} {ay}" stroke="{accent}" stroke-width="2" marker-end="url(#arrow-blue)"/>')

# ===================== Section 5: KPI Dashboard =====================
y_cur = phy + ph_h + 70
section_header(PAD, y_cur, W-2*PAD, "05 · KPI Targets &amp; Measurement", "What success looks like at month 12. Measured weekly, reported monthly.", color=GREEN)

kpis = [
    ("70%", "Containment\n(end-to-end AI)", BLUE),
    ("< 90s", "Avg Handle Time\n(inbound)", BLUE),
    ("≥ 4.3", "CSAT\n(post-call survey)", GREEN),
    ("+15", "NPS\n(vs baseline)", GREEN),
    ("99.5%", "24/7 availability\n(p50 SLA)", PURPLE),
    ("-45%", "Cost-to-serve\n(per resolved)", AMBER),
    ("+22%", "Service rev.\n(reminder-driven)", AMBER),
    ("100%", "Recall coverage\n(eligible base)", RED),
]
ky = y_cur + 110
kw = (W - 2*PAD - 7*16) / 8
kh = 160
for i, (val, lbl, color) in enumerate(kpis):
    x = PAD + i * (kw + 16)
    w(f'<rect x="{x}" y="{ky}" width="{kw}" height="{kh}" fill="{CARD}" stroke="{LINE}" rx="12" filter="url(#shadow)"/>')
    w(f'<rect x="{x}" y="{ky}" width="{kw}" height="6" fill="{color}" rx="12"/>')
    w(f'<text x="{x+kw/2}" y="{ky+78}" fill="{color}" font-size="44" font-weight="800" text-anchor="middle">{val}</text>')
    for j, line in enumerate(lbl.split("\n")):
        w(f'<text x="{x+kw/2}" y="{ky+108+j*22}" fill="{SUB}" font-size="14" text-anchor="middle">{line}</text>')

# ===================== Section 6: Governance =====================
y_cur = ky + kh + 70
section_header(PAD, y_cur, W-2*PAD, "06 · Governance &amp; Operating Cadence", "Who decides what, on what cadence. Aligned with dealer network reality.", color=NAVY)

gov_y = y_cur + 110
gov = [
    ("Steering Committee", "Monthly", ["Doğuş GM Müşteri Hiz.", "Doğuş CIO", "Freya CEO", "Freya VP Customer"], NAVY),
    ("War Room", "Weekly", ["Freya delivery lead", "Doğuş PM", "QA reviewer", "Dealer rep (rotating)"], BLUE),
    ("Quality Council", "Bi-weekly", ["Sample 50 calls", "Score WER, CSAT, intent", "Update prompt library", "Failure pattern review"], GREEN),
    ("Dealer Council", "Monthly", ["10 pilot dealers", "Friction reports", "Process changes", "Local language gotchas"], AMBER),
    ("Compliance Officer", "Continuous", ["KVKK audit log", "Voice consent capture", "Data retention review", "Incident reporting"], RED),
]
gw = (W - 2*PAD - 4*18) / 5
gh = 240
for i, (name, cad, members, color) in enumerate(gov):
    x = PAD + i * (gw + 18)
    w(f'<rect x="{x}" y="{gov_y}" width="{gw}" height="{gh}" fill="{CARD}" stroke="{LINE}" rx="10" filter="url(#shadow)"/>')
    w(f'<rect x="{x}" y="{gov_y}" width="{gw}" height="6" fill="{color}" rx="10"/>')
    w(f'<text x="{x+20}" y="{gov_y+44}" fill="{INK}" font-size="20" font-weight="800">{name}</text>')
    w(f'<rect x="{x+20}" y="{gov_y+58}" width="120" height="26" fill="{color}" rx="13" opacity="0.15"/>')
    w(f'<text x="{x+80}" y="{gov_y+76}" fill="{color}" font-size="13" font-weight="700" text-anchor="middle">{cad}</text>')
    for j, m in enumerate(members):
        w(f'<circle cx="{x+24}" cy="{gov_y+114+j*30}" r="3" fill="{color}"/>')
        w(f'<text x="{x+38}" y="{gov_y+119+j*30}" fill="{INK}" font-size="14">{m}</text>')

# ===================== Section 7: Risk register (right) and Quick wins (left) =====================
y_cur = gov_y + gh + 60
risks_w = (W - 2*PAD - 24) / 2

# Quick wins
section_header(PAD, y_cur, risks_w, "07a · Quick Wins (≤ 60 days)", "Visible, low-risk, fast ROI", color=GREEN)
wins = [
    "✓ Service Appointment Agent in 1 brand × 3 dealers",
    "✓ Outbound NPS callback for last week's services",
    "✓ Inbound call-overflow handling (peak Mon 10-12)",
    "✓ Recall campaign call-out for one open campaign",
    "✓ Dashboard: real-time call volume + containment",
    "✓ Daily Slack digest of failed/escalated calls",
]
wy = y_cur + 110
w(f'<rect x="{PAD}" y="{wy}" width="{risks_w}" height="280" fill="{CARD}" stroke="{LINE}" rx="10" filter="url(#shadow)"/>')
w(f'<rect x="{PAD}" y="{wy}" width="{risks_w}" height="8" fill="{GREEN}" rx="10"/>')
for j, win in enumerate(wins):
    w(f'<text x="{PAD+24}" y="{wy+58+j*36}" fill="{INK}" font-size="17" font-weight="500">{win}</text>')

# Risks
rx = PAD + risks_w + 24
section_header(rx, y_cur, risks_w, "07b · Risk Register", "What can break, and how we de-risk", color=RED)
risks = [
    ("Dealer DMS heterogeneity", "Standardize 3 most common, manual fallback for rest"),
    ("Turkish language quality at edge", "Continuous fine-tune on collected calls"),
    ("KVKK + voice biometrics", "Legal opinion in week 1, opt-in flow on call"),
    ("Peak hour overflow", "Continuous batching + autoscale + queue with ETA"),
    ("Dealer change-management", "Champion dealer council + pilot wins as proof"),
    ("OEM compliance (recall)", "Audit trail per call, weekly OEM reporting"),
]
w(f'<rect x="{rx}" y="{wy}" width="{risks_w}" height="280" fill="{CARD}" stroke="{LINE}" rx="10" filter="url(#shadow)"/>')
w(f'<rect x="{rx}" y="{wy}" width="{risks_w}" height="8" fill="{RED}" rx="10"/>')
for j, (r, m) in enumerate(risks):
    w(f'<text x="{rx+24}" y="{wy+50+j*38}" fill="{INK}" font-size="15" font-weight="700">⚠ {r}</text>')
    w(f'<text x="{rx+44}" y="{wy+70+j*38}" fill="{SUB}" font-size="13">→ {m}</text>')

# ===================== Footer =====================
fy = H - 80
w(f'<line x1="{PAD}" y1="{fy-12}" x2="{W-PAD}" y2="{fy-12}" stroke="{LINE}" stroke-width="1"/>')
w(f'<text x="{PAD}" y="{fy+18}" fill="{SUB}" font-size="14">Prepared by Freya Labs · Confidential, for Doğuş Otomotiv leadership review · Print at A0 (84cm × 119cm) for war-room wall</text>')
w(f'<text x="{W-PAD}" y="{fy+18}" fill="{SUB}" font-size="14" text-anchor="end">freyavoice.ai · tunga@freyavoice.ai · +90 536 467 3603</text>')

w('</svg>')

import sys, pathlib
out_path = pathlib.Path(__file__).parent / "dogus_ai_call_center_blueprint.svg"
out_path.write_text("\n".join(out), encoding="utf-8")
print(f"Wrote {out_path} ({out_path.stat().st_size:,} bytes)")
