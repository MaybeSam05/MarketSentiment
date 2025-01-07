from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = NewsApiClient(os.getenv("NEWS_API_KEY"))
domains = ["cnn.com", "bbc.com", "nytime.com", "wsj.com", "forbes.com", "bloomberg.com", "reuters.com", "marketwatch.com", "cnbc.com", "financialpost.com", "investopedia.com", "ft.com", "seekingalpha.com", "businessinsider.com", "thestreet.com", "morningstar.com", "zacks.com", "yahoo.com", "benzinga.com", "investing.com", "economist.com", "nasdaq.com", "kiplinger.com", "fool.com", "barrons.com", "marketplace.org"]

def main():
    company = "Tesla"
    fetch_articles(company)

def fetch_articles(company_name):
    articles = newsapi.get_everything(
        q=company_name,
        from_param='2025-01-01',  # Start date
        to='2025-01-05',          # End date
        language='en',            # Language of the articles
        sort_by='publishedAt'     # Sort by most recent
    )
    
    count = 0
    for article in articles['articles']:
        if (article['title'] != "[Removed]") and any(domain in article['url'] for domain in domains):
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}\n")
            count += 1
            if count == 5:  # Stop after 5 iterations
                break

if __name__ == "__main__":
    main()