import tweepy
import pandas as pd
import yaml
from datetime import datetime

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def collect_tweets(query="#NIFTY50", count=100):
    cfg = load_config()
    client = tweepy.Client(bearer_token=cfg["twitter"]["bearer_token"])
    tweets = client.search_recent_tweets(query=query, max_results=count)
    data = []
    for t in tweets.data:
        data.append({"tweet": t.text, "timestamp": datetime.utcnow()})
    return data

if __name__ == "__main__":
    tweets = collect_tweets()
    df = pd.DataFrame(tweets)
    df.to_csv("data/tweets.csv", index=False)
    print(f"Collected {len(df)} tweets -> data/tweets.csv")
