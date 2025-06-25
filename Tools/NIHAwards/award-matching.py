import pandas as pd
import os
from glob import glob
from fuzzywuzzy import process

# === CONFIG ===
awards_folder = './'                      # Folder with award CSVs
trainee_file = '../PubMedAlerts/CDI-Trainees.csv'      # Path to CDI Trainees list
output_file = 'matched_awards_summary.csv'
match_threshold = 80                    # Fuzzy match threshold

# === Load trainees ===
trainees_df = pd.read_csv(trainee_file)
trainee_names = trainees_df['Name'].dropna().tolist()

# === Fuzzy matching helper ===
def find_best_match(name, candidates, threshold=90):
    if pd.isna(name):
        return None
    match, score = process.extractOne(name, candidates)
    return match if score >= threshold else None

# === Collect matches from all award files ===
all_matches = []

for file_path in glob(os.path.join(awards_folder, '*.csv')):
    print(f"\nProcessing {file_path}...")

    try:
        df = pd.read_csv(
            file_path,
            dtype=str,
            quotechar='"',
            skip_blank_lines=True,
            on_bad_lines='skip',  # For pandas >=1.3
            encoding='utf-8',
            skiprows=6            # NIH exports: skip metadata
        )
    except Exception as e:
        print(f"❌ Skipping {file_path}: {e}")
        continue

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Check for required column
    if 'contact pi / project leader' not in df.columns:
        print(f"❌ Skipping {file_path}: Missing 'Contact PI / Project Leader'")
        print(f"Columns found: {df.columns.tolist()}")
        continue

    # Fuzzy match to trainees
    df['matched trainee'] = df['contact pi / project leader'].apply(
        lambda x: find_best_match(x, trainee_names, threshold=match_threshold)
    )

    matched_df = df[df['matched trainee'].notnull()]
    if matched_df.empty:
        print("No matches in this file.")
        continue

    # Define desired fields and clean output
    wanted_cols = {
        'contact pi / project leader': 'Author',
        'project title': 'Title',
        'total cost': 'Total Cost',
        'funding mechanism': 'Funding Mechanism',
        'funding ic(s)': 'Funding IC(s)',
        'total cost ic': 'Total Cost IC',
        'project number': 'Project Number'
    }

    # Make sure matched_df columns match cleaned df
    matched_df.columns = df.columns

    available_cols = [col for col in wanted_cols if col in matched_df.columns]
    result = matched_df[available_cols].copy()
    result.columns = [wanted_cols[col] for col in available_cols]

    all_matches.append(result)
    print(f"✅ Found {len(result)} match(es) in {file_path}")

# === Combine and export ===
if all_matches:
    final_df = pd.concat(all_matches, ignore_index=True)
    final_df.to_csv(output_file, index=False)
    print(f"\n🎉 Done! {len(final_df)} total matches written to '{output_file}'")
else:
    print("\n❌ No matches found in any file.")
