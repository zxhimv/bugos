# Quizlet PREPARE_ONLY Known-Issue Map

Status: PREPARE_ONLY

No Quizlet-specific known-issue list was retrieved. This map only captures local triage categories to prevent premature submission or unsafe work.

| Category | PREPARE_ONLY handling |
| --- | --- |
| Scope-dependent observations | Block until authoritative scope is verified. |
| Account, enrollment, billing, or classroom workflows | Block until explicit permission and test-account rules are verified. |
| Authentication and session behavior | Block. Do not request, collect, alter, or reset credentials. |
| Rate limits, abuse prevention, and automation | Block. Do not run automated checks or generate traffic. |
| Privacy or data exposure observations | Block until evidence can be handled without secrets, personal data, or unauthorized access. |
| Browser-only UI behavior | Keep as local notes only unless impact and scope are verified later. |
| Reports requiring exploit steps or payload strings | Block under this intake. |
| Duplicate or previously known findings | Unknown. Requires authoritative program guidance before any report draft can advance. |

## Local Notes

- This file does not assert that any issue exists.
- This file does not contain target data, payloads, exploit details, credentials, or externally sourced program rules.
- Future authorized work may update known-issue guidance after authoritative policy review, but must not enable automatic submission, target interaction from this intake pack, scanners, exploits, payloads, credentials, password reset actions, crawling, browser automation, or submission automation.
