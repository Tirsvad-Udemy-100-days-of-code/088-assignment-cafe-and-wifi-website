# MIL-003 Step 2: Add a cafe

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Purpose

Decide whether step 2, adding a cafe through a form, is complete and understood.

## Deliverable

An add-cafe form with validation, persisted to the database, tests, screenshots and an English wiki page.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A valid form submission stores a new cafe and redirects to the list | The new cafe is listed after the redirect | Not stored or no redirect |
| 2 | An invalid submission (empty name, bad URL, duplicate name) shows errors and stores nothing | Errors shown, row count unchanged | Stored anyway |
| 3 | The form is protected from injection | Parameterised SQL and escaped output verified by tests | Any unescaped value |
| 4 | `pytest` passes; opengrep has no error finding | Both hold | Either fails |
| 5 | Screenshots of the form and the error state exist | Both PNGs present | Missing |
| 6 | Pull request reviewed, `RC-*` says `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The list page is the redirect target |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2 | [BC-001] |
| US-001.02 | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-23

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Repository: add_cafe | Implement `add_cafe(connection, cafe)` with a parameterised insert and a clear error for a duplicate name (the column is unique). Tests against an in-memory database. | Yes | US-001.02 |
| 2 | Form validation | A pure function that validates the submitted fields (required name and location, http(s) map and image URLs, boolean facilities, optional seats and price) and returns field errors. Length limits are constants. | Yes | US-001.02 |
| 3 | Add controller and view | `GET /add` shows the form; `POST /add` validates, stores and redirects (post/redirect/get), or shows the form again with errors and the entered values. | Yes | US-001.02 |
| 4 | Tests for step 2 | Unit tests for validation and `add_cafe`; integration tests for the form flow against a temporary database copy. | No |  |
| 5 | Screenshots of step 2 | Save `docs/screenshots/step-2-add-form.png` and `step-2-add-errors.png` from the Docker harness. Environment: Docker container. | No |  |
| 6 | Wiki page Step 2 (English) | Write `docs/wiki/Step-2-Add-Cafe.md` with the screenshots and what the step taught: form handling, validation, post/redirect/get, parameterised SQL. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
