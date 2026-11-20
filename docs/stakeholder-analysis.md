# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This analysis names the people who care about the project, classifies them by power and interest (Mendelow grid) and records their concerns in business language with a FURPS+ attribute, so that the Business Case ([BC-001]) objectives and the milestones can be traced to them.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A complete, reviewed solution and a record of what was learned |
| S02 | Udemy course participants | Fellow learners who share and compare code | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | MEDIUM | Monitor | A clear description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews every artifact.
- **Keep Informed (S02):** cannot change the project but is its main audience; they get the README and wiki.
- **Monitor (S03):** arrives occasionally; the repository front page must work without any contact.
- **Keep Satisfied:** no stakeholder.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The website lists, adds and deletes cafes as the assignment asks | Functionality |
| CN-002 | S01 | Each step is reviewed and traceable to a milestone and a branch | Supportability |
| CN-003 | S01 | The learning of each step is written down | Supportability |
| CN-004 | S02 | The code is readable and uses the assignment's function names | Supportability |
| CN-005 | S02 | The README tells how to create the `.venv`, run the site and run the tests | Usability |
| CN-006 | S02 | A screenshot and an explanation exist for every step, in more than one language | Usability |
| CN-007 | S03 | The repository has a description, topics and a clear README | Usability |
| CN-008 | S03 | Nothing has to be installed beyond Python itself | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat | At the start | The plan, as the dry run of the sync, for acceptance | Planning |
| CR-002 | Pull request | One per milestone | Reviewed changes and screenshots | Every milestone |
| CR-003 | Chat | At the end of the run | Summary of merged pull requests, `RC-*` verdicts and stand-in decisions | Final |
| CR-004 | README and wiki | At each release | Run instructions, screenshots, lessons | Documentation milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| A web framework would shorten the code (S01) but adds runtime dependencies (S03, CN-008) | S01, S03 | Use the standard library; recorded in an ADR |
| Three wiki languages cost effort (S01) but widen the audience (S02) | S01, S02 | English is authoritative; Danish and Bahasa Malaysia follow page by page with the same page set |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | O1, O2, O3 ([BC-001]) |
| S01 | CN-002, CN-003 | O5, O6 ([BC-001]) |
| S02 | CN-004, CN-005 | O4, O5 ([BC-001]) |
| S02 | CN-006 | O6 ([BC-001]) |
| S03 | CN-007 | O6 ([BC-001]) |
| S03 | CN-008 | O4 ([BC-001]) |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Accepted by S01 (stand-in, not independent) | |

---

[BC-001]: ./business-case.md
