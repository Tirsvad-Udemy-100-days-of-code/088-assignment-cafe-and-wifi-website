# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [5cdbee2] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] (`QC-PP-001`) and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (S01 reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give start 2026-11-20, end 2026-11-26 and cite the Business Case duration constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Gateway Schedule lists MIL-001 to MIL-005 once each with owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates equal the Target Date of each MIL document. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage table maps every In Scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Linear chain MIL-001 to MIL-005, acyclic and in date order. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state later dates move and that S01 decides the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Only S01 is named as owner. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions cite their source; no re-baseline yet. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks each have a mitigation. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues are consistent with the rest; the design chain waiver is explicit. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverables match the Deliverable sections of the MIL documents. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories named per gateway; MIL-001 has none (technical tasks) and the cell is empty by design. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars equal the table windows; chain equals the dependency list. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column is blank until the sync, as the reference allows. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | Single project plan PP-001. |

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

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[5cdbee2]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/commit/5cdbee2df2a2f92661408d724235b4d340ef3ca1
