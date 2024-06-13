menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente para realizar o saque.")
    elif excedeu_limite:
        print("Falha! O valor do saque excede o limite máximo por saque de R$ 500.00.")
    elif excedeu_saques:
        print("Operação falhou! Limite diário de saques atingido. Tente novamente amanhã.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def visualizar_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "3":
        visualizar_extrato()

    elif opcao == "4":
        print("Obrigado por utilizar o sistema bancário!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

