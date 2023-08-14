#Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.

# numero = int(input("Digite um número: "))
# if numero %2 == 0:
#     print (f"O número {numero} é par!")
# else:
#     print (f"O número {numero} é ímpar!")


#Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.
# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# if numero1 > numero2:
#     print (f"O número {numero1} é maior que {numero2}!")
# elif numero1 == numero2:
#     print (f"Os números {numero1} e {numero2} são iguais!")
# else:
#     print (f"O número {numero2} é maior que {numero1}!")


#Crie um programa que recebe dois valores inteiros A e B pelo teclado e imprime o valor de A dividido por B. Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.

# numeroA = int(input("Digite um número: "))
# numeroB = int(input("Digite outro número: "))
# if numeroB == 0:
#     print ("ERRO! Não podemos fazer divisão com 0!")
# else:
#     print (f"A divisão entre {numeroA} por {numeroB} é igual a: {numeroA/numeroB}")


#Crie um programa que recebe três valores inteiros pelo teclado e imprime qual dos três é menor.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# numero3 = int(input("Digite mais um número: "))
# if numero1 < numero2 and numero1 < numero3:
#     print(f"O número {numero1} é o menor digitado!")
# elif numero2 < numero1 and numero2 < numero3:
#     print(f"O número {numero2} é o menor digitado!")
# else:
#     print(f"O número {numero3} é o menor digitado!")


#Crie um programa que recebe o preço de um produto pelo teclado e imprime na tela a mensagem adequada, de acordo com o preço:

# preco = float(input("Digite o valor do produto: "))
# if preco <= 0:
#     print ("Preço inválido")
# elif preco <= 30:
#     print ("Preço baixo")
# elif preco <= 50:
#     print ("Preço médio")
# else:
#     print ("Preço alto")


#Crie um programa que aplica uma taxa de juros em um determinado preço digitado pelo teclado. A taxa aplicada deve ser:

# preco = float(input("Digite o valor do produto: "))
# if preco <= 0:
#     print ("ERRO! O valor digitado é inválido")
# elif preco < 100:
#     print (f"O valor após a taxa de 10% é igual a: {preco+(preco*0.1)}")
# elif preco <300:
#     print (f"O valor após a taxa de 20% é igual a: {preco+(preco*0.2)}")
# else:
#     print (f"O valor após a taxa de 50% é igual a: {preco+(preco*0.5)}")


#Crie um programa que recebe um valor inteiro referente a um determinado ano. Imprima na tela se o ano informado é bissexto ou não.
# print ("Vamos descobrir qual ano é bissexto?")
# ano = int(input("Digite o ano que você quer saber: "))
# if ano %4 == 0:
#     print (f"O ano de {ano} é bissexto!")
# else:
#     print (f"O ano de {ano} não é bissexto!")


#Crie um programa que exibe um menu de calculadora na tela. O menu exibido deve ser o seguinte:

# print("Calculadora do Hirt")
# print("Menu:")
# print("Digite 1 para somar dois valores.")
# print("Digite 2 para subtrair dois valores.")
# print("Digite 3 para multiplicar dois valores.")
# print("Digite 4 para dividir dois valores.")
# print("Digite 5 para realizar uma potência entre dois valores.")
# print("Digite 6 para realizar uma radiciação entre dois valores.")
# print("Digite qualquer outro número para sair.")
# usuario = int(input(""))
# a = (int(input("Digite o primeiro número: ")))
# b = (int(input("Digite o segundo número: ")))
# if usuario == 1:
#     print (f"O valor de {a} mais {b} é igual a: {a+b}")
# elif usuario == 2:
#     print (f"O valor de {a} menos {b} é igual a: {a-b}")
# elif usuario == 3:
#     print (f"O valor de {a} vezes {b} é igual a: {a*b}")
# elif usuario == 4:
#     if b != 0:
#         print (f"O valor de {a} dividido por {b} é igual a: {a/b}")
#     else:
#         print (f"Não é possível dividir por zero!")
# elif usuario == 5:
#     print (f"O valor de {a} potencializado por {b} é igual a: {a**b}")
# elif usuario == 6:
#     print (f"O valor de {a} radicializado por {b} é igual a: {a**(1/b)}")
# else:
#     print ("Nos vemos na próxima!")


#. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se será necessário ou não realizar o Grau C
# print ("Preciso fazer o Grau C?")
# grauA = float(input("Digite a nota do Grau A: "))
# grauB = float(input("Digite a nota do Grau B: "))
# total = grauA+grauB
# if grauA < 0:
#     print("Erro! Algum valor é negativo!")
# elif grauA >= 70:
#     print("Parabéns! Você não precisa fazer o Grau C!")
# else:
#     print("Você precisa fazer o grau C!")


#Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.
# vogais = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
# print ("Vamos descobrir se uma letra é Vogal ou Consoante!")
# letra = input("Digite uma letra: ")
# if letra in vogais:
#     print (f"A letra: {letra}, é Vogal!")
# else:
#     print (f"A letra: {letra}, é Consoante!")