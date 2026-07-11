from neo4j import GraphDatabase


class Neo4jService:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            "bolt://127.0.0.1:7687",
            auth=("neo4j", "Saurabh@12345")
        )

    def execute(self, query, parameters=None):

        with self.driver.session(database="neo4j") as session:

            result = session.run(
                query,
                parameters or {}
            )

            # Fetch all rows before closing the session
            return list(result)

    def close(self):

        self.driver.close()