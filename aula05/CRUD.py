import pymongo
from pymongo import MongoClient
from helper.writeAJson import writeAJson

client = MongoClient('mongodb://localhost:27017/')
db = client['relatorio_05']
collection = db['Livros']

def criar_livro():
    try:
        _id = int(input("Digite o ID do livro: "))
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação do livro: "))
        preco = float(input("Digite o preço do livro: "))

        novo_livro = {
            "_id": _id,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "preco": preco
        }

        collection.insert_one(novo_livro)
        print("Livro adicionado com sucesso!")
        
        livros = list(collection.find())
        writeAJson(livros, 'Adicionado')
        
    except Exception as e:
        print(f"Erro ao adicionar o livro: {e}")

def ler_livros():
    livros = list(collection.find())
    for livro in livros:
        print(f"ID: {livro['_id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Preço: {livro['preco']}")

    writeAJson(livros, 'livros')

def atualizar_livro():
    try:
        _id = int(input("Digite o ID do livro a ser atualizado: "))
        campo = input("Qual campo deseja atualizar? (titulo, autor, ano, preco): ")
        novo_valor = input(f"Digite o novo valor para {campo}: ")

        if campo == "ano":
            novo_valor = int(novo_valor)
        elif campo == "preco":
            novo_valor = float(novo_valor)

        collection.update_one({"_id": _id}, {"$set": {campo: novo_valor}})
        print("Livro atualizado com sucesso!")
        
        livros = list(collection.find())
        writeAJson(livros, 'atualizado')

    except Exception as e:
        print(f"Erro ao atualizar o livro: {e}")

def deletar_livro():
    try:
        _id = int(input("Digite o ID do livro a ser deletado: "))
        collection.delete_one({"_id": _id})
        print("Livro deletado com sucesso!")
    
        livros = list(collection.find())
        writeAJson(livros, 'deletado')

    except Exception as e:
        print(f"Erro ao deletar o livro: {e}")

def menu_crud():
    while True:
        print("\n----- Menu CRUD Livros -----")
        print("1. Adicionar novo livro")
        print("2. Listar todos os livros")
        print("3. Atualizar um livro")
        print("4. Deletar um livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_livro()
        elif escolha == '2':
            ler_livros()
        elif escolha == '3':
            atualizar_livro()
        elif escolha == '4':
            deletar_livro()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu_crud()
