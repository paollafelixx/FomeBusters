class oferta:
    def __init__(self, cpf_cnpj, descricao, perecivel, data_validade, peso, volume, endereco, telefone, horarios):
        #inserir um campo a mais para definir se PF ou PJ
        self.cpf_cnpj = cpf_cnpj
        self.descricao = descricao
        self.perecivel = perecivel
        self.data_validade = data_validade
        self.peso = peso
        self.volume = volume
        self.endereco = endereco
        self.telefone = telefone
        self.horarios = horarios

def cadastrar_doacao():
    #cadastrar if para separa PF e PJ
    tipo = int(input("Digite se o cliente é [1 - CPF] ou [2 - CNPJ]: "))
    while tipo != 1 and tipo != 2:
        print("Opção Inválida")
        tipo = int(input("Digite se o cliente é [1 - CPF] ou [2 - CNPJ]: "))
    if tipo == 1:
        cpf_cnpj = input("Informe o CPF (somente numeros): ")
        while not cpf_cnpj.isdigit() or len(cpf_cnpj) != 11:
            print("CPF inválido!")
            cpf_cnpj = input("Digite novamente o CPF (11 números): ")
    elif tipo == 2:
        cpf_cnpj = input("Informe o CNPJ: ")
        while not cpf_cnpj.isdigit() or len(cpf_cnpj) != 14:
            print("CNPJ inválido!")
            cpf_cnpj = input("Digite novamente o CNPJ (14 números): ")

    descricao = input("Descrição do alimento: ")

    tipoperecivel = int(input("O alimento é perecivel? [1 - Sim] ou [2 - Não]: "))
    while tipoperecivel != 1 and tipoperecivel != 2:
        print("Opção Inválida")
        tipoperecivel = int(input("O alimento é perecivel? [1 - Sim] ou [2 - Não]: "))
    if tipoperecivel == 1:
        perecivel = "Sim"
    else:perecivel = "Não"

    data_validade = input("Data de validade: ")
    #try except pesquisar como iferror excel
    # usar validação while com 1 ou 0 pro except
    peso = input("Peso aproximado (em kg): ")
    volume = input("Volume aproximado (em litros): ")
    endereco = input("Endereço para retirada: ")
    #Existe comando pra padrao de data ou numero de celular?
    #pesquisar mascara para input ou print. PEsquisar biblioteca
    telefone = input("Número de telefone para contato via WhatsApp (xx-XXXXX XXXX: ") #limitar via string(usar while e lengh)
    horarios = input("Horários e dias da semana para buscar: ")

    alimento = oferta(cpf_cnpj, descricao, perecivel, data_validade, peso, volume, endereco, telefone, horarios)
    return alimento


def imprimir_alimento(alimento):
    print("\n===== Informações da Doação =====")
    print("CPF ou CNPJ:", alimento.cpf_cnpj)
    print("Descrição do alimento:", alimento.descricao)
    print("Perecível:", "Sim" if alimento.perecivel == 1 else "Não")
    print("Data de validade:", alimento.data_validade)
    print("Peso aproximado (em kg):", alimento.peso)
    print("Volume aproximado (em litros):", alimento.volume)
    print("Endereço para retirada:", alimento.endereco)
    print("Número de telefone para contato via WhatsApp:", alimento.telefone)
    print("Horários e dias da semana para buscar:", alimento.horarios)


def main():
    doacoes = []

    while True:
        print("\n===== Sistema de Doações de Alimentos =====")
        print("1. Cadastrar doação")
        print("2. Listar doações")
        print("3. Pesquisar doação")
        print("4. Sair")
        #consultar lista de determinado | usar o exemplo do dicionario portugues ingues
        #funcao usar o FOR - if para trazer o objeto, remover o cpf e trazer

        opcao = input("\nSelecione uma opção: ")

        if opcao == "1":
            doacao = cadastrar_doacao()
            doacoes.append(doacao)
            print("\nDoação cadastrada com sucesso!")

        elif opcao == "2":
            if not doacoes:
                print("\nNenhuma doação cadastrada.")
            else:
                print("\n===== Lista de Doações Cadastradas =====")
                for i, doacao in enumerate(doacoes):
                    print(f"\n--- Doação {i+1} ---")
                    imprimir_alimento(doacao)

        elif opcao == "3":
           doc_busca = input("Digite o CPF ou CNPJ (somente numeros) para localizar a doação: ")
           busca_resultado = []
           for doacao in doacoes:
               if doacao.cpf_cnpj == doc_busca:
                   busca_resultado.append(doacao)
           if not busca_resultado:
               print("Nenhuma doação encontrada com esses dados.")
           else:
               print("\n===== Lista de Doações Encontradas =====")
               for i, doacao in enumerate(busca_resultado):
                   print(f"\n--- Doação {i + 1} ---")
                   imprimir_alimento(doacao)


        elif opcao == "4":
            break

        else:
            print("\nOpção inválida. Tente novamente.")

    print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()