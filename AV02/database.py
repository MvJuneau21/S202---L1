from neo4j import GraphDatabase

class Database:
    def __init__(self, uri="bolt://98.84.46.7", user="neo4j", password="farad-coordinators-chiefs"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record.data() for record in result]
