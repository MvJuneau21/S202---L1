from database import Database

class TeacherCRUD:
    def __init__(self):
        self.db = Database(uri="bolt://98.84.46.7", user="neo4j", password="farad-coordinators-chiefs")

    def create(self, name, ano_nasc, cpf):
        query = f"CREATE (:Teacher {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})"
        return self.db.execute_query(query)

    def read(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) RETURN t"
        return self.db.execute_query(query)

    def update(self, name, new_cpf):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) SET t.cpf = '{new_cpf}' RETURN t"
        return self.db.execute_query(query)

    def delete(self, name):
        query = f"MATCH (t:Teacher {{name: '{name}'}}) DELETE t"
        return self.db.execute_query(query)
