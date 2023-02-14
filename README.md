# NeoGPT-Explorer

Run the following commands to start the services:


1. Create an `.env` file and input your OPENAI API KEY as shown in `env.example`

2. Start docker services

```
docker-compose up
```

3. On the first run, you need to seed the database with the following command

```
sh seed_database.sh
```

4. Open localhost:8501 in your browser

## Data 

Testing dataset consists of 1000 latest articles from Kaggle repository: https://www.kaggle.com/datasets/adityakharosekar2/guardian-news-articles

## Preprocessing

The information extraction pipeline was executed with Diffbot API: See `notebooks/Preprocess.ipynb`.

