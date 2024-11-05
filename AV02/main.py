import argparse
from teacher_crud import TeacherCRUD
from query import Query

def main():
    parser = argparse.ArgumentParser(description="CLI para operações CRUD e consultas no banco de dados Neo4j")
    parser.add_argument("operacao", type=str, choices=[
        "create_teacher", "read_teacher", "update_teacher", "delete_teacher",
        "oldest_youngest", "average_population", "city_name_replace", "third_char_names"
    ], help="Operação a ser realizada")

    parser.add_argument("--name", type=str, help="Nome do professor")
    parser.add_argument("--ano_nasc", type=int, help="Ano de nascimento do professor")
    parser.add_argument("--cpf", type=str, help="CPF do professor")
    parser.add_argument("--new_cpf", type=str, help="Novo CPF para atualizar")

    parser.add_argument("--cep", type=str, help="CEP para busca de cidade e substituição de 'a' por 'A' no nome")

    args = parser.parse_args()
    crud = TeacherCRUD()
    query = Query()

    if args.operacao == "create_teacher" and args.name and args.ano_nasc and args.cpf:
        crud.create(args.name, args.ano_nasc, args.cpf)
        print(f"Professor {args.name} criado com sucesso!")
    elif args.operacao == "read_teacher" and args.name:
        result = crud.read(args.name)
        print("Resultado da consulta:", result)
    elif args.operacao == "update_teacher" and args.name and args.new_cpf:
        crud.update(args.name, args.new_cpf)
        print(f"CPF do professor {args.name} atualizado para {args.new_cpf}")
    elif args.operacao == "delete_teacher" and args.name:
        crud.delete(args.name)
        print(f"Professor {args.name} deletado com sucesso!")
    elif args.operacao == "oldest_youngest":
        result = query.get_oldest_youngest_teacher_years()
        print("Ano do professor mais velho e mais jovem:", result)
    elif args.operacao == "average_population":
        result = query.get_average_population()
        print("Média da população das cidades:", result)
    elif args.operacao == "city_name_replace":
        cep = args.cep if args.cep else "37540-000"
        result = query.get_city_name_with_replaced_a(cep)
        print(f"Nome da cidade com 'a' substituído por 'A' (CEP {cep}):", result)
    elif args.operacao == "third_char_names":
        result = query.get_teacher_names_third_char()
        print("Terceiro caractere dos nomes dos professores:", result)
    else:
        print("Operação ou argumentos inválidos. Use --help para mais informações.")

if __name__ == "__main__":
    main()
