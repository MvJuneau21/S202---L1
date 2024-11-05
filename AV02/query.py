from database import Database

class Query:
    def __init__(self):
        self.db = Database(uri="bolt://98.84.46.7", user="neo4j", password="farad-coordinators-chiefs")

    def get_teacher_renzo(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        return self.db.execute_query(query)

    def get_teachers_starting_with_m(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        return self.db.execute_query(query)

    def get_all_cities(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        return self.db.execute_query(query)

    def get_schools_by_number_range(self):
        query = """
            MATCH (s:School) 
            WHERE s.number >= 150 AND s.number <= 550 
            RETURN s.name AS name, s.address AS address, s.number AS number
        """
        return self.db.execute_query(query)

    def get_oldest_youngest_teacher_years(self):
        query = """
            MATCH (t:Teacher)
            RETURN min(t.ano_nasc) AS oldest, max(t.ano_nasc) AS youngest
        """
        return self.db.execute_query(query)

    def get_average_population(self):
        query = "MATCH (c:City) RETURN avg(c.population) AS average_population"
        return self.db.execute_query(query)

    def get_city_name_with_replaced_a(self, cep="37540-000"):
        query = f"MATCH (c:City {{cep: '{cep}'}}) RETURN replace(c.name, 'a', 'A') AS name"
        return self.db.execute_query(query)

    def get_teacher_names_third_char(self):
        query = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS third_char"
        return self.db.execute_query(query)
