# price_predictor.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def create_dataset(prices, sentiment_score, window_size=5):
    X, y = [], []
    for i in range(window_size, len(prices) - 1):
        features = prices[i - window_size:i]  # last 5 days
        features.append(sentiment_score)  # add sentiment
        X.append(features)
        y.append(prices[i + 1])  # next day's price
    return np.array(X), np.array(y)

def train_and_predict(prices_df, sentiment_score):
    close_prices = prices_df['Close'].to_list()
    
    X, y = create_dataset(close_prices, sentiment_score)
    
    if len(X) == 0:
        print("❌ Not enough data for prediction.")
        return None
    
    model = LinearRegression()
    model.fit(X, y)
    
    last_sequence = close_prices[-5:] + [sentiment_score]
    next_day_price = model.predict([last_sequence])[0]
    
    return round(next_day_price, 2)

# Test run
if __name__ == "__main__":
    from data_collector import fetch_stock_data
    from sentiment_analyzer import analyze_sentiment
    from data_collector import fetch_news
    import datetime

    ticker = "AAPL"
    today = datetime.date.today()
    start = today - datetime.timedelta(days=60)

    df = fetch_stock_data(ticker, start, today)
    news = fetch_news(ticker)
    sentiment = analyze_sentiment(news)

    print("Columns in df:", prices_df.columns)
    print(prices_df.tail())

    prediction = train_and_predict(df, sentiment)
    print(f"🔮 Predicted next closing price for {ticker}: ${prediction}")
