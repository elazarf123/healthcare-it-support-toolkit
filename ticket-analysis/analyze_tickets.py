"""
analyze_tickets.py
Turns the raw ticket extract into the metrics a support manager acts on:

  - volume + SLA breach rate by category
  - which categories deserve automation/self-service investment
  - reopen rates (quality signal, not just speed)

Outputs: findings.md + ticket_volume_sla.png
Run after generate_tickets.py.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
df = pd.read_csv(HERE / "tickets.csv")

by_cat = df.groupby("category").agg(
    tickets=("ticket_id", "count"),
    median_resolve_min=("resolve_minutes", "median"),
    sla_breach_pct=("sla_breached", lambda s: round(100 * s.mean(), 1)),
    reopen_pct=("reopened", lambda s: round(100 * s.mean(), 1)),
).sort_values("tickets", ascending=False)

# ---- chart: volume vs SLA breach rate --------------------------------------
fig, ax1 = plt.subplots(figsize=(11, 5.5))
ax1.barh(by_cat.index[::-1], by_cat["tickets"][::-1], color="#a5c8e4")
ax1.set_xlabel("Tickets (90 days)")
for i, (cat, row) in enumerate(by_cat[::-1].iterrows()):
    ax1.text(row["tickets"] + 3, i, f"{row['sla_breach_pct']}% SLA breach",
             va="center", fontsize=9, color="#c0392b")
ax1.set_title("Service Desk: 90-Day Ticket Volume & SLA Breach Rate by Category (synthetic)")
fig.tight_layout()
fig.savefig(HERE / "ticket_volume_sla.png", dpi=120)

# ---- findings ---------------------------------------------------------------
top_volume = by_cat.index[0]
worst_sla = by_cat.sort_values("sla_breach_pct", ascending=False).iloc[0]
worst_reopen = by_cat.sort_values("reopen_pct", ascending=False).iloc[0]
pw = by_cat.loc["Password reset"]

lines = [
    "# Ticket Analysis — Findings & Recommendations",
    "",
    f"Dataset: {len(df)} tickets over 90 days (synthetic). "
    "Analysis in `analyze_tickets.py`; chart in `ticket_volume_sla.png`.",
    "",
    "## What the data says",
    "",
    f"1. **`{top_volume}` is the volume leader** ({by_cat.iloc[0]['tickets']} tickets). "
    "High-volume, low-complexity categories are the automation target list.",
    f"2. **`{worst_sla.name}` breaches SLA most** ({worst_sla['sla_breach_pct']}% of tickets). "
    "These involve vendor coordination — the fix is a different SLA tier and a vendor-escalation "
    "runbook, not pushing techs harder.",
    f"3. **`{worst_reopen.name}` has the highest reopen rate** ({worst_reopen['reopen_pct']}%). "
    "Reopens are a fix-quality signal: recommend a permanent-fix checklist (driver version, "
    "tray config, test page from the EHR, not just Windows).",
    f"4. **Password resets: {int(pw['tickets'])} tickets at {pw['median_resolve_min']:.0f} min median.** "
    "Every one is self-service-able. SSPR enrollment push would remove roughly "
    f"{int(pw['tickets'])} tickets/quarter from the queue.",
    "",
    "## Recommended actions (priority order)",
    "",
    "| Action | Effort | Impact |",
    "|---|---|---|",
    "| SSPR enrollment campaign for password resets | Low | Removes ~13% of queue |",
    "| Vendor-escalation runbook + separate SLA for device connectivity | Low | Fixes worst breach category |",
    "| Printer permanent-fix checklist | Low | Cuts highest reopen rate |",
    "| Knowledge-base articles for top 3 EHR login failure modes | Medium | Shifts volume leader left |",
]
(HERE / "findings.md").write_text("\n".join(lines))
print(by_cat.to_string())
print(f"\nWrote findings.md + ticket_volume_sla.png")
