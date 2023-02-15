import json
from graphdatascience import GraphDataScience
import pandas as pd

host = "bolt://localhost:7687"
user = "neo4j"
password = "pleaseletmein"
gds = GraphDataScience(host, auth=(user, password))

articles = pd.read_csv("data/articles.csv")

gds.run_cypher(
    """
CREATE CONSTRAINT IF NOT EXISTS FOR (a:Article) REQUIRE a.id IS UNIQUE;
"""
)
gds.run_cypher(
    """
CREATE CONSTRAINT IF NOT EXISTS FOR (s:Section) REQUIRE s.name IS UNIQUE;
"""
)
gds.run_cypher(
    """
CREATE TEXT INDEX articletitle IF NOT EXISTS FOR (a:Article) ON a.webTitle;
"""
)

article_import_query = """
UNWIND $data AS row
MERGE (a:Article {id: row.id})
SET a += apoc.map.clean(row, ["id", "article_id", "sectionName", "webPublicationDate"], [])
SET a.date = datetime(replace(row.webPublicationDate, " ", "T"))
WITH a, row.sectionName AS section
MERGE (s:Section {name: section})
MERGE (a)-[:HAS_SECTION]->(s)
"""

gds.run_cypher(article_import_query, {"data": articles.to_dict("records")})

with open("data/nlp_output.json") as file:
    nlp_output = json.load(file)

gds.run_cypher(
    """
CREATE CONSTRAINT IF NOT EXISTS FOR (e:Entity) REQUIRE e.id IS UNIQUE;
"""
)

nlp_import_query = """
UNWIND $data AS row
MATCH (a:Article {id: row.id})
SET a.sentiment = row.sentiment
FOREACH (entity in row.entity | 
  MERGE (e:Entity {id: entity.name})
  ON CREATE SET e.type = entity.type,
                e.uri = entity.uri
  MERGE (a)-[m:MENTIONS]-(e)
  SET m.confidence = entity.confidence,
      m.sentiment = entity.sentiment
)
WITH a, row
UNWIND row.fact AS fact
  WITH a, fact
  MERGE (source:Entity {id: fact.source.name})
  ON CREATE SET source.type = fact.source.type
  MERGE (target:Entity {id: fact.target.name})
  ON CREATE SET target.type = fact.target.type
  MERGE (source)-[:RELATIONSHIP]->(r:Relationship {type: toUpper(replace(fact.relationship,' ','_'))})-[:RELATIONSHIP]->(target)
  MERGE (a)-[mr:MENTIONS_RELATIONSHIP]->(r)
  SET mr.confidence = fact.confidence
"""

batch_step = 100

for offset in range(0, len(nlp_output), batch_step):
    batch = nlp_output[offset: offset + batch_step]
    gds.run_cypher(nlp_import_query, {"data": batch})
