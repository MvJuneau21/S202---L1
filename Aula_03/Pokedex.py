from database import Database
from helper.writeAJSon import writeAJson

class Pokedex():
    def __init__(self, database, collection):
        self.db = Database(database, collection)
    def mostrarPokemon(self):
        pokemons = self.db.collection.find()
    def mostrarPorNome(self, name: str):
        return self.db.collection.find({"name": name})
    def mostrarPorTipo(self, types: list):
        return self.db.collection.find({"type": {"$in": types}})
    def mostrarPorEvo(self, types: list):
        return self.db.collection.find({"type": {"$in": types},"next_evolution": {"$exists": True}})
    def mostrarUmaFraqueza(self):
        return self.db.collection.find({"weaknesses": {"$size": 1}})
    
