import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_yahoo_finance():
    url = "https://finance.yahoo.com/topic/stock-market-news/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    headlines = [h.text for h in soup.select('h3')]
    return [{"headline": h, "source": "yahoo", "timestamp": datetime.utcnow()} for h in headlines]

if __name__ == "__main__":
    df = pd.DataFrame(scrape_yahoo_finance())
    df.to_csv("data/news_headlines.csv", index=False)
    print(f"Saved {len(df)} headlines to data/news_headlines.csv")
