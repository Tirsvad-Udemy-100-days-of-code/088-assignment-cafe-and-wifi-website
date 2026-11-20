# MIL-002 Step 1: List cafes

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Purpose

Decide whether step 1, showing the cafes from `cafes.db` on a web page, is complete and understood.

## Deliverable

A running site whose home page lists all cafes, with unit and integration tests, a screenshot of the page and an English wiki page that explains what step 1 taught.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The home page shows every row of `cafes.db` | 21 cafes rendered in the integration test | Fewer or more |
| 2 | Prices show a readable currency sign | No replacement character in the HTML | A replacement character is shown |
| 3 | `pytest` passes with at least one test per function | Exit code 0 | Any failure |
| 4 | `docs/screenshots/step-1-list.png` exists and was made in Docker | File present | Missing |
| 5 | Source has Doxygen comments and the opengrep scan has no error finding | Both hold | Either fails |
| 6 | Pull request reviewed, `RC-*` says `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Tooling, layout and decisions must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O4, O5 | [BC-001] |
| US-001.01 | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Cafe entity and constants | Define the `Cafe` dataclass for the columns of the `cafe` table and the constants (database path, page title, host, port, template folder) in `constants.py`. Plain data, no framework. | No |  |
| 2 | Repository: get_all_cafes | Implement `get_all_cafes(connection)` with `sqlite3`, returning `Cafe` objects ordered by name; decode the stored price so the currency sign is readable (the file stores a broken pound sign). Unit tests use an in-memory database with the same schema. | Yes | US-001.01 |
| 3 | List page controller and view | A WSGI controller for `GET /` and an HTML view that renders a card per cafe with image, name, location, map link, wifi, sockets, toilet, calls, seats and price. Every value is escaped. | Yes | US-001.01 |
| 4 | Server entry point | `python -m cafe_wifi` starts `wsgiref` on the configured host and port against `data/cafes.db`; the database path can be overridden by an environment variable named in `constants.py`. | No |  |
| 5 | Tests for step 1 | pytest unit tests for the repository and view, and an integration test that calls the WSGI app and counts the cafes (21). | No |  |
| 6 | Screenshot of step 1 | Run the screenshot harness in Docker and save `docs/screenshots/step-1-list.png`. Environment: Docker container. | No |  |
| 7 | Wiki page Step 1 (English) | Write `docs/wiki/Step-1-List-Cafes.md` with the screenshot and what the step taught: reading SQLite with the standard library, escaping output, WSGI request handling. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
