import datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

########################################################################################

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

########################################################################################

def depositar(valor):
    global saldo
    global extrato
    if valor > 0:
        saldo += int(valor)
        time_operation = datetime.datetime.now().strftime("%X - %x")
        extrato += f"Depósito: R$ {valor:.2f} - {time_operation}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo
    global numero_saques
    global extrato
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        time_operation = datetime.datetime.now().strftime("%X - %x")
        extrato += f"Saque: R$ {valor:.2f} - {time_operation}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

def show_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

########################################################################################

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        show_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
