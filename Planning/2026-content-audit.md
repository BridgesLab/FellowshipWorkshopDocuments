# 2026 Course Prep: Content Audit for New PA Forms-I

Materials need to be updated to reflect the new fellowship application structure effective January 25, 2025 (PA-25-422 for F31, PA-25-423 for F32, Forms-I instructions).

Key structural changes:
- Review criteria consolidated from **5 → 3** scored criteria
- New document names ("Candidate's Goals, Preparedness, and Potential", "Training Activities and Timeline", "Research Training Project Strategy", "Sponsor(s) Commitment")
- **Removed sections**: Respective Contributions, Selection of Sponsor and Institution
- **Removed criteria**: biological variables (sex), adequate research funds, professional skills for career transition
- **Biosketch**: NIH now uses a Biographical Sketch Common Form (replacing separate fellowship biosketch); must be prepared via SciENcv; ORCID ID required and must be linked to eRA Commons profile. Effective for applications due on or after January 25, 2026; grace period (warnings only, no withdrawals) through May 2026 per NOT-OD-26-033.

---

## Tasks

### High Priority

- [x] **`Review_Criteria_NRSA.md`** — Complete rewrite around new 3-criteria system
  - Remove all old sub-questions
  - Structure around: (1) Candidate's Goals, Preparedness, and Potential; (2) Research Training Plan; (3) Commitment to Candidate, Mentoring and Training Environment
  - Remove rows referencing deleted criteria: adequate research funds, biological variables, professional skills for career transition
  - Remove link to `Sponsor_Statement.md#selection-of-sponsor-and-institution` (section no longer exists)

- [x] **`Research_Strategy.md`** — Remove deleted section and stale criterion
  - Remove description of "Relative Contributions" as a required 1-page document (section was removed in new PA)
  - Remove "Has the applicant presented adequate plans to address relevant biological variables, such as sex..." from review criteria (explicitly removed)
  - Update page title/description: "Research Strategy" → "Research Training Project Strategy"

### Medium Priority

- [x] **`Candidate.md`** — Replace old review criteria with new criteria language
  - Remove the 7 old sub-questions under "Review Criteria (NRSA - Need to Update for New Criteria)"
  - Replace with relevant sub-questions from the new **Candidate's Goals, Preparedness, and Potential** criterion

- [x] **`Candidate.md`** — Update biosketch guidance for NIH Common Form
  - Updated to reference Biographical Sketch Common Form (no separate fellowship biosketch)
  - SciENcv and ORCID ID requirements noted
  - Old forms-h biosketch instructions link removed

- [x] **`Training_Plan.md`** — Replace old review criteria with new criteria language
  - Remove the 12 old sub-questions under "Review Criteria (Need to Update for new PA)"
  - Replace with relevant sub-questions from the new **Research Training Plan** criterion
  - Remove "Will the training plan provide the professional skills needed for the candidate to transition..." (criterion was removed)

- [x] **`Sponsor_Statement.md`** — Update criteria and section format; updated A-E to new Sponsor(s) Commitment structure per Forms-I; updated Letters section to link to Supporting_Documents.md
  - Remove the 14 old sub-questions under "Review Criteria (Need to Update for new PA)"
  - Replace with relevant sub-questions from the new **Commitment to Candidate, Mentoring and Training Environment** criterion
  - Update "Suggested Format" sections A–E to reflect the new **Sponsor(s) Commitment** structure per Forms-I
  - Update instructions link from old forms-e URL to Forms-I: `https://grants.nih.gov/grants/how-to-apply-application-guide/forms-i/fellowship-forms-i.pdf`

### Low Priority

- [x] **`index.md`** — Update links and schedule dates
  - PA links and 2026 submission deadline were already updated on this branch
  - Fixed typo in schedule table: `Research_Stragegy.md` → `Research_Strategy.md`
  - Fixed broken fellowship instructions URL (had a line-break mid-URL)

- [x] **`Budget.md`** — Fix link and verify rates
  - Update resources link from `fellowship-forms-h.pdf` → `fellowship-forms-i.pdf`
  - Updated stipend rates per [NOT-OD-25-105](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-105.html): F31 $28,788; F32 Year 1 $62,232 / Year 2 $62,652 / Year 3 $63,120

### Manual Review Required

- [x] **`Documents/Images/`** — Review workshop diagrams and timeline images for accuracy against new PA structure; source files are Adobe Illustrator PDFs with PNG exports.
  - `Workshop Structure.png` — no changes needed
  - `Aims Structure.png` — no changes needed
  - `NRSA_Criteria_Changes.png` — no changes needed (correctly shows old→new criteria transition)
  - `Workshop Timeline.png` — updated session names; "Sponsor Statement" colloquial name retained intentionally
  - `Training Plan Documents.pdf/png` — updated: "Selection of Sponsor and Institution" replaced with "Institutional Environment Description"; "Sponsor's Commitment" / "Institutional Environment Description" labels now correct
  - [ ] Minor: left circle label reads "Sponsor's Commitment" — consider updating to "Sponsor(s) Commitment" for consistency with text

---

## Reference Links

- [PA-25-422 (F31)](https://grants.nih.gov/grants/guide/pa-files/PA-25-422.html)
- [PA-25-423 (F32)](https://grants.nih.gov/grants/guide/pa-files/PA-25-423.html)
- [Fellowship Forms-I Instructions (PDF)](https://grants.nih.gov/grants/how-to-apply-application-guide/forms-i/fellowship-forms-i.pdf)
- [Biographical Sketch Common Form](https://grants.nih.gov/grants-process/write-application/forms-directory/biographical-sketch-common-form)
- [NOT-OD-26-033 (biosketch grace period)](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-033.html)
- [Internal comparison doc](F31_PAF_Comparason.md)
