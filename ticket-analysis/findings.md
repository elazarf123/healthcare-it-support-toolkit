# Ticket Analysis — Findings & Recommendations

Dataset: 640 tickets over 90 days (synthetic). Analysis in `analyze_tickets.py`; chart in `ticket_volume_sla.png`.

## What the data says

1. **`EHR access / login` is the volume leader** (198.0 tickets). High-volume, low-complexity categories are the automation target list.
2. **`Medical device connectivity` breaches SLA most** (51.7% of tickets). These involve vendor coordination — the fix is a different SLA tier and a vendor-escalation runbook, not pushing techs harder.
3. **`Printer / label printer` has the highest reopen rate** (14.8%). Reopens are a fix-quality signal: recommend a permanent-fix checklist (driver version, tray config, test page from the EHR, not just Windows).
4. **Password resets: 79 tickets at 10 min median.** Every one is self-service-able. SSPR enrollment push would remove roughly 79 tickets/quarter from the queue.

## Recommended actions (priority order)

| Action | Effort | Impact |
|---|---|---|
| SSPR enrollment campaign for password resets | Low | Removes ~13% of queue |
| Vendor-escalation runbook + separate SLA for device connectivity | Low | Fixes worst breach category |
| Printer permanent-fix checklist | Low | Cuts highest reopen rate |
| Knowledge-base articles for top 3 EHR login failure modes | Medium | Shifts volume leader left |