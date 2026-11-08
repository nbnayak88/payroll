# SuccessLabs Academy · Payroll Atlas

[Open the workbook hub](https://nbnayak88.github.io/payroll/)

108 learning resources across 107 countries and regions: 65 country payroll workbooks, 42 focused replication workbooks, and the UK Payroll Configurator. Search by country or code, filter regions and resource types, and save favourites in your browser.

The original 62 country URLs and UK configurator URL are retained for existing LMS embeds. The hub covers all country entries in the pinned SAP 2H 2026 guide; [see the coverage audit](COUNTRY_COVERAGE.md) for the important difference between main-country and appendix replication scope.

## Updating content and the LMS

1. Update the appropriate country HTML in this repository, keeping its filename. Work prepared in ChatGPT must be explicitly committed to GitHub; editing a chat or a Library file alone does not update the live site.
2. Commit to `main`. The existing GitHub Pages deployment publishes the committed files automatically. Check the Pages workflow before considering the update live.
3. The LMS iframe continues using the same Pages URL. Learners see the deployed version on reload; the LMS does not need another file upload. A tab already open may need refresh, and normal browser/CDN caching can delay a change briefly.

Use this once for the full hub:

```html
<iframe src="https://nbnayak88.github.io/payroll/" title="SuccessLabs Academy Payroll Workbook Hub" width="100%" height="1000" style="border:0" loading="lazy" allow="fullscreen"></iframe>
```

Individual country URLs can also be embedded. Pages access does not require ChatGPT or GitHub login. This repository and GitHub Pages site are publicly accessible; LMS embedding alone is not access control. This does not change the separate private Sites preview.

## Source maintenance

The 45 additions generated on 8 November 2026 have a portable source system in `workbook-system/`. Edit `build_workbooks.py` for the three main-country profiles or the learning activities, and `appendix-blueprints.json` for the 42 appendix source records. The user’s existing UAE workbook supplies the shared UI template. Source files are kept separately from generated country pages.

```bash
python3 workbook-system/build_workbooks.py
python3 workbook-system/build_hub.py
```

Python 3 and Node.js are required for workbook generation and inline JavaScript syntax validation. These scripts run locally and make no external system changes. They regenerate only the 45 additions and the directory; they do not overwrite the original 62 workbooks or the UK configurator. Review the diff and commit the generated files to deploy.

For a directory change, edit `payroll-catalog.json`; for its appearance, edit `workbook-system/hub-template.html`, then run the hub builder. Comfortaa and the exact SuccessLabs logo are embedded, with the font licence retained. Country data, notes and reviewed-section progress are stored locally in the learner’s browser; use workbook backups when changing devices.

These are independent educational workbooks with fictional examples and explicit source/evidence boundaries. The mapping practice does not execute SAP. No affiliation with SAP or statutory authorities is claimed.

## Synthetic cases, page reflections and focus music

Every country workbook now includes an original fictional country case, four test workers, dated source events, mapping boundary fixtures and section-specific example tables. The UK configuration companion has matching fixtures for its 44 configuration pages. Country case JSON and worker CSV can be exported from each workbook; these exports contain only the deliberately synthetic TEST identifiers. Four contextual reflection statements — Affirmation, Visualization, Gratitude and Intention — follow the selected section or learning tool.

Payroll arithmetic examples are teaching inputs, not wage benchmarks, legal proration rules or verified statutory calculations. Tax, insurance, enrolment and payment approval still require independently evidenced country rules. Appendix editions remain replication practice. Their required-value and length checks are explicitly illustrative, rather than claims about delivered country field constraints.

Maintain the case content and page-specific prompts in `workbook-system/enrich_workbooks.py`; maintain shared behavior and appearance in `learning-enhancements.js` and `learning-enhancements.css`. Run `python3 workbook-system/enrich_workbooks.py` after editing these sources. Both main builders also run the enrichment step automatically. The operation is idempotent, embeds its assets in the standalone pages and preserves learner storage keys, source section numbering and existing learning records.

Focus music uses the owner-selected YouTube video through its standard embedded player. No raw video URL is printed in the workbook. The player loads only when the learner opens the focus-music panel, retains YouTube's controls and attribution, and stops when the panel is closed or the tab is hidden. The earlier generated melodies and reflection sound generators have been removed. External playback needs internet access and may depend on YouTube availability and the LMS content policy; no audio file is extracted or redistributed.
