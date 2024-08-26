from Pokedex import Pokedex
from helper.writeAJSon import writeAJson
pokedex = Pokedex(database = "pokedex", collection="pokemons")
pkm = pokedex.mostrarPokemon()
writeAJson(pkm, "Pokémons")
nome = str(input("Digite o nome do pokemon: "))
achar = pokedex.mostrarPorNome(nome)
writeAJson(achar, nome)
tipagem = ["Psychic", "Ice"]
pkm = pokedex.mostrarPorTipo(tipagem)
writeAJson(pkm, tipagem)
evo = pokedex.mostrarPorEvo(tipagem)
writeAJson(evo, "Pokemon_com_Evolucoes")
fraqueza = pokedex.mostrarUmaFraqueza()
writeAJson(fraqueza, "Pokemon_com_fraqueza_unica")