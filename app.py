from flask import Flask, render_template, request
from sentiment_analysis import fetch_articles, read_articles, analyze_sentiment
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method == 'POST':
        # Get form data
        company = request.form['company']

        # Set date range to last 30 days
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        # Define domains to search
        domains = [
            "cnn.com", "bbc.com", "nytimes.com", "bloomberg.com", "cnbc.com",
            "investopedia.com", "ft.com", "seekingalpha.com", "businessinsider.com",
            "zacks.com", "benzinga.com", "investing.com", "economist.com",
            "nasdaq.com", "kiplinger.com", "fool.com", "marketplace.org"
        ]

        # Fetch, process, and analyze articles
        headlines_to_links = fetch_articles(company, domains, start_date, end_date)
        titles_to_content = read_articles(headlines_to_links)
        sentiments = analyze_sentiment(titles_to_content)

        # Prepare data for display
        results = []
        overall_sentiment_score = 0
        for title, sentiment in sentiments.items():
            result = {
                "title": title,
                "negative": f"{sentiment['neg'] * 100:.2f}",
                "neutral": f"{sentiment['neu'] * 100:.2f}",
                "positive": f"{sentiment['pos'] * 100:.2f}",
                "overall": (
                    "Positive" if sentiment['compound'] >= 0.05 else
                    "Negative" if sentiment['compound'] <= -0.05 else
                    "Neutral"
                )
            }
            results.append(result)
            overall_sentiment_score += sentiment['compound']

        overall_sentiment = f"{overall_sentiment_score / len(results):.2f}"

        if float(overall_sentiment) > 0:
            sentimentText = "Positive Sentiment"
        elif float(overall_sentiment) == 0:
            sentimentText = "Neutral Sentiment"
        else:
            sentimentText = "Negative Sentiment"

        # Render the results page
        return render_template(
            'results.html',
            company=company,
            results=results,
            overall_sentiment=overall_sentiment,
            sentimentText=sentimentText,
            enumerate=enumerate  # Pass enumerate to the template
        )

    # Render the form page for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
