import pandas as pd
from transformers import pipeline

def analyze_sentiment(texts, model_name="ProsusAI/finbert"):
    nlp = pipeline("sentiment-analysis", model=model_name)
    return [nlp(t)[0]["label"] for t in texts]

if __name__ == "__main__":
    news = pd.read_csv("data/news_clean.csv")
    tweets = pd.read_csv("data/tweets_clean.csv")
    news["sentiment"] = analyze_sentiment(news["clean"].tolist())
    tweets["sentiment"] = analyze_sentiment(tweets["clean"].tolist())
    news.to_csv("data/news_sentiment.csv", index=False)
    tweets.to_csv("data/tweets_sentiment.csv", index=False)
    print("Sentiment analysis complete.")
