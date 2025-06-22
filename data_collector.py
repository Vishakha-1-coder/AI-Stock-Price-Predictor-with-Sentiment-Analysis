# data_collector.py

import yfinance as yf
import requests
from bs4 import BeautifulSoup
import datetime

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def fetch_news(ticker):
    url = f'https://finviz.com/quote.ashx?t={ticker}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    news_table = soup.find('table', class_='fullview-news-outer')

    headlines = []
    for row in news_table.findAll('tr'):
        headline = row.a.text
        headlines.append(headline)

    return headlines

# Test run
if __name__ == "__main__":
    ticker = "AAPL"
    today = datetime.date.today()
    past = today - datetime.timedelta(days=30)

    print("✅ Downloading stock data...")
    df = fetch_stock_data(ticker, past, today)
    print(df.tail())

    print("\n📰 Fetching recent headlines...")
    news = fetch_news(ticker)
    for i, headline in enumerate(news[:5]):
        print(f"{i+1}. {headline}")
