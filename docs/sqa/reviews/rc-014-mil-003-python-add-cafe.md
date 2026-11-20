# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: src/cafe_wifi and tests (MIL-003, step 2)
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | sqlite IntegrityError for a unique name is re-raised as DuplicateCafeError from the cause; other IntegrityErrors are re-raised. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 7 | Files, locks and connections are managed with context managers | Pass | The sqlite connection is closed after each request with a context manager. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | No logging in this step. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; the design chain was waived by the accepted plan (PP-001, Open Issues). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 81 tests: unit and integration on a database copy in tmp_path; includes injection, duplicate, oversized body and escape cases. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Validation rules, limits and messages are defined once (validate_new_cafe, constants.py). |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing from other layers; application imports domain; infrastructure imports domain; presentation is the only layer that composes them. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | One reason to change per module; the controller depends on the use case and a Protocol. Note: views receive the Cafe entity directly (no DTO), accepted for MVC in ADR-0002. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Packages domain, application, infrastructure, presentation under src/cafe_wifi; tests/unit and tests/integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | Checked by hand, ruff (check and format), mypy strict and 81 passing tests. |

## Overall Verdict

Go — every Mandatory criterion passes or is not applicable with a stated reason; no blocking finding. The review is by a stand-in for S01 and is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
