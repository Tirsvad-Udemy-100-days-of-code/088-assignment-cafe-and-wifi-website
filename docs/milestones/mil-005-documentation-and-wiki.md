# MIL-005 Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Purpose

Decide whether the documentation is complete: README, wiki in three languages, screenshots and reflection.

## Deliverable

A final README with screenshots, a wiki in English, Danish and Bahasa Malaysia with the same page set, a reflection page, the Doxygen run documented and a final scan.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The wiki has the same pages in `en`, `da` (suffix `-da`) and `ms` (suffix `-ms`) | Page sets are identical | A page is missing |
| 2 | Each step page contains its screenshot and a section on what was gained | Present in all languages | Missing |
| 3 | `_Sidebar.md` follows `framework/process/wiki.md` with the three languages | Conforms to `QC-WIKI-001` | Deviates |
| 4 | The README shows a screenshot for each step and the commands for `.venv`, run and tests | Present, `check-readme.sh` passes | Missing or failing |
| 5 | `doxygen Doxyfile` runs without warnings | 0 warnings | Warnings |
| 6 | Full opengrep scan and full pytest run pass | Both pass | Either fails |
| 7 | The wiki is enabled on the repository and published | Pages visible on the host | Not visible |
| 8 | Pull request reviewed, `RC-*` says `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | All three steps and their screenshots must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5, O6 | [BC-001] |
| US-001.04, US-001.05 | [US-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-26

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Wiki Home, sidebar and reflection (English) | Write `Home.md`, `_Sidebar.md` and `Reflection.md` (the assignment's reflection: approach, what was hard and easy, biggest learning, what to do differently). | No |  |
| 2 | Danish wiki translation | Translate every English page to Danish as `<Page>-da.md`, with the language line on each page. | No |  |
| 3 | Bahasa Malaysia wiki translation | Translate every English page to Bahasa Malaysia as `<Page>-ms.md`, with the language line on each page. | No |  |
| 4 | Enable and check the wiki on the host | Enable the wiki in the repository settings, merge, and verify that all pages and the sidebar show on the host. | No |  |
| 5 | Final README with screenshots | Add the three step screenshots with a short caption each, the Doxygen instructions and the links to the wiki. | Yes | US-001.04 |
| 6 | Repository front page check | Check the description, topics and README as a first-time viewer would see them, and that no runtime dependency is listed. | Yes | US-001.05 |
| 7 | Final scan and test run | Run the full pytest suite, the opengrep scan, `doxygen Doxyfile`, `check-readme.sh` and `check-editorconfig.sh` and record the results in the pull request. | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
