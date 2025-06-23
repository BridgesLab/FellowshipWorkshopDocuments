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