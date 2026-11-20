# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-004 |
| CrossReference | [US-001], [QC-US-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Artifact Under Review

- Instance reviewed: [US-001]
- Checklist used: [QC-US-001] (`QC-US-001`) and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (S01 reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Follows INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) | Pass | INVEST Check section; one stated exception. |
| 2 | Written in "As a / I want / So that" form | Pass | Every story uses As a / I want / so that. |
| 3 | Clear, testable acceptance criteria are included | Pass | Each story has Given/When/Then criteria. |
| 4 | Traceable to a use case or epic | Pass | Traces to a gateway (an epic) per story. |
| 5 | Story is sized to fit within a single iteration | Pass | Size column: fits one iteration. |
| 6 | Story statement avoids technical implementation detail | Pass | Statements name goals, not implementation. |
| 7 | Role named in the story matches an actor defined in the Use Case Diagram | N-A | No Use Case Diagram exists; roles (visitor, S02, S03) are stakeholders of [SA-001]. Not applicable until a UCD exists. |
| 8 | A story with more than one actor goal is split into use cases, one per actor goal, and each use case names the story it comes from | Pass | Each story has one actor goal. |
| 9 | The story has a priority (MoSCoW: Must, Should, Could, Won't now) with the reason beside it | Pass | MoSCoW priority and reason on every story. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has Language is `en` and Domain is `it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register of this type per registry; text matches (executive English for BC/PP/MIL, professional English for SA/US). |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary exists yet; terms are the plain IT terms of the domain, used consistently (cafe, repository, milestone). |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin file exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no earlier language. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Reviewer S01 reads English and knows the IT domain (is the Product Owner). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | WSGI, ADR, MVC, MVVM and similar are named in the text or described; acceptable for the IT domain. |

## Overall Verdict

Go — every Mandatory criterion passes or is not applicable with a stated reason; no blocking finding. The review is by a stand-in for S01 and is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[US-001]: ../../user-stories.md
[QC-US-001]: ../../../framework/qc/artifacts/qc-user-story.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
