# Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar. 

# inteiro = int(input("Digite um número inteiro: "))
# if inteiro <0:
#     print (f"ERRO: O número digitado {inteiro}, é negativo!")
# elif inteiro == 0:
#     print (f"ERRO: O número digitado é {inteiro}.")9
# elif inteiro % 2 == 0:
#     print (f"O número {inteiro} que você digitou, é par!")
# else:
#     print (f"O número {inteiro} que você digitou, é ínpar!") 

# Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B. Entretanto, se o valo de B for 0, imprima uma mensagem de erro e não faça a divisão.

# valorA = int(input("Digite um número inteiro: "))
# valorB = int(input("Digite outro número inteiro: "))
# if valorB == 0:
#     print ("Opa, temos um erro! O valor de B é 0! A divisão não pode acontecer.")
# else:
#     divisao = valorA/valorB
#     print(f"O valor da divisão de {valorA} por {valorB} é igual a: {divisao}")

# Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não (para simplificar, você pode utilizar apenas a informação de o ano é divisível por 4 ou não).

# ano = int(input("Vamos descobrir qual ano é bissexto? Digite algum ano: "))
# if ano % 4 == 0:
#     print (f"O ano de {ano} é bissexto!")
# else:
#     print (f"O ano de {ano} não é bissexto!")

# Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos, sendo o GA valendo 30% e o GB valendo 70%). Caso algum valor informado seja negativo, informe uma mensagem de erro e não realize o cálculo.

# notaGA = int(input("Digite aqui, a sua nota do Grau A: "))
# notaGB = int(input("Digite aqui, a sua nota do Grau B: "))
# notaFinal = (notaGA)*0.3 + (notaGB)*0.7
# if notaGA <0 or notaGB <0:
#     print ("Erro, a sua nota não pode ser um número negativo.")
# elif notaFinal < 70.0:
#     print (f"Sua nota final é: {notaFinal}. Você precisará fazer a prova de Grau C!")
# else:
#     print (f"Sua nota final é: {notaFinal}. Você passou!")

# Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.

# vogais = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
# letraUsuario = input("Digite uma letra: ")
# if letraUsuario in vogais:
#     print (input(f"A letra {letraUsuario}, é uma vogal!"))
# else:
#     print (input(f"A letra {letraUsuario}, é uma consoante!"))

# O que é um parâmetro de entrada de um método?

#Um valor que o metodo precisa pra fazer a ação que ele precisa. Vamos ter ações que vamos precisar de informações externas que o método não sabe.
#Exemplo 1
# def nomedometodosemparametro ():
#     print ("mensagem fixa")
# #Exemplo 2
# def nomedometodocomparametro (parametro):
#     print (parametro)

# nomedometodocomparametro ("eu solicito uma nova informação")
#Exemplo 3
# def qualemaior (a,b):
#     if a>b:
#         print (f"O valor {a} é maior do que o valor {b}")
#     else:
#         print (f"O valor {b} é maior do que o valor {a}")

# qualemaior (15,11)

#O que é o retorno de um método?

#É a reação/resposta/resultado que o método vai nos dar para quem chamou. Mas Retorno de Método não é Impressão na Tela! A chamada do método me retorna o resultado.
#Exemplo 1
# def somaValores(a,b):
#     return a+b

# soma = somaValores (7,5)
# print (f"A soma dos valores é {soma}")
#Exemplo 2
# def nomedometodo (a,b):
#     if a == b:
#         return True
#     else:
#         return False

# def nomedometodo2 (time):
#     if time.lower() == "grêmio":
#         return "Gremista"
#     else:
#         return "Colorado"

# comparacao = nomedometodo (2,2)

# if comparacao:
#     print ("Os valores são iguais")
# else:
#     print ("Os valores são diferentes")

# torcedor = nomedometodo2 ("Internacional")
# print (torcedor)

#Utilizando while, crie um programa que imprime os números de 0 a 1000.

# numeros = 0
# while numeros <= 1000:
#     print (numeros)
#     numeros += 1

#Utilizando while, crie um programa que imprime os números pares de 0 a 2000.

# numeros = 0
# while numeros <= 2000:
#     print (numeros)
#     numeros += 2

#Utilizando while, crie um programa que imprime os números de 0 a 1000 em ordem decrescente (ou seja, de 1000 a 0).

# numeros = 1000
# while numeros >= 0:
#     print (numeros)
#     numeros -= 1

#Utilizando while, crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados. 

# numeros = 0
# soma = 0 :
# while numeros < 10
#     numeroX = int(input("Digite um número inteiro: "))
#     soma += numeroX
#     numeros += 1
# print (f"A soma dos valores digitados é igual a: {soma}")

#Comparando os comandos de repetição for e while, em quais ocasiões é mais comum a utilização de um ou de outro?

#While é usado quando não temos uma quantidade x de vezes que o nosso código repitirá. Já o for é usado quando temos uma quantidade fixa de iterações a serem realizadas.

#Utilizando for, crie um programa imprime na tela os valores de 1 a 100 (incluindo o 1 e o 100).

# numeros = range(1,1001,1)
# for i in numeros:
#     print (i)

#Utilizando for,crie um programa que imprime a tabuada de um número inteiro digitado pelo usuário.

# numero = int(input("Vamos descobrir a tabuada de algum número? Digite ele aqui: "))
# tabuada = range (1,10)
# for i in tabuada:
#     print (i) * (tabuada)

#Crie um programa que permita que o usuário crie sua lista de compras.

# x = int(input("Digite a quantidade de Produtos que você irá comprar: "))

# ListadeProdutos.append = 
# print (ListadeProdutos)