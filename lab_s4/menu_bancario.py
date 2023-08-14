# Variável para armazenar o saldo da conta
saldo_conta = 1000.0

# Função para realizar um saque na conta bancária
def saque(valor):
    # Implementação do saque
    global saldo_conta
    if valor <= saldo_conta:
        saldo_conta -= valor
        print("Saque realizado com sucesso. Retire o dinheiro abaixo.")
    else:
        print("Saldo insuficiente para realizar o saque. Seu saldo é de R$",saldo_conta)


# Função para realizar um depósito na conta bancária
def deposito(valor):
    # Implementação do depósito
    global saldo_conta
    saldo_conta += valor
    print("Depósito realizado com sucesso.")

# Função para realizar uma transferência para outra conta bancária
def transferencia(valor, conta_destino):
    # Implementação da transferência
    global saldo_conta
    if valor <= saldo_conta:
        saldo_conta -= valor
        print("Transferência realizada com sucesso. O valor de R$", valor, "foi transferido para a conta", conta_destino, ".")
    else:
        print("Saldo insuficiente para realizar a transferência.")

# Função para consultar o saldo da conta bancária
def saldo():
    global saldo_conta
    print("Saldo atual da conta: R$", saldo_conta)

# Opções de transações bancárias
opcoes = [
    ("1", "Saque"),
    ("2", "Depósito"),
    ("3", "Transferência"),
    ("4", "Consulta de saldo"),
    ("0", "Sair")
]

# Loop principal do menu
while True:
    # Imprime as opções disponíveis
    print("Escolha uma opção:")
    for opcao in opcoes:
        print(f"{opcao[0]} - {opcao[1]}")

    # Lê a opção escolhida pelo usuário
    escolha = input("Opção: ")

    # Realiza a transação bancária correspondente à escolha do usuário
    match escolha:
        case "1":
            # Realiza um saque na conta bancária
            valor = float(input("Digite o valor do saque: "))
            saque(valor)
        case "2":
            # Realiza um depósito na conta bancária
            valor = float(input("Digite o valor do depósito: "))
            deposito(valor)
        case "3":
            # Realiza uma transferência para outra conta bancária
            valor = float(input("Digite o valor da transferência: "))
            conta_destino = input("Digite o número da conta de destino: ")
            transferencia(valor, conta_destino)
        case "4":
            # Consulta o saldo da conta bancária
            saldo()
        case "0":
            # Sai do menu
            print("Obrigado por utilizar nosso serviço.")
            exit()
        case _:
            # Caso a opção escolhida não seja válida
            print("Opção inválida. Escolha uma opção válida.")

#POC
""""
deposito(500.0)
consulta_saldo()
saque(200.0)
consulta_saldo()
transferencia(300.0, "12345-6")
consulta_saldo()

"""