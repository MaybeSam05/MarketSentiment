from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

load_dotenv()
newsapi = NewsApiClient(os.getenv("NEWS_API_KEY"))

def fetch_articles(company_name, domains, start, end):
    my_dict = {}
    articles = newsapi.get_everything(
        q=company_name,
        from_param=start,
        to=end,
        language='en',
        sort_by='relevancy'
    )
    count = 0
    for article in articles['articles']:
        if (article['title'] != "[Removed]") and any(domain in article['url'] for domain in domains):
            my_dict[article['title']] = article['url']
            count += 1
            if count == 5:
                break
    return my_dict

def read_articles(my_dict):
    articleToContent = {}
    for key, url in my_dict.items():
        article = Article(url)
        article.download()
        article.parse()
        articleToContent[key] = article.text
    return articleToContent

def analyze_sentiment(my_dict):
    analyzer = SentimentIntensityAnalyzer()
    articleToSentiment = {}
    for key, text in my_dict.items():
        articleToSentiment[key] = analyzer.polarity_scores(text)
    return articleToSentiment
