# data_collector.py

import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd

# ✅ Fetch historical stock price data
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Handle single vs multi-index for consistent behavior
    if isinstance(data.columns, pd.MultiIndex):
        return data
    else:
        data.columns = pd.MultiIndex.from_product([data.columns, [ticker]])
        return data

# ✅ Fetch news headlines from Yahoo Finance
def fetch_news(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Yahoo Finance doesn't always use a table — safer to look for <li> or <a> tags inside news section
    headlines = []
    
    # Try to find news headlines safely
    news_section = soup.find('section')
    if news_section:
        for link in news_section.find_all('a'):
            text = link.get_text(strip=True)
            if text:
                headlines.append(text)
    
    # If section not found, fallback to simple a-tags
    if not headlines:
        for tag in soup.find_all('a'):
            text = tag.get_text(strip=True)
            if text and ticker in text.upper():
                headlines.append(text)

    return headlines
