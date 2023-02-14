from neo4j import GraphDatabase

host = 'bolt://localhost:7687'
user = 'neo4j'
password = 'pleaseletmein'
driver = GraphDatabase.driver(host, auth=(user, password))


def read_query(query, params={}):
    with driver.session() as session:
        result = session.run(query, params)
        response = [r.values()[0] for r in result]
        return response


def get_article_text(title):
    text = read_query(
        "MATCH (a:Article {webTitle:$title}) RETURN a.bodyContent as text", {'title': title})
    return text
