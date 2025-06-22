# sentiment_analyzer.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(headlines):
    scores = []
    for headline in headlines:
        sentiment = analyzer.polarity_scores(headline)
        scores.append(sentiment['compound'])  # Compound is the overall score
    if scores:
        return sum(scores) / len(scores)  # Average score
    return 0  # Neutral if no headlines

# Test run
if __name__ == "__main__":
    sample_news = [
        "Apple stock soars after strong earnings report",
        "Investors worry about upcoming tech layoffs",
        "New iPhone model receives mixed reviews"
    ]
    avg_sentiment = analyze_sentiment(sample_news)
    print(f"🧠 Average Sentiment Score: {avg_sentiment:.3f}")

from data_collector import fetch_news
headlines = fetch_news("AAPL")
print("Score:", analyze_sentiment(headlines))
