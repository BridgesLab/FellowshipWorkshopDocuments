# PubMed Alert Parser

The goal of this project is to parse a set of MCommunity files and generate pubmed search feeds for University of Michigan affilitated trainees.

## Setting Up the Environment

Set up a conda environment by running 

```bash
conda env create -f environment.yml
conda activate pubmed_alert_env
```

Only the second command needs to be run each subsequent time running the scripts

## Generating the Report

This script searches for articles since a particular date (here 2024-12-31)

```bash
python generate_pubmed_report.py --since 2024-12-31
```

This should generate a file called **YYYY-MM-DD-pubmed_report.md**, marked to when it was last run.

## Prompt

To parse this file try this prompt:

### Document structure rules

Each publication begins with a line starting with ## (this is the title).

Within that block, the following fields appear and must be parsed literally:

**Authors:** → a comma-separated list.

**Publication Date:** → extract YYYY-MM-DD.

**Searched Author:** → the full name specified for this record.

### Author matching rules

- Match the surname exactly.
- Match the initial(s) to the searched author’s initials.
- The author counts as first or last author only if they appear in position 1 or in the final position in the Authors list.

### Inclusion rule

Include a publication only if the searched author is first or last author according to the above matching rules.

### Extraction fields
For each included publication, extract:

- first_author
- last_author
- title
- publication_date
- relevance_diabetes_metabolism

Read the abstract; classify relevance_diabetes_metabolism as:

- “High” = directly about diabetes, β-cells, insulin, metabolism
- “Moderate” = adjacent fields (e.g., obesity, feeding behavior, relevant functional genomics)
- “Low/Blank” = unrelated

If no relevance, leave blank.

### Output format

- Provide a Markdown table
- Sort the rows by publication_date descending.
- Do not omit any required fields.

Final Output Template
Publication Date | First Author	| Last Author | Title | Relevance to Diabetes/Metabolism
