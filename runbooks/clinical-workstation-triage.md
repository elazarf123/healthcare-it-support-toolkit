# Runbook: Clinical Workstation Triage

**Goal:** restore a clinician to a working session in under 10 minutes, without touching PHI you don't need.

## Triage order (fastest fix first)

1. **Session, not machine.** Most "my computer is broken" calls in clinical settings are stuck roaming/VDI sessions. Log the session off from the management console and have the user roam to the adjacent workstation — clinicians can be working again in 90 seconds while you fix the original machine.
2. **Peripherals with clinical impact next:** label printers, barcode scanners (med administration), signature pads. A broken scanner blocks bedside med verification — that's a patient-safety-adjacent ticket, not a convenience ticket. Prioritize accordingly.
3. **Profile issues:** clear the local profile cache only after confirming the user's data is roaming — never delete a local profile as a first move.
4. **Hardware swap:** if the machine itself is faulty, swap from spares pool and re-image. Chasing hardware ghosts at a nurses' station wastes clinical time.

## Rules that don't bend

- **Lock or log off any unattended session showing a chart** — then handle the ticket. Fixing the workstation while a patient chart is open to the hallway is itself a HIPAA finding (§164.310(b)-(c), workstation use & security).
- **No PHI screenshots in tickets.** Describe the error, crop to the dialog, or reproduce on a test patient.
- **Remote-control requires user consent per session**, and end the session when done — no lingering unattended remote connections at clinical workstations.
- Asset tags and encryption status get verified at every touch — an unencrypted device that stores PHI is a reportable event waiting to happen.

## When to stop troubleshooting and escalate

15-minute rule: if a SEV-affecting clinical workstation isn't functional in 15 minutes, deploy the spare and continue diagnosis off the floor. The unit needs a working station more than you need to win against this machine.
