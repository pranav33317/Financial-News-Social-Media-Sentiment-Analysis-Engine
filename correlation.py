import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    news = pd.read_csv("data/news_sentiment.csv")
    tweets = pd.read_csv("data/tweets_sentiment.csv")
    # Placeholder: dummy stock returns
    stock = pd.DataFrame({
        "timestamp": news["timestamp"],
        "return": range(len(news))
    })
    combined = news.merge(stock, on="timestamp", how="left")
    sentiment_counts = combined.groupby("sentiment")["return"].mean()
    print("Correlation (dummy):", sentiment_counts)
    sentiment_counts.plot(kind="bar", title="Avg Return by Sentiment")
    plt.savefig("data/correlation.png")
    print("Saved correlation.png")
