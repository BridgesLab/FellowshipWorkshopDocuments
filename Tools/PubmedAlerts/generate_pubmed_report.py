from Bio import Entrez
import time
import os
import csv
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

Entrez.email = os.getenv("NCBI_EMAIL")
Entrez.api_key = os.getenv("NCBI_API_KEY")

def load_filtered_names(filepath):
    names = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Owner'].strip().upper() == 'FALSE' and row['Member'].strip().upper() == 'TRUE':
                names.append(row['Name'].strip())
    return names

def search_author_papers(author_name, affiliation="University of Michigan", retmax=20):
    # Skip empty or whitespace-only names
    if not author_name or not author_name.strip():
        return []
    
    # Format author name: assume "First Middle Last" or "Last, First"
    parts = author_name.split()
    last = parts[-1]
    first_initial = parts[0][0]
    query = f'{last} {first_initial}[Author] AND "{affiliation}"[Affiliation]'
    
    handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax, sort='pub date')
    record = Entrez.read(handle)
    handle.close()
    
    return record['IdList']

def fetch_articles(pmid_list):
    if not pmid_list:
        return []
    ids = ",".join(pmid_list)
    handle = Entrez.efetch(db="pubmed", id=ids, retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    return records['PubmedArticle']

def extract_article_info(article):
    medline = article['MedlineCitation']
    article_info = medline['Article']
    title = article_info.get('ArticleTitle', 'No title')
    abstract_list = article_info.get('Abstract', {}).get('AbstractText', ['No abstract'])
    abstract = " ".join(abstract_list) if isinstance(abstract_list, list) else abstract_list

    authors = []
    umich_authors = []
    all_affiliations = []

    # Loop through authors and check their affiliations
    for author in article_info.get('AuthorList', []):
        if 'LastName' in author and 'Initials' in author:
            name = f"{author['LastName']} {author['Initials']}"
            authors.append(name)

            # Check if this author has a Michigan affiliation
            if 'AffiliationInfo' in author:
                affils = [a['Affiliation'] for a in author['AffiliationInfo'] if 'Affiliation' in a]
                all_affiliations.extend(affils)
                if any("University of Michigan" in aff for aff in affils):
                    umich_authors.append(name)

    pub_date = "Unknown"
    if 'DateCompleted' in medline:
        d = medline['DateCompleted']
        pub_date = f"{d['Year']}-{d['Month']}-{d['Day']}"
    elif 'ArticleDate' in article_info and article_info['ArticleDate']:
        d = article_info['ArticleDate'][0]
        pub_date = f"{d.get('Year', '0000')}-{d.get('Month', '00')}-{d.get('Day', '00')}"

    return {
        'title': title,
        'abstract': abstract,
        'authors': authors,
        'umich_authors': umich_authors,
        'affiliations': all_affiliations,
        'pub_date': pub_date
    }

def generate_report(author_names, affiliation="University of Michigan", since_date=None):
    all_articles = []

    print(f"🔍 Starting PubMed search for {len(author_names)} authors...")

    for i, author in enumerate(author_names, 1):
        print(f"\n[{i}/{len(author_names)}] Searching for articles by: {author}")
        pmids = search_author_papers(author, affiliation)
        print(f"    ➤ Found {len(pmids)} PMIDs")
        if not pmids:
            continue

        articles = fetch_articles(pmids)
        print(f"    ➤ Fetching {len(articles)} articles...")

        # Format searched author's name to "Last Initials"
        parts = author.strip().split()
        if len(parts) < 2:
            continue  # skip malformed names
        last_name = parts[-1]
        initials = ''.join(p[0] for p in parts[:-1])
        searched_name = f"{last_name} {initials}"

        for j, art in enumerate(articles, 1):
            info = extract_article_info(art)

            # ✅ Require that the searched author is *affiliated* with Michigan
            if searched_name not in info['umich_authors']:
                continue

            # ✅ Filter by date if specified
            try:
                pubdate = datetime.strptime(info['pub_date'], "%Y-%m-%d").date()
                if since_date and pubdate < since_date:
                    continue
            except:
                continue  # skip if pub_date is invalid

            info['author_searched'] = author
            all_articles.append(info)
            print(f"        → Parsed article {j}/{len(articles)}: {info['title'][:60]}...")

        time.sleep(0.34)  # Respect NCBI rate limits

    print(f"\n✅ Done! Collected {len(all_articles)} articles after filtering.")

    # Sort by pub date (newest first)
    all_articles.sort(key=lambda x: x['pub_date'], reverse=True)

    # Generate Markdown report
    report = f"# PubMed Report for {affiliation} — {datetime.today().strftime('%Y-%m-%d')}\n\n"
    for art in all_articles:
        report += f"## {art['title']}\n"
        report += f"**Publication Date:** {art['pub_date']}\n\n"
        report += f"**Authors:** {', '.join(art['authors'])}\n\n"
        report += f"**Searched Author:** {art['author_searched']}\n\n"
        report += f"**Abstract:** {art['abstract']}\n\n---\n\n"

    return report


if __name__ == "__main__":
    # Parse command-line argument
    parser = argparse.ArgumentParser(description="Generate PubMed report for group authors")
    parser.add_argument(
        "--since",
        type=str,
        help="Filter articles published on or after this date (YYYY-MM-DD)",
        default=None
    )
    args = parser.parse_args()

    since_date = None
    if args.since:
        try:
            since_date = datetime.strptime(args.since, "%Y-%m-%d").date()
            print(f"📅 Filtering articles published since: {since_date}")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            exit(1)

    trainee_names = load_filtered_names("CDI-Trainees.csv")
    md_report = generate_report(trainee_names, since_date=since_date)
    out_filename = f"{datetime.today().strftime('%Y-%m-%d')}_pubmed_report.md"
    with open(out_filename, "w", encoding="utf-8") as f:
        f.write(md_report)
    print(f"\n✅ Report saved to {out_filename}")
