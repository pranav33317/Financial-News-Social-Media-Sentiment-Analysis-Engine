#!/bin/bash
set -e

python src/news_scraper.py
python src/twitter_collector.py
python src/text_cleaning.py
python src/sentiment_model.py
python src/correlation.py
streamlit run src/dashboard.py
