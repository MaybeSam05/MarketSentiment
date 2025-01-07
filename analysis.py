from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import sys
from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

load_dotenv()

newsapi = NewsApiClient(os.getenv("NEWS_API_KEY"))


def main():
    company = "Tesla" # customizable
    start = "2024-12-25" # customizable
    end = "2025-01-05" # customizable
    domains = ["cnn.com", "bbc.com", "nytimes.com", "bloomberg.com", "cnbc.com", "investopedia.com",
    "ft.com", "seekingalpha.com", "businessinsider.com", "zacks.com", "benzinga.com", "investing.com",
    "economist.com", "nasdaq.com", "kiplinger.com", "fool.com", "marketplace.org"] # not customizable
    
    #headlinesToLinks = (fetch_articles(company, domains, start, end))
    #titlesToContent = read_articles(headlinesToLinks)
    #sentiments = analyze_sentiment(titlesToContent)

    sentiments = {
        'Tesla could see 40% of its profits evaporate when Trump takes office, JPMorgan warns': {'neg': 0.058, 'neu': 0.87, 'pos': 0.072, 'compound': 0.7753}, 
        'Tesla Cybertruck that exploded and the New Orleans attack vehicle were both reportedly rented using the Turo app': {'neg': 0.105, 'neu': 0.821, 'pos': 0.075, 'compound': -0.9852},
        "Tesla shows it's not immune to the EV slowdown": {'neg': 0.061, 'neu': 0.837, 'pos': 0.102, 'compound': 0.8567},
        'The most popular cars of 2024: It was the year of the hybrid.': {'neg': 0.008, 'neu': 0.812, 'pos': 0.18, 'compound': 0.9953},
        "BYD makes much more than cars. These 5 side hustles also helped turn the Chinese EV giant into a challenger to Elon Musk's Tesla.": {'neg': 0.005, 'neu': 0.918, 'pos': 0.077, 'compound': 0.996}
    }

    format_sentiment(company, sentiments)

def fetch_articles(company_name, domains, start, end):
    my_dict = {}
    
    articles = newsapi.get_everything(
        q=company_name,
        from_param=start,  # Start date
        to=end,          # End date
        language='en',            # Language of the articles
        sort_by='relevancy'     # Sort by relevancy
    )
    
    count = 0
    for article in articles['articles']:
        if (article['title'] != "[Removed]") and any(domain in article['url'] for domain in domains):
            #print(f"Title: {article['title']}")
            #print(f"URL: {article['url']}\n")
            my_dict[article['title']] = article['url']
            count += 1
            if count == 5:
                break
    
    return my_dict

def read_articles(my_dict):
    articleToContent = {}
    
    for key, url in my_dict.items():  # Loop through key-value pairs
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

def format_sentiment(company, my_dict):
    print(f"\nCompany: {company}\n")
    totalSent = 0

    count = 1
    for key, value in my_dict.items():
        print(f"\nArticle {count}: {key}")
        print("Sentence was rated as ", value['neg']*100, "% Negative")
        print("Sentence was rated as ", value['neu']*100, "% Neutral")
        print("Sentence was rated as ", value['pos']*100, "% Neutral")
        
        totalSent += value['compound']
        print("Sentence Overall Rated As", end=" ")
        if value['compound'] >= 0.05 :
            print("Positive")
        elif value['compound'] <= -0.05 :
            print("Negative")
        else :
            print("Neutral")

        count += 1

        if count > 5:
            print(f"\n{company} Overall Sentiment: {(totalSent / 5)}\n")
        
if __name__ == "__main__":
    main()