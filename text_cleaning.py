import pandas as pd
import re
import nltk
import spacy

nltk.download("stopwords")
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = text.lower()
    tokens = [t.lemma_ for t in nlp(text) if t.text not in stopwords.words("english")]
    return " ".join(tokens)

if __name__ == "__main__":
    news = pd.read_csv("data/news_headlines.csv")
    tweets = pd.read_csv("data/tweets.csv")
    news["clean"] = news["headline"].apply(clean_text)
    tweets["clean"] = tweets["tweet"].apply(clean_text)
    news.to_csv("data/news_clean.csv", index=False)
    tweets.to_csv("data/tweets_clean.csv", index=False)
    print("Cleaned news & tweets saved.")
