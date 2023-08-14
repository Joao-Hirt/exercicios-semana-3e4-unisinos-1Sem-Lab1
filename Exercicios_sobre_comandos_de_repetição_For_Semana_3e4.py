#1. Crie um programa imprime na tela os valores de 1 a 100 (incluindo o 1 e o 100).

# for i in range (1, 101):
#     print (i)


#2. Crie um programa que imprime na tela todos os valores entre dois valores digitados pelo teclado.

# val1 = int(input("Digite um número: "))
# val2 = int(input("Digite um número: "))

# if val1 < val2:
#     for i in range(val1+1,val2):
#         print (i)
# else:
#     for i in range(val2+1,val1):
#         print (i)


#3. Crie um programa que imprime a tabuada de um número qualquer digitado pelo usuário.

# num = int(input("Digite um número: "))
# tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in tabuada:
#     print (i*num)


#4. Sabendo que uma string é uma lista de letras, peça para o usuário digitar um texto e imprima na tela a quantidade de vogais que existem no texto.

# frase = input("Digite uma breve frase: ")
# quantidadeVogais = 0
# vogais = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

# for letra in frase:
#     if letra in vogais:
#         quantidadeVogais += 1
# print (quantidadeVogais)


#5. Crie um programa que permita que o usuário crie sua lista de compras. 

# quant = int(input("Digite a quantidade de produtos: "))
# lista = []

# for i in range(0,quant):
#     produtos = input("Digite o nome dos produtos: ")
#     lista.append(produtos)

# print(lista)


# 6. Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo teclado. 

# listaNome = []
# listaSolteiras = []
# listaCasadas = []
# listaDivorciadas = []
# listaViuvas = []

# for i in range(8):
#     nome = input ("Digite o nome da pessoa: ")
#     estadoCivil = input("Digite o Estado Civil: ")
#     if (estadoCivil == "solteiro" or estadoCivil == "solteira"):
#         listaSolteiras.append(nome)
#     elif (estadoCivil == "casado" or estadoCivil == "casada"):
#         listaCasadas.append(nome)
#     elif (estadoCivil == "divorciado" or estadoCivil == "divorciada"):
#         listaDivorciadas.append(nome)
#     elif (estadoCivil == "viuvo" or estadoCivil == "viuva"):
#         listaViuvas.append(nome)
#     else:
#         print ("[ERRO] Estado Civil Invalido.")

# print ("Pessoas Solteiras:")
# print (listaSolteiras)

# print ("Pessoas Casadas:")
# print (listaCasadas)

# print ("Pessoas Divorciadas:")
# print (listaDivorciadas)

# print ("Pessoas Viúvas:")
# print (listaViuvas)



#7. Crie um programa que solicita ao usuário que ele defina sua senha.

# acerto = False
# for i in range (0,6):
#     senha = input("Digite sua nova senha: ")

#     if senha.isdigit() and len(senha) >=5 and len(senha) <= 10:
#         print("Sua senha foi cadastrada com sucesso!")
#         acertou = True
#         break
#     else:
#         print ("Senha Inválida.")
#     if not acerto:
#         print("Quantidade de tentativas excedida =/")


#8. Crie um programa que separa o joio do trigo.

listaTrigo = []
listaJoio = []

joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo",
"joio", "joio", "joio", "joio", "trigo", "trigo", "joio",
"joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"joio", "joio", "joio", "joio", "joio", "joio", "joio",
"joio", "trigo", "trigo", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "joio", "joio",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "joio", "joio", "joio", "joio",
"joio", "joio", "trigo", "joio", "joio", "joio", "joio",
"joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
"trigo", "joio", "trigo", "joio", "joio", "joio"]

for joio in joioETrigo:
    listaJoio.append("joio")
for trigo in joioETrigo:
    listaTrigo.append("trigo")

print(listaTrigo)
print(listaJoio)