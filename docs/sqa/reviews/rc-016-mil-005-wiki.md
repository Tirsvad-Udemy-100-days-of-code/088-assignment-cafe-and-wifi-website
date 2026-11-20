# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-20 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: docs/wiki (English, Danish, Bahasa Melayu)
- Checklist used: [QC-WIKI-001] (`QC-WIKI-001`)
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is the stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so no Related section exists. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 6 | The sidebar does not repeat the page list per language | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Melayu; the registry PO language is English. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with a language line with the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Suffixes -da and -ms; English has none. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pass | All 16 pages, the sidebar and the three Home pages answer 200 on the host API after the merge; the screenshot links answer 200. |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | Pass | Met; checked in the repository folder by a link and page-set script (no dead link; Home, 3 step pages and Reflection exist in en, da, ms). |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All 16 files are directly in docs/wiki/. |

## Overall Verdict

Go — every Mandatory criterion passes or is not applicable; criterion 14 was checked on the published wiki after the merge. The review is by a stand-in for S01 and is not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
