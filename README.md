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

If you are using Windows, you can also execute the `notebooks/Import.ipynb` notebook for initial import

4. Open localhost:8501 in your browser

## Example questions

What are the latest news?

What are the latest news about Apple?

What are the latest news about COVID-19?

What are the latest news about education?

Who was mentioned in a positive light lately?

Most mentioned people in the last 100 articles?

What are the latest facts?

What do you know about Andrew Macintosh?

Where does Ian Chubb work?

What are most mentioned people in sports?

## Data 

Testing dataset consists of 1000 latest articles from Kaggle repository: https://www.kaggle.com/datasets/adityakharosekar2/guardian-news-articles

## Preprocessing

The information extraction pipeline was executed with Diffbot API: See `notebooks/Preprocess.ipynb`.

## Feedback

Please create an issue if you have any feedback!

