class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "sair":
                print("Até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("criar", self.create_motorista)
        self.add_command("ler", self.read_motorista)
        self.add_command("atualizar", self.update_motorista)
        self.add_command("deletar", self.delete_motorista)

    def create_motorista(self):
        nome = input("Digite o nome do motorista: ")
        nota = int(input("Digite a nota do motorista: "))
        
        corridas = []
        num_corridas = int(input("Digite o número de corridas: "))

        for i in range(num_corridas):
            print(f"--- Corrida {i+1} ---")
            nota_corrida = int(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distância da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            nome_passageiro = input("Digite o nome do passageiro: ")
            documento_passageiro = input("Digite o documento do passageiro: ")
            
            passageiro = {"nome": nome_passageiro, "documento": documento_passageiro}
            corrida = {"nota": nota_corrida, "distancia": distancia, "valor": valor, "passageiro": passageiro}
            corridas.append(corrida)
        
        self.motorista_dao.create_motorista(nome, nota, corridas)

    def read_motorista(self):
        id = input("Digite o id do motorista: ")
        motorista = self.motorista_dao.read_motorista_by_id(id)
        if motorista:
            print(f"Nome: {motorista['nome']}")
            print(f"Nota: {motorista['nota']}")
            print("Corridas:")
            for i, corrida in enumerate(motorista['corridas']):
                print(f"--- Corrida {i+1} ---")
                print(f"Nota da Corrida: {corrida['nota']}")
                print(f"Distância: {corrida['distancia']} km")
                print(f"Valor: R$ {corrida['valor']}")
                print(f"Nome do Passageiro: {corrida['passageiro']['nome']}")
                print(f"Documento do Passageiro: {corrida['passageiro']['documento']}")

    def update_motorista(self):
        id = input("Digite o id do motorista: ")
        nome = input("Digite o novo nome do motorista: ")
        nota = int(input("Digite a nova nota do motorista: "))
        self.motorista_dao.update_motorista(id, nome, nota)

    def delete_motorista(self):
        id = input("Digite o id do motorista: ")
        self.motorista_dao.delete_motorista(id)

    def run(self):
        print("Bem-vindo ao sistema CLI de Motoristas!")
        print("Comandos disponíveis: criar, ler, atualizar, deletar, sair")
        super().run()


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sistema_motoristas"]
    motorista_dao = MotoristaDAO(db)
    cli = MotoristaCLI(motorista_dao)
    cli.run()