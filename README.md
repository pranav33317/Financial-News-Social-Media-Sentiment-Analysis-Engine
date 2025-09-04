# Financial Sentiment Analyzer

Pipeline to scrape financial news & tweets, run sentiment analysis (VADER + FinBERT),
and correlate sentiment with stock returns. Dashboard built using Streamlit.

## Structure
- data/: scraped raw + processed data
- notebooks/: EDA + model experimentation
- src/: main pipeline scripts
- config.yaml: API keys + database credentials

## Run
```bash
pip install -r requirements.txt
python src/news_scraper.py
python src/twitter_collector.py
python src/text_cleaning.py
python src/sentiment_model.py
python src/correlation.py
streamlit run src/dashboard.py
```
