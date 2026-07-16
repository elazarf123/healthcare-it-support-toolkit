"""
generate_tickets.py
Creates a synthetic 90-day service-desk ticket extract (tickets.csv)
for a mid-size clinic network. Seeded for reproducibility. No PHI.
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(11)

OUT = Path(__file__).resolve().parent
CATEGORIES = {
    "EHR access / login": (0.28, 25),        # (share of volume, base resolve minutes)
    "Clinical workstation": (0.18, 45),
    "Printer / label printer": (0.14, 40),
    "Password reset": (0.13, 12),
    "Network / VDI": (0.10, 75),
    "Medical device connectivity": (0.07, 120),
    "Software request": (0.06, 240),
    "Phone / paging": (0.04, 60),
}
PRIORITIES = {"P1": 0.04, "P2": 0.16, "P3": 0.55, "P4": 0.25}
SLA_MIN = {"P1": 60, "P2": 240, "P3": 1440, "P4": 4320}
DEPARTMENTS = ["Emergency", "Cardiology", "Family Medicine", "Pulmonology",
               "Registration", "Revenue Cycle", "Pharmacy", "Radiology"]

start = datetime(2025, 4, 1, 7, 0)
rows = []
for i in range(1, 641):
    cat = random.choices(list(CATEGORIES), weights=[v[0] for v in CATEGORIES.values()])[0]
    pri = random.choices(list(PRIORITIES), weights=PRIORITIES.values())[0]
    opened = start + timedelta(minutes=random.randint(0, 90 * 24 * 60))
    base = CATEGORIES[cat][1]
    resolve_min = max(5, int(random.gauss(base, base * 0.6)))
    # Medical device + software request tickets breach SLA more often
    if cat in ("Medical device connectivity", "Software request") and random.random() < 0.35:
        resolve_min = int(SLA_MIN[pri] * random.uniform(1.1, 2.2))
    rows.append({
        "ticket_id": f"INC-{40000+i}",
        "opened_at": opened.strftime("%Y-%m-%d %H:%M"),
        "department": random.choice(DEPARTMENTS),
        "category": cat,
        "priority": pri,
        "resolve_minutes": resolve_min,
        "sla_minutes": SLA_MIN[pri],
        "sla_breached": int(resolve_min > SLA_MIN[pri]),
        "reopened": int(random.random() < (0.12 if cat == "Printer / label printer" else 0.04)),
    })

with open(OUT / "tickets.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)

print(f"Wrote {len(rows)} tickets -> {OUT / 'tickets.csv'}")
