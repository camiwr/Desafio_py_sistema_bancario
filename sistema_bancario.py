def exibir_menu():
    menu = """\n
    =_=_=_=_=_=_ MENU =_=_=_=_=_=_=

    [1] Cadastrar Usuário
    [2] Cadastrar Conta Corrente
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Listar Contas
    [0] Sair
    => """
    return input(menu)

def cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro! Já existe um usuário cadastrado com esse CPF.")
            return
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def cadastrar_conta(usuarios, contas, numero_conta, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario, "saldo": 0.0, "extrato": [], "numero_saques": 0}
            contas.append(conta)
            print(f"Conta corrente {numero_conta} cadastrada com sucesso!")
            return numero_conta + 1
    print("Erro! Usuário não encontrado. Verifique o CPF e tente novamente.")
    return numero_conta

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
    else:
        print("\n=_=_=_=_=_=_ LISTA DE CONTAS =_=_=_=_=_=_=")
        for conta in contas:
            usuario = conta["usuario"]
            print(f"Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']} | Usuário: {usuario['nome']}")
        print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")

def buscar_conta(contas, numero_conta):
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return conta
    return None

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def visualizar_extrato(saldo, /, *, extrato):
    print("\n=_=_=_=_=_=_ EXTRATO =_=_=_=_=_=_=")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")

def main():
    usuarios = []
    contas = []
    numero_conta = 1

    LIMITE_SAQUES = 3
    LIMITE = 500.0

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            nome = input("Informe o nome do usuário: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF (apenas números): ")
            endereco = input("Informe o endereço (logradouro, nro bairro cidade/sigla estado): ")
            cadastrar_usuario(usuarios, nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário para a nova conta: ")
            numero_conta = cadastrar_conta(usuarios, contas, numero_conta, cpf)

        elif opcao == "3":
            num_conta = int(input("Informe o número da sua conta corrente para depósito: "))
            conta = buscar_conta(contas, num_conta)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta["saldo"], conta["extrato"] = depositar(conta["saldo"], valor, conta["extrato"])
            else:
                print("Conta não encontrada!")

        elif opcao == "4":
            num_conta = int(input("Informe o número da sua conta corrente para saque: "))
            conta = buscar_conta(contas, num_conta)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta["saldo"], conta["extrato"], conta["numero_saques"] = sacar(
                    saldo=conta["saldo"], valor=valor, extrato=conta["extrato"], limite=LIMITE, 
                    numero_saques=conta["numero_saques"], limite_saques=LIMITE_SAQUES
                )
            else:
                print("Conta não encontrada!")

        elif opcao == "5":
            num_conta = int(input("Informe o número da sua conta corrente para ver extrato: "))
            conta = buscar_conta(contas, num_conta)
            if conta:
                visualizar_extrato(conta["saldo"], extrato=conta["extrato"])
            else:
                print("Conta não encontrada!")

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Obrigado por utilizar o sistema bancário!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
