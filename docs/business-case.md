# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Remote workers need to know which cafes offer wifi, power sockets and quiet enough conditions to work. The Udemy course "100 Days of Code" (day 88) supplies a SQLite database `cafes.db` with 21 London cafes and asks the participant to build a website on it. This project delivers a small website that lists the cafes, lets a visitor add a cafe and delete a cafe, runs with the Python standard library only, and is documented with screenshots and a three-language wiki so that fellow course participants can read, run and compare the solution.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: artifacts in the order Business Case, Stakeholder Analysis, Project Plan, milestones, tasks, code, each reviewed against its QC checklist with an `RC-*` record. Quality is described with ISO/IEC 25010:2023 characteristics. Code follows the `coding-conventions` skill (Python) and the layering of the `clean-architecture` skill.

## Problem Statement

- The course assignment is a learning exercise whose result is only valuable if it is complete, runnable and understandable by another participant.
- A solution that depends on a web framework, hidden configuration or a manual setup is hard for other participants to run and compare.
- The course describes the steps in lecture form, but a participant who reads a repository later cannot see what each step added unless the steps are captured visually and explained.

## Business Opportunity

A clean, dependency-free reference solution with a screenshot and an explanation for each build step helps other participants compare approaches, and shows the author's work to anyone browsing the repository.

## Objectives

1. **O1** Display all cafes of `cafes.db` on a web page, with name, location, map link, image and the facilities (sockets, toilet, wifi, calls), seats and coffee price.
2. **O2** Let a visitor add a new cafe through a form with validation.
3. **O3** Let a visitor delete a cafe, after a confirmation step.
4. **O4** Run on Python 3.13 or newer with no runtime dependency beyond the standard library, inside a local `.venv`.
5. **O5** Provide tests (pytest), a README with run and test instructions, source documented with Doxygen comments and a `Doxyfile`.
6. **O6** Publish a repository on the project's Gitea instance with a description and topics, and a wiki in English, Danish and Bahasa Malaysia that shows a screenshot of every build step and explains what the step taught.

## Scope

### In Scope

- A website with a cafe list, an add-cafe form and a delete action, served from the standard library.
- The supplied `cafes.db` kept in `data/` and a script to work on a copy for the demo and the tests.
- `constants.py` for constants, `pyproject.toml`, `.gitignore`, `.editorconfig`, `Doxyfile`.
- README from the framework template; wiki pages in `en`, `da` and `ms`; screenshots of each step, produced in a Docker container with a headless browser.
- A local static-analysis run with opengrep before every push.
- Repository description and topics on Gitea.

### Out of Scope

- User accounts, login, editing an existing cafe, search and map embedding.
- Hosting or deployment of the website.
- Any runtime third-party package (a web framework, an ORM, a template engine).
- Migrating the data from the original day 66 API.

## Expected Benefits

### Tangible Benefits

- A runnable solution that passes its tests on a clean clone with three documented commands.
- A repository that other participants can read: README, wiki in three languages and a screenshot per step.

### Intangible Benefits

- A reflection record of what each step taught, which supports the author's own learning.
- Practice with the review-driven workflow of the framework on a small project.

## Strategic Alignment

The project supports the author's goal of completing the "100 Days of Code" course with a result that is shareable and reviewed, and the goal of using the framework on real work.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | All cafes are listed | 21 of 21 rows of `cafes.db` are shown | An integration test counts the rendered cafes |
| 2 | Add and delete work | A new cafe is stored and a deleted cafe is gone | Integration tests against a temporary database |
| 3 | No runtime dependency | 0 packages under `[project] dependencies` | `pyproject.toml` review |
| 4 | Tests pass | 100 percent of pytest tests pass on Python 3.13 | `pytest` exit code 0 |
| 5 | Static analysis clean | 0 findings of severity error | opengrep run before each push |
| 6 | Documentation complete | README plus wiki in 3 languages, one screenshot per step | Page and screenshot count check |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The pound sign in `cafes.db` coffee prices is stored in a broken encoding, so prices show as an unreadable character | A visible defect in the list page | Inspect the stored bytes; decode on read in one function with a test, or document the data issue in the wiki |
| Screenshots cannot be taken on the host desktop | The documentation lacks pictures | Take them in a Docker container with a headless browser, as `framework/process/gui-testing.md` requires |
| The tokens in `.env` leak into the repository | Loss of control of the Gitea account | `.env` stays git-ignored, is never read by project code or tests and never printed |
| Python 3.14 is read from "greater than 3.13" but only 3.13 is installed | The project cannot be run by the author | Require `>=3.13`; recorded as an assumption and confirmed in the plan |
| The standard library server is less convenient than a framework | More code to write | Keep the layers small; it is also a learning goal and satisfies S03 |

## Assumptions

- "Python greater than 3.13" means Python 3.13 or newer; 3.13 is the installed interpreter.
- The Product Owner's language is English and the domain is IT.
- S01 is the Product Owner, developer and reviewer. In autonomous mode a review made as stand-in for S01 is recorded as not independent.
- The user can reach the Gitea host and has put the tokens in `.env`; the file is for personal use only.
- The "lecture steps" of the assignment are the build steps of this project: list, add, delete.

## Constraints

- Duration: the assignment and its documentation are delivered between 2026-11-20 and 2026-11-26 (about one week).
- Python 3.13 or newer, a local `.venv`, pytest, `pyproject.toml`, constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependency unless needed.
- No tooling attribution in any artifact, commit message or repository text.
- Doxygen comments in the source and a `Doxyfile`.
- Work is done on branches with pull requests, one per milestone.
- The wiki exists in English, Danish and Bahasa Malaysia.
- GUI work is tested in a Docker container, never on the host desktop.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| The author's time (about 120 minutes for the assignment plus documentation effort) | A reviewed, runnable, documented reference solution |
| Docker image pull for the screenshot step | Reproducible screenshots without taking the desktop |
| Translation effort for two extra wiki languages | Readers in three languages |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a complete, reviewed solution and a learning record |
| S02 | Udemy course participants; want readable, runnable code with the assignment's function names and run instructions |
| S03 | GitHub viewers; want a clear description, topics and README and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the data exists, and the standard library is enough to deliver every objective.
