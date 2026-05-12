import argparse
from urllib.parse import urlparse

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

COLUMNS = ['DateTime', 'NavigatedToUrl', 'PageTitle']


def load_history(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path, delimiter=',', names=COLUMNS)


def extract_domain(url: str) -> str:
    return urlparse(url).netloc


def cmd_top_domains(args):
    df = load_history(args.input)
    df['Domain'] = df['NavigatedToUrl'].apply(extract_domain)
    top_domains = df['Domain'].value_counts().head(args.top_n)

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_domains.index, y=top_domains.values,
                hue=top_domains.index, palette="viridis", legend=False)
    plt.title(f'Top {args.top_n} Visited Domains', fontsize=20)
    plt.xlabel('Domain', fontsize=16)
    plt.ylabel('Number of Visits', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()


def cmd_filter(args):
    df = pd.read_csv(args.input, delimiter=',')
    filtered = df[df['NavigatedToUrl'].str.contains(args.keyword, na=False)]
    filtered.to_csv(args.output, index=False, encoding=args.encoding)
    print(f"Saved {len(filtered)} rows to {args.output}")


def cmd_count(args):
    df = pd.read_csv(args.input, delimiter=',')
    url_counts = df['NavigatedToUrl'].value_counts()
    url_counts.to_csv(args.output, header=['Count'])
    print(f"Saved URL counts to {args.output}")


def main():
    parser = argparse.ArgumentParser(
        description='Browser history analyzer (tested with Edge exports)')
    subparsers = parser.add_subparsers(dest='command', required=True)

    p_top = subparsers.add_parser('top-domains', help='Show top visited domains chart')
    p_top.add_argument('input', help='Input CSV file')
    p_top.add_argument('--top-n', type=int, default=10,
                       help='Number of top domains to show (default: 10)')
    p_top.set_defaults(func=cmd_top_domains)

    p_filter = subparsers.add_parser('filter', help='Filter URLs by keyword')
    p_filter.add_argument('input', help='Input CSV file')
    p_filter.add_argument('keyword', help='Keyword to filter by')
    p_filter.add_argument('--output', default='filtered_urls.csv',
                          help='Output CSV file (default: filtered_urls.csv)')
    p_filter.add_argument('--encoding', default='utf-16',
                          help='Output file encoding (default: utf-16)')
    p_filter.set_defaults(func=cmd_filter)

    p_count = subparsers.add_parser('count', help='Count URL visits')
    p_count.add_argument('input', help='Input CSV file')
    p_count.add_argument('--output', default='url_counts.csv',
                         help='Output CSV file (default: url_counts.csv)')
    p_count.set_defaults(func=cmd_count)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
