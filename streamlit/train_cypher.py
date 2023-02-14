examples = """
# What are the latest news?
MATCH (a:Article) RETURN a.webTitle AS response ORDER BY a.date DESC LIMIT 3

# What are the latest news about Apple?
MATCH (e:Entity {id:"Apple"})<-[m:MENTIONS]-(a) RETURN a.webTitle AS response ORDER BY m.confidence DESC LIMIT 3

# What are the latest news about COVID-19?
MATCH (e:Entity {id:"COVID-19"})<-[m:MENTIONS]-(a) RETURN a.webTitle AS response ORDER BY m.confidence DESC LIMIT 3

# What are the latest news about education?
MATCH (a)-[:HAS_SECTION]->(section {name:'Education'}) RETURN a.webTitle AS response ORDER BY a.date DESC LIMIT 3

# Who was mentioned in a positive light lately?
MATCH (a:Article)-[m:MENTIONS]->(e:Entity {type:'person'}) RETURN e.id + " in " + a.webTitle AS response ORDER BY m.sentiment DESC LIMIT 3

# Most mentioned people in the last 100 articles?
MATCH (a:Article) WITH a ORDER BY a.date DESC LIMIT 100 MATCH (a)-[m:MENTIONS]->(e:Entity {type:'person'}) WITH distinct e WITH e, count{(e)<-[:MENTIONS]-()} AS s ORDER BY s DESC LIMIT 3 RETURN e.id AS response

"""
