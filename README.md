# 🚀 Cafe and Wifi Website

A small website that lists cafes with wifi and power sockets for remote working. It is the solution to the day 88 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp", and it needs nothing but Python.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The site reads the supplied SQLite database `data/cafes.db` (21 London cafes) and lets a visitor list, add and delete cafes. It is built in three steps, and each step has a screenshot and a wiki page that explains what it taught.

| Folder | Holds |
| --- | --- |
| `src/cafe_wifi/` | The website: constants, data access, controllers and views |
| `tests/` | The pytest tests |
| `data/` | The supplied database `cafes.db` |
| `docs/` | The project documents, the wiki pages and the screenshots |
| `scripts/` | The static analysis and screenshot scripts |

The site has no runtime dependency: it uses the Python standard library only (`wsgiref`, `sqlite3`). The source is documented with Doxygen comments, and a `Doxyfile` is included.

## 📋 Requirements

- Python 3.13 or newer, to run the site and the tests.
- Git, to clone the repository.
- Optional: Doxygen, to build the source documentation; Docker, to take the screenshots; opengrep, to scan the code before a push.

## 🛠️ Setup

Create a local virtual environment, update `pip`, and install the project with its test tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

```bash
python -m cafe_wifi
```

Then open <http://127.0.0.1:8000>. The database path can be changed with the environment variable `CAFE_WIFI_DB`. Pages are added step by step; see the wiki for what each step contains.

## 🧪 Tests

```bash
python -m pytest
```

Before a push, run the static analysis and the style checks:

```bash
bash scripts/opengrep-scan.sh
python -m ruff check src tests
```

The source documentation is built with `doxygen Doxyfile` and written to `docs/doxygen/`. The screenshots are taken in a Docker container with `bash scripts/screenshots/run.sh --steps 1 2 3` (on Windows: `pwsh scripts/screenshots/run.ps1 --steps 1 2 3`), never on the desktop.

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
