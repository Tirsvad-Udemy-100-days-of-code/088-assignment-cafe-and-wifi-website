# MVC for server-rendered pages

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0002 |
| CrossReference | [BC-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

The `clean-architecture` skill names MVVM as the presentation pattern for a user interface and MVC for an API. The site is a user interface, but its pages are rendered on the server: each request is answered by a controller that fetches data and returns finished HTML. There is no view state kept between requests and no data binding, which is what a view model exists for. Options: (A) MVVM with a view model per page as the default says; (B) MVC with a controller per route and a view that renders a template.

## Decision

Use option B. Each route is handled by a controller function in `presentation`; views are pure functions from data to HTML. The layers `domain`, `application`, `infrastructure` and `presentation` of the skill stay as they are. This deviates from the default and is recorded here for the Product Owner.

## Consequences

**Positive:**

- The structure matches how the request is handled; no empty view-model classes.
- Controllers and views are small and testable without a server.

**Negative:**

- Differs from the default of the skill; a reader who expects MVVM must read this record.

Quality attributes: Maintainability and Interaction Capability: less ceremony for a three-page site.

## Affected Artifacts

- [BC-001] — objectives O1 to O3 are delivered through controllers
- [SA-001] — concern CN-004 (readable code)

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
