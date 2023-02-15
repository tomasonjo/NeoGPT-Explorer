examples = """
# What are the latest news?
MATCH (a:Article) RETURN a.webTitle AS response ORDER BY a.date DESC LIMIT 3

# What are the latest positive news?
MATCH (a:Article) WHERE a.sentiment > 0 RETURN a.webTitle AS response ORDER BY a.date DESC LIMIT 3

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

# What are the latest facts?
MATCH (a:Article)-[:MENTIONS_RELATIONSHIP]->(relationship) WITH relationship, min(a.date) AS date ORDER BY date DESC LIMIT 3 MATCH (source)-[:RELATIONSHIP]->(relationship)-[:RELATIONSHIP]->(target) RETURN source.id + " " + relationship.type + " " + target.id AS response

# What do you know about Andrew Macintosh?
CALL {MATCH (s:Entity {id:"Andrew Macintosh"})-[:RELATIONSHIP]->(rel)-[:RELATIONSHIP]->(target) RETURN s.id + " " + rel.type + " " + target.id AS response LIMIT 3 UNION ALL MATCH (s:Entity {id:"Andrew Macintosh"})<-[:RELATIONSHIP]->(rel)<-[:RELATIONSHIP]->(target) RETURN target.id + " " + rel.type + " " + s.id AS response LIMIT 3} RETURN response LIMIT 3

# Where does Ian Chubb work?
MATCH (e:Entity {id:"Ian Chubb"})-[:RELATIONSHIP]->({type:"EMPLOYEE_OR_MEMBER_OF"})-[:RELATIONSHIP]->(target) RETURN target.id AS response

# Who are most mentioned people in sports?
MATCH (entity {type:"person"})<-[:MENTIONS]-(a:Article)-[:HAS_SECTION]->({name:"Sport"}) WITH entity, count(*) AS mentions ORDER BY mentions DESC LIMIT 3 RETURN entity.id AS response
"""
