# MIL-001 Baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Purpose

Decide whether the repository, the tooling and the plan documents are in place so that feature work can start.

## Deliverable

A repository on the Gitea host with description and topics; `pyproject.toml`, `constants.py`, `.gitignore`, `.editorconfig`, `Doxyfile`, a README from the framework template, a screenshot harness that runs in Docker, and the decision records for the architecture.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The repository has a description and at least five topics on the Gitea host | Both are visible in the repository API | Either is empty |
| 2 | `pip install -e .[dev]` and `pytest` run in a fresh `.venv` | Exit code 0 on both commands | Any command fails |
| 3 | `pyproject.toml` declares no runtime dependency and `requires-python >= 3.13` | Both hold | A runtime dependency is listed |
| 4 | `check-editorconfig.sh` and `check-readme.sh` pass | Both exit 0 | Either fails |
| 5 | The opengrep run over the repository reports no error finding | 0 findings of severity error | Any error finding |
| 6 | The screenshot harness produces a PNG of a static page inside a Docker container | A PNG exists in the results folder | No PNG |
| 7 | Pull request reviewed, `RC-*` says `Go` | Go | No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O4, O5, O6 | [BC-001] |
| CN-002, CN-005, CN-007, CN-008 | [SA-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-21 — within the days the assignment needs.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set repository description and topics | Use the Gitea API with the repository token from `.env` (read by the shell only, never by project code, never printed) to set a one-line description and topics such as `python`, `sqlite`, `wsgi`, `cafe`, `wifi`, `udemy`, `100-days-of-code`. Satisfies CN-007. | No |  |
| 2 | Scaffold project files | Create `pyproject.toml` (Python 3.13 or newer, pytest config, no runtime dependencies, an optional `dev` extra with pytest), `src/cafe_wifi/constants.py`, the `src/` and `tests/` layout, a Python `.gitignore` that also ignores `.env`, `.venv` and the prompt-log folder, and the root `.editorconfig` from the framework baseline. `data/cafes.db` is already in the repository folder and is kept as the reference data. | No |  |
| 3 | Document the virtual environment | Write the commands for `python -m venv .venv`, activation on Windows and Linux, `python -m pip install --upgrade pip`, `pip install -e .[dev]`, running the site and running pytest, for use in the README and the wiki. | No |  |
| 4 | Add Doxyfile and Doxygen comment style | Add a `Doxyfile` for Python (`EXTRACT_ALL`, input `src`) and fix the Doxygen comment convention (`##` blocks with `@brief`, `@param`, `@return`) used in all source files. | No |  |
| 5 | Write ADR 0001 and 0002 | ADR 0001: standard library only (`wsgiref`, `sqlite3`, `string.Template`) so there are no runtime dependencies (CN-008). ADR 0002: MVC for the server-rendered pages, because each page is a request answered by a controller; the `clean-architecture` skill defaults to MVVM for a user interface, so this deviation is recorded for the Product Owner. | No |  |
| 6 | Local static analysis with opengrep | Add `scripts/opengrep-scan.ps1` and `.sh` that call `~/.opengrep/cli/latest/opengrep.exe` over `src`, `tests` and `scripts`, and document that it is run before every push to Gitea. | No |  |
| 7 | Screenshot harness in Docker | Write `scripts/screenshots/` with a Dockerfile (Python plus a headless Chromium) and a script that starts the site against a temporary copy of the database and writes PNGs to `docs/screenshots/`. It runs only in a Docker container, never on the host desktop (`framework/process/gui-testing.md`). Environment: Docker container. | No |  |
| 8 | README from the framework template | Create `README.md` from `framework/templates/README-template.md` with overview, requirements, setup (`.venv`), run, tests and the appendix of project documents; check it with `check-readme.sh`. | No |  |
| 9 | Install git hooks, skills and plan gate | Run `install-git-hooks.sh --enable-plan-gate` and `install-skills.sh`, and record the prompts of the session as the framework's prompt-log process says (the folder is git-ignored). | No |  |

---

[BC-001]: ../business-case.md
[US-001]: ../user-stories.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
