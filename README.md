# Doğuş Otomotiv × Freya Labs

## Call Center AI Transformation Blueprint

A comprehensive, single-page operating model for transforming the Doğuş Otomotiv multi-brand contact center into a 24/7 AI-augmented operation. Designed as a war-room wall poster, zoomable on screen.

### View

- **SVG (zoom forever in browser)**: [`dogus_ai_call_center_blueprint.svg`](./dogus_ai_call_center_blueprint.svg)
- **PNG (3600px)**: [`dogus_ai_call_center_blueprint.png`](./dogus_ai_call_center_blueprint.png)
- **PDF (print-ready)**: [`dogus_ai_call_center_blueprint.pdf`](./dogus_ai_call_center_blueprint.pdf)

### What it covers

1. **Inbound & Outbound Channels** — phone, WhatsApp, web chat, email, app, roadside, outbound dialer
2. **AI Agent Map** — 10 specialized voice agents (5 inbound, 5 outbound) covering the full customer lifecycle
3. **Technology Stack** — 8-layer model from telephony up to compliance, with clear ownership (Doğuş vs Freya)
4. **Phased Rollout** — 12-month plan with 5 phases and KPI gates
5. **KPI Targets** — 8 measurable outcomes (containment, AHT, CSAT, NPS, availability, cost-to-serve, revenue, recall coverage)
6. **Governance** — 5 standing forums with cadence and members
7. **Quick Wins + Risk Register** — 60-day deliverables and de-risking plan

### How it was made

Single Python script (`generate.py`) writes a self-contained SVG. No external dependencies, no JS, no fonts to load. Renders identically in browsers, Figma, and as a print artifact.

### Regenerate

```bash
python3 generate.py
rsvg-convert -f png -w 3600 -o dogus_ai_call_center_blueprint.png dogus_ai_call_center_blueprint.svg
rsvg-convert -f pdf -o dogus_ai_call_center_blueprint.pdf dogus_ai_call_center_blueprint.svg
```

### Print

A0 (84 × 119 cm) for war-room wall display. Source SVG is vector — scales to any size.

---

Prepared by Freya Labs · Confidential, for Doğuş Otomotiv leadership review
