# app.py

import streamlit as st
import datetime
import plotly.graph_objects as go

from data_collector import fetch_stock_data, fetch_news
from sentiment_analyzer import analyze_sentiment
from price_predictor import train_and_predict

st.set_page_config(page_title="📈 AI Stock Price Predictor", layout="centered")

st.title("📊 AI Stock Price Predictor with Sentiment Analysis")
st.markdown("Built with 💡 by Vishakha using Streamlit + ML")

# Input
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, GOOGL)", "AAPL").upper()

if st.button("Predict"):
    today = datetime.date.today()
    start = today - datetime.timedelta(days=60)

    with st.spinner("Fetching stock data..."):
        df = fetch_stock_data(ticker, start, today)

    with st.spinner("Analyzing news sentiment..."):
        headlines = fetch_news(ticker)
        sentiment = analyze_sentiment(headlines)

    with st.spinner("Predicting next day price..."):
        prediction = train_and_predict(df, sentiment, ticker)


    st.success(f"🧠 Average News Sentiment: `{round(sentiment, 3)}`")
    st.success(f"🔮 Predicted Next Closing Price: `${prediction}`")

    # Plot last 30 days
    st.subheader("📈 Last 30 Days Closing Price")
    try:
        price_series = df[('Close', ticker)]
    except:
        price_series = df['Close']

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=price_series.index, y=price_series, mode='lines+markers', name='Close Price'))
    fig.update_layout(xaxis_title="Date", yaxis_title="Price (USD)")
    st.plotly_chart(fig)

    # Show recent news
    st.subheader("📰 Recent Headlines")
    for h in headlines[:5]:
        st.write("•", h)
