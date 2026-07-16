# HIPAA Quick Reference for IT Support Staff

Not legal guidance — an operational cheat sheet mapping daily IT support actions to the HIPAA Security Rule controls they touch.

## The rule of thumb

You are allowed to see PHI *incidentally* while doing your job. You are not allowed to browse, copy, share, or retain it. "Minimum necessary" applies to IT the same as to clinicians.

## Daily actions → controls

| When you... | You're touching | Do |
|---|---|---|
| Remote into a clinical workstation | §164.310(b) Workstation use | Get per-session consent; end session when done; never leave remote sessions unattended |
| Reset a password | §164.312(d) Authentication | Two-factor identity verification, logged in the ticket (see runbook) |
| Handle a device with local data | §164.310(d) Device & media controls | Verify encryption before it leaves the building; sanitize before disposal/reuse; keep chain of custody |
| See an unattended open chart | §164.310(c) Workstation security | Lock it. Then handle whatever you came for |
| Attach evidence to a ticket | §164.502(b) Minimum necessary | No PHI in screenshots; crop to the error, or reproduce on a test patient |
| Provision/deprovision accounts | §164.308(a)(3)-(4) Workforce security | Access matches role; termination = same-day disablement, not "next sweep" |
| Notice possible snooping or a breach | §164.308(a)(6) Incident procedures | Report to the privacy/security officer — that duty belongs to everyone, including IT |

## What gets IT people in actual trouble

Curiosity lookups (family, coworkers, public figures) — audit logs catch these and they are individually attributable. Sharing credentials "to save time." Emailing PHI to personal accounts to "work on it later." Disposing of drives without sanitization. Every one of these is a pattern from real OCR enforcement actions.

## Escalation phrase that always works

"I can't do that in a way that keeps us HIPAA-compliant, but here's what I can do instead: ___." Support's job is a compliant *yes*, not a flat no.
