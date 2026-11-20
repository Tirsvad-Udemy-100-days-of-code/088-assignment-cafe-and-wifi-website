# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's traceability can be checked. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | SA-001, PP-001, US-001 | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | PP-001 | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | MIL-001..MIL-005 | [RC-003] |
| [US-001] | User Story | en | it | [BC-001] | MIL-002..MIL-005 | [RC-004] |
| [MIL-001] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-005] |
| [MIL-002] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-006] |
| [MIL-003] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-007] |
| [MIL-004] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-008] |
| [MIL-005] | Milestone | en | it | [BC-001], [PP-001] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | MIL-002, MIL-003, MIL-004 | - | - | Covered |
| CN-002 | MIL-001 to MIL-005 | - | - | Covered |
| CN-003 | MIL-002 to MIL-005 (wiki step pages) | - | - | Covered |
| CN-004 | MIL-002 to MIL-004 | - | - | Covered |
| CN-005 | MIL-001, MIL-005 | - | - | Covered |
| CN-006 | MIL-002 to MIL-005 | - | - | Covered |
| CN-007 | MIL-001, MIL-005 | - | - | Covered |
| CN-008 | MIL-001 | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None | - | Closed | - |

## Coverage Notes

No ADR, test plan, use case or design artifact exists yet; `-` in a Decisions or Quality check cell means none exists yet. Source code and its review records are added when code is reviewed.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[US-001]: ../user-stories.md
[MIL-001]: ../milestones/mil-001-baseline.md
[MIL-002]: ../milestones/mil-002-step-1-list-cafes.md
[MIL-003]: ../milestones/mil-003-step-2-add-cafe.md
[MIL-004]: ../milestones/mil-004-step-3-delete-cafe.md
[MIL-005]: ../milestones/mil-005-documentation-and-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-user-stories.md
[RC-005]: ./reviews/rc-005-mil-001-baseline.md
[RC-006]: ./reviews/rc-006-mil-002-step-1-list-cafes.md
[RC-007]: ./reviews/rc-007-mil-003-step-2-add-cafe.md
[RC-008]: ./reviews/rc-008-mil-004-step-3-delete-cafe.md
[RC-009]: ./reviews/rc-009-mil-005-documentation-and-wiki.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
