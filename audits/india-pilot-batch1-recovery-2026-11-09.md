# India ECP Pilot — Batch 1 Recovery Audit (2026-11-09)

## Preservation baseline
- Payroll main commit inspected: `902b6bd544ca2ea1e739c7a865e57444e7db45d9`.
- Existing `India.html` blob SHA: `45d6d7bfdfd6b8877b9dcda62b39806ed8b5b03c`. Do not replace without a separate reviewed patch.
- PlayLab-108 latest inspected commit: `f91e17cb1a202fe39f32900a2c2fccdde273c54b`.

## Source-verified findings
- India workbook describes 48 configuration sections and six learning tools; navigation includes quiz, crossword, snakes and ladders, AVG reflection, flashcards and notes.
- Sidebar search targets 48 sections and tools; it does not advertise 108 games.
- Sidebar progress tracks reviewed workbook sections and explicitly says it is self-recorded, not executed test evidence.
- Crossword has a reveal button and associated handler in the source. This does not establish that browser interaction works.
- India.html contains no literal `PlayLab` integration reference in the inspected source.
- PlayLab-108 README still states its materials are specifications and examples rather than 108 deployed games; newer app.js contains a reusable runtime and content packs.

## Pending — do not mark complete
1. Integrate or link 108 playable PlayLab entries in the India pilot without changing the 48 payroll configuration sections.
2. Browser-test game launch, answer reveal, scoring, replay and keyboard accessibility for all 108 entries; capture reproducible failures.
3. Verify 108-game search and game-specific completion tracking separately from 48-section workbook progress.
4. Test PCC and EC–ECP replication learning evidence against workbook coverage.
5. Validate the deployed GitHub Pages build against the committed source.

## Acceptance criteria
- All 48 existing configuration sections remain intact.
- All 108 entries can launch and finish with correct feedback, scoring or outcome, and replay.
- Search finds game titles/IDs; progress is persisted and clearly distinguishes games from workbook review.
- No change to country-specific statutory configuration or workbook evidence without review.
- Publish exact commit, deployment URL and browser test evidence for each batch.

## Batch disposition
Read-only source audit completed; no gameplay functionality claimed verified. This additive audit file is the only Batch 1 change. Follow-up implementation must be small and separately tested.
