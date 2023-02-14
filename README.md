# NeoGPT-Explorer

## Data 

Testing dataset consists of 1000 latest articles from Kaggle repository: https://www.kaggle.com/datasets/adityakharosekar2/guardian-news-articles

## Preprocessing

The information extraction pipeline was executed with Diffbot API: See `notebooks/Preprocess.ipynb`.

## Neo4j import

See `notebooks/Import.ipynb`

## Streamlit app

First install requirements.
Next, insert your OpenAI API KEY into `app.py`

Run `streamlit run streamlit/app.py`

