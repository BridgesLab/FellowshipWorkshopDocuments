# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Fellowship writing workshop materials for the **Elizabeth Weiser Caswell Diabetes Institute (CDI)** at the University of Michigan. Primary audience: trainees writing NIH NRSA fellowship applications (F30, F31, F32). Published via GitHub Pages at `https://bridgeslab.github.io/FellowshipWorkshopDocuments`.

## Site Structure

Jekyll site with `jekyll-theme-primer`. The root markdown files (`Aims.md`, `Budget.md`, `Candidate.md`, etc.) are the core workshop guidance pages. `index.md` is the homepage. `_config.yml` sets the theme and GitHub Pages URL.

## Python Tools

Both scripts share the trainee list at `Tools/PubmedAlerts/CDI-Trainees.csv`. The CSV has `Name`, `Owner`, and `Member` columns — PubMed searches filter to rows where `Owner=FALSE` and `Member=TRUE`.

### PubMed Alert Parser (`Tools/PubmedAlerts/`)

Searches PubMed for publications by CDI trainees affiliated with U-M and generates a Markdown report.

**Setup (one time):**
```bash
conda env create -f Tools/PubmedAlerts/environment.yml
```

**Run:**
```bash
conda activate pubmed_alert_env
cd Tools/PubmedAlerts
python generate_pubmed_report.py --since 2024-12-31
```

Requires a `.env` file in `Tools/PubmedAlerts/` with:
```
NCBI_EMAIL=your@email.com
NCBI_API_KEY=your_key
```

Output: `YYYY-MM-DD_pubmed_report.md` sorted by publication date descending.

### NIH Award Matching (`Tools/NIHAwards/`)

Fuzzy-matches trainees against NIH award export CSVs to find funded awards.

**Run:**
```bash
conda activate pubmed_alert_env
cd Tools/NIHAwards
python award-matching.py
```

Place NIH Reporter CSV exports (skipping 6 metadata rows) in `Tools/NIHAwards/`. Output: `matched_awards_summary.csv`. The script expects a `Contact PI / Project Leader` column in the award CSVs.

## Branches

- `main` — stable/published content
- `2026-Summer-CDI` — current development branch for the 2026 summer workshop cycle
- `2025-Jan-CDI` — archived 2025 January session materials
