idade = 0
salario = 0

#Entrada de dados
idade = int(input("Qual sua idade?\n"))
salario = float(input("Qual seu salário?\n"))


if idade >= 18:
    # Se a idade for maior ou igual a 18, o programa verifica o salário.
    if salario >= 2000:
        # Se o salário for maior ou igual a 2000 e a idade for maior ou igual a 18, o programa imprime a mensagem abaixo.
        print("Você tem idade suficiente e seu salário é bom.")
    else:
        # Se o salário for menor que 2000 mas a idade for maior ou igual a 18, o programa imprime a mensagem abaixo.
        print("Você tem idade suficiente, mas seu salário não é suficiente.")
else:
    # Se a idade for menor que 18, o programa imprime a mensagem abaixo.
    print("Desculpe, você é muito jovem para esta vaga.")
