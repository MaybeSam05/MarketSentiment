<h1>Stock Market Sentiment Analysis Tool</h1>

This Python script fetches recent news articles about a specified company, extracts their content, and performs sentiment analysis using the VADER sentiment analysis tool. The results provide an overview of how positively, negatively, or neutrally the company has been portrayed in the selected news sources.

<h2>Features</h2>
- Fetches up to 5 relevant articles for a specified company from multiple reputable domains.
- Extracts the full content of each article using the newspaper library.
- Analyzes the sentiment of the articles using VADER SentimentIntensityAnalyzer.
- Summarizes and formats sentiment scores for easy interpretation.

<h2>Requirements</h2>
- Python 3.7+
- NewsAPI key (free or paid subscription)
- .env file to store your NewsAPI key

<h2>Installation</h2>
1. Clone this repository:
- git clone https://github.com/your-username/your-repo-name.git
- cd your-repo-name

2. Install the required packages:
- pip install newsapi-python
- pip install flask
- pip install python-dotenv
- pip install newspaper3k
- pip install nltk
- pip install lxml
- pip install lxml_html_clean
- pip install vaderSentiment

3. Create a .env file in the project root and add your NewsAPI key:
NEWS_API_KEY=your_news_api_key

<h2>Usage</h2>
1. Open the script and customize the following variables in the main() function:
  - company: The name of the company to search for news articles (e.g., "Tesla").
  - start: Start date for fetching articles (format: YYYY-MM-DD).
  - end: End date for fetching articles (format: YYYY-MM-DD).

2. Run the script

3. The script will:
  - Fetch articles related to the specified company.
  - Display the sentiment analysis for each article.
  - Provide an overall sentiment score for the company.