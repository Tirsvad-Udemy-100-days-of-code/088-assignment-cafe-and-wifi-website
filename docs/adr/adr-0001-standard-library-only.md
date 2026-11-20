# Standard library only

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

GitHub viewers (S03, concern CN-008) want a repository with no runtime dependency, and course participants (S02) want code they can run with Python alone. The site needs HTTP handling, HTML output and a SQLite database. Options: (A) Flask with SQLAlchemy as in the course; (B) a small framework such as Bottle; (C) the standard library: `wsgiref` for HTTP, `sqlite3` for storage, `html.escape` and `string.Template` for output.

## Decision

Use option C. The site is a WSGI application served by `wsgiref`, with `sqlite3` for storage and no third-party runtime package. Test and lint tools are optional development extras.

## Consequences

**Positive:**

- `dependencies = []` in `pyproject.toml`; nothing to install to run the site.
- The code shows how HTTP, forms and SQL work underneath a framework, which supports the learning goal.

**Negative:**

- More code than with a framework: routing, form parsing and templating are written by hand.
- No automatic protection such as CSRF tokens; the small scope and local use accept this, and output is always escaped.

Quality attributes: Security: parameterised SQL and escaped output are rules of the code; Maintainability: few moving parts.

## Affected Artifacts

- [BC-001] — objective O4 and the constraint "no runtime dependency unless needed"
- [SA-001] — concerns CN-005 and CN-008

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
