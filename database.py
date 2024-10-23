from neo4j import GraphDatabase

class GameDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def create_player(self, player_id, name):
        with self.driver.session() as session:
            session.write_transaction(self._create_player, player_id, name)

    @staticmethod
    def _create_player(tx, player_id, name):
        tx.run("CREATE (p:Player {id: $player_id, name: $name})",
               player_id=player_id, name=name)

    def update_player(self, player_id, name):
        with self.driver.session() as session:
            session.write_transaction(self._update_player, player_id, name)

    @staticmethod
    def _update_player(tx, player_id, name):
        tx.run("MATCH (p:Player {id: $player_id}) "
               "SET p.name = $name", player_id=player_id, name=name)

    def delete_player(self, player_id):
        with self.driver.session() as session:
            session.write_transaction(self._delete_player, player_id)

    @staticmethod
    def _delete_player(tx, player_id):
        tx.run("MATCH (p:Player {id: $player_id}) DETACH DELETE p",
               player_id=player_id)

    def get_player(self, player_id):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_player, player_id)
            return result.single()

    @staticmethod
    def _get_player(tx, player_id):
        result = tx.run("MATCH (p:Player {id: $player_id}) RETURN p.id AS id, p.name AS name",
                        player_id=player_id)
        return result

    def get_all_players(self):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_all_players)
            return [record for record in result]

    @staticmethod
    def _get_all_players(tx):
        result = tx.run("MATCH (p:Player) RETURN p.id AS id, p.name AS name")
        return result

    def create_match(self, match_id, player_ids, result):
        with self.driver.session() as session:
            session.write_transaction(self._create_match, match_id, player_ids, result)

    @staticmethod
    def _create_match(tx, match_id, player_ids, result):
        tx.run("CREATE (m:Match {id: $match_id, result: $result})",
               match_id=match_id, result=result)

        for player_id in player_ids:
            tx.run("MATCH (p:Player {id: $player_id}), (m:Match {id: $match_id}) "
                   "MERGE (p)-[:PARTICIPATED_IN]->(m)",
                   player_id=player_id, match_id=match_id)

    def update_match(self, match_id, result):
        with self.driver.session() as session:
            session.write_transaction(self._update_match, match_id, result)

    @staticmethod
    def _update_match(tx, match_id, result):
        tx.run("MATCH (m:Match {id: $match_id}) "
               "SET m.result = $result", match_id=match_id, result=result)

    def delete_match(self, match_id):
        with self.driver.session() as session:
            session.write_transaction(self._delete_match, match_id)

    @staticmethod
    def _delete_match(tx, match_id):
        tx.run("MATCH (m:Match {id: $match_id}) DETACH DELETE m",
               match_id=match_id)

    def get_match(self, match_id):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_match, match_id)
            return result.single()

    @staticmethod
    def _get_match(tx, match_id):
        result = tx.run("MATCH (m:Match {id: $match_id}) "
                        "RETURN m.id AS id, m.result AS result")
        return result

    def get_player_matches(self, player_id):
        with self.driver.session() as session:
            result = session.read_transaction(self._get_player_matches, player_id)
            return [record for record in result]

    @staticmethod
    def _get_player_matches(tx, player_id):
        result = tx.run("MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match) "
                        "RETURN m.id AS id, m.result AS result", player_id=player_id)
        return result
