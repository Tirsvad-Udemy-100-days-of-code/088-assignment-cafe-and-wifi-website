# User Story

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [SA-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Purpose and Scope

The stories of the whole project: one epic per gateway ([MIL-002] to [MIL-005]). The actors are the stakeholders of [SA-001]; no Use Case Diagram exists, because the website has one visitor role and the stories are short.

## Story List

### US-001.01 — List the cafes

**As a** visitor (remote worker), **I want** to see all cafes with their wifi, power and price details, **so that** I can choose a place to work.

**Acceptance Criteria**

- Given the database holds 21 cafes, when the home page is opened, then 21 cafe cards are shown.
- Given a cafe has a price stored with a currency sign, when it is shown, then the sign is readable.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-002] | fits one iteration | none | Must | The core of the assignment |

### US-001.02 — Add a cafe

**As a** visitor, **I want** to add a cafe through a form, **so that** the list grows with places I know.

**Acceptance Criteria**

- Given valid input, when the form is submitted, then the cafe is stored and shown in the list.
- Given an empty name, a bad URL or a name that exists, when the form is submitted, then field errors are shown and nothing is stored.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-003] | fits one iteration | none | Must | Named in the assignment |

### US-001.03 — Delete a cafe

**As a** visitor, **I want** to delete a cafe after a confirmation, **so that** wrong or closed places leave the list.

**Acceptance Criteria**

- Given a cafe, when deletion is confirmed with POST, then the cafe is gone from the list.
- Given an unknown id, when it is requested, then a not-found page is shown and nothing changes.
- Given any GET request, then nothing is deleted.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-004] | fits one iteration | none | Must | Named in the assignment |

### US-001.04 — Run the project and read the steps

**As a** course participant (S02), **I want** run instructions, a screenshot per step and an explanation of what each step taught, **so that** I can compare my solution with this one.

**Acceptance Criteria**

- Given a clean clone and Python 3.13, when the README commands are followed, then the site starts and the tests pass.
- Given the wiki, when a language is chosen (English, Danish, Bahasa Malaysia), then every step page shows its screenshot and its lessons.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Must | Serves S02 (CN-004, CN-005, CN-006) |

### US-001.05 — Judge the repository at a glance

**As a** GitHub viewer (S03), **I want** a clear description, topics and README and no runtime dependency, **so that** I can decide quickly whether the repository is useful.

**Acceptance Criteria**

- Given the repository front page, then description, topics and README are present.
- Given `pyproject.toml`, then no runtime dependency is listed.

| Traces to | Size | INVEST exceptions | Priority (MoSCoW) | Reason |
| --- | --- | --- | --- | --- |
| [MIL-005] | fits one iteration | none | Should | Serves S03 (CN-007, CN-008) |

## INVEST Check

All five stories are independent enough to be delivered in the order of the gateways, negotiable in detail, valuable to a named stakeholder, estimable, small (one iteration) and testable through their acceptance criteria. Exception: US-001.03 builds on the list of US-001.01 for its test data; the dependency is the gateway order.
---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-002]: ./milestones/mil-002-step-1-list-cafes.md
[MIL-003]: ./milestones/mil-003-step-2-add-cafe.md
[MIL-004]: ./milestones/mil-004-step-3-delete-cafe.md
[MIL-005]: ./milestones/mil-005-documentation-and-wiki.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
