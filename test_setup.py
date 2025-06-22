# test_setup.py - Verify your environment is ready

import sys
print("Python version:", sys.version)

# Test all required imports
try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import streamlit as st
    import plotly.express as px
    from sklearn.linear_model import LinearRegression
    import requests
    
    print("✅ All packages imported successfully!")
    
    # Test basic functionality
    print("\n🔍 Testing basic functionality...")
    
    # Test yfinance
    stock = yf.Ticker("AAPL")
    data = stock.history(period="5d")
    print(f"✅ Stock data fetched: {len(data)} days of AAPL data")
    
    # Test sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    test_text = "Apple stock reaches new highs!"
    sentiment = analyzer.polarity_scores(test_text)
    print(f"✅ Sentiment analysis working: {sentiment['compound']}")
    
    print("\n🎉 Environment setup complete! Ready for next step.")
    
except ImportError as e:
    print(f"❌ Missing package: {e}")
    print("Run: pip install yfinance vaderSentiment streamlit plotly scikit-learn pandas numpy requests")
except Exception as e:
    print(f"❌ Error: {e}")