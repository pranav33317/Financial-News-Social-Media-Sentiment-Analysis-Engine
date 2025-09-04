import streamlit as st
import pandas as pd

st.title("Financial Sentiment Analyzer")

news = pd.read_csv("data/news_sentiment.csv")
tweets = pd.read_csv("data/tweets_sentiment.csv")

st.subheader("News Sentiment")
st.write(news.head())

st.subheader("Tweet Sentiment")
st.write(tweets.head())

st.bar_chart(news["sentiment"].value_counts())
st.bar_chart(tweets["sentiment"].value_counts())
