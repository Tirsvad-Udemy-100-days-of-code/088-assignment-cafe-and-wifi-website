# MIL-004 Step 3: Delete a cafe

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether step 3, deleting a cafe, is complete and understood.

## Deliverable

A delete action with a confirmation step, tests, a screenshot and an English wiki page.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Confirming the deletion removes the cafe from the list | Row count decreases by one | The row remains |
| 2 | Deleting an unknown id gives a not-found page and changes nothing | 404 and row count unchanged | Error or change |
| 3 | A delete is only possible with a POST request | GET does not delete | GET deletes |
| 4 | `pytest` passes; opengrep has no error finding | Both hold | Either fails |
| 5 | A screenshot of the confirmation page exists | PNG present | Missing |
| 6 | Pull request reviewed, `RC-*` says `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Add and delete share the repository and the layout |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3 | [BC-001] |
| US-001.03 | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-24

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Repository: delete_cafe | Implement `delete_cafe(connection, cafe_id)` returning whether a row was removed. Tests for an existing and an unknown id. | Yes | US-001.03 |
| 2 | Delete controller and confirmation view | `GET /delete/<id>` shows a confirmation page naming the cafe; `POST /delete/<id>` deletes and redirects; an unknown id returns 404. | Yes | US-001.03 |
| 3 | Tests for step 3 | Unit and integration tests for the delete flow, including the rule that GET never deletes. | No |  |
| 4 | Screenshot of step 3 | Save `docs/screenshots/step-3-delete-confirm.png` from the Docker harness. Environment: Docker container. | No |  |
| 5 | Wiki page Step 3 (English) | Write `docs/wiki/Step-3-Delete-Cafe.md` with the screenshot and what the step taught: safe versus unsafe HTTP methods, confirmation, not-found handling. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
