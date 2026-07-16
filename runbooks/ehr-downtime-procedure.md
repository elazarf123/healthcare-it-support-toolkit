# Runbook: EHR Downtime Procedure

**Scope:** Unplanned EHR outage (application, database, or network) affecting clinical users.
**Audience:** IT support / service desk. Clinical downtime forms are owned by nursing leadership; this runbook covers the IT side.

## Severity classification (first 5 minutes)

| Level | Definition | Examples | Escalation |
|---|---|---|---|
| SEV-1 | EHR unavailable enterprise-wide OR patient-safety impact | Full outage, meds/allergies unreadable | Page on-call engineer + notify house supervisor immediately |
| SEV-2 | Degraded for a department or major function | Lab results not filing, one clinic down | On-call engineer within 15 min |
| SEV-3 | Individual users affected, workaround exists | One workstation, one printer | Standard queue, same-day |

## Immediate actions (IT)

1. **Confirm scope before declaring.** Test from 2+ workstations on different subnets and 1 VDI session. One user ≠ outage.
2. **Check the obvious tier first:** Citrix/VDI session health → application services → database listener → recent change window (was anything deployed?).
3. **Declare downtime** via the incident bridge if SEV-1/SEV-2. Note declaration time — it drives the downtime-documentation window clinicians must backfill.
4. **Activate downtime workstations.** Verify BCA (business continuity access) machines are printing current census + MAR snapshots. These machines are the clinical fallback — treat their availability as part of the incident, not an afterthought.
5. **Communicate on a cadence, not on demand:** status update every 30 min to unit leadership even if the update is "still investigating." Silence generates duplicate tickets and phone storms.

## HIPAA considerations during downtime

- Downtime paper forms contain PHI — they must be collected and reconciled into the EHR after recovery, not left at stations.
- Do **not** stand up ad-hoc workarounds that move PHI outside approved systems (personal email, texting patient details, shadow spreadsheets). Fast is not a defense in an OCR audit.
- Log who was given break-glass or elevated access during the incident; revoke and review within 24 hours of recovery.

## Recovery & closure

1. Validate core workflows with a clinical super-user *before* announcing recovery: chart open, order entry, result review, medication administration.
2. Announce recovery + the backfill window for paper documentation.
3. Post-incident review within 5 business days: timeline, root cause, what monitoring would have caught it earlier.

## Common failure I've seen from the support side

The outage is declared over when the application is up — but interface engines (lab, pharmacy) are still queued/backed up. Verify interface backlogs are draining before closing the incident, or results will "go missing" for hours and generate a second wave of tickets.
