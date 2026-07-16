# Runbook: Password Reset with Identity Verification (Healthcare)

**Why this runbook exists:** the service desk is the softest target in a hospital. Vishing a password reset is how several major healthcare breaches started. A reset done without verification is an account compromise you performed for the attacker.

## Verification requirements (before ANY credential action)

Minimum two of the following, at least one from the "strong" column:

| Strong | Supporting |
|---|---|
| Callback to the phone number in the HR system (not the number that called you) | Employee ID matches directory |
| Manager confirms via known-good channel | Department + role match the account |
| In-person with badge | Answers to enrolled verification questions |

**Never acceptable:** caller ID alone, urgency ("I'm in the OR"), name-dropping, or the caller knowing personal details about the account holder. Clinical urgency is real — which is why the callback path must be *fast*, not skipped.

## Reset procedure

1. Verify identity per the table above. Log which two factors were used in the ticket.
2. Reset via the approved tool only; set **change-at-next-logon**.
3. Deliver the temporary credential over a different channel than the request came in on (e.g., request by phone → deliver to enrolled personal email or SSPR).
4. Confirm the user can authenticate; verify MFA enrollment is intact — an attacker who just failed at reset may try MFA re-enrollment next.
5. Ticket must record: requester, verification factors, channel of delivery. This is your audit trail under HIPAA §164.312(d) (person or entity authentication).

## Red flags → treat as security incident, not a ticket

- Caller refuses callback verification or pressures against procedure
- Reset request for a privileged/service account
- Second reset request for the same account within days
- Request for an executive or physician from an "assistant"

Escalation: hold the reset, notify security team with the caller's number and time. A false alarm costs 10 minutes; a compromised clinician account costs a breach notification.
