#1. Crie um programa que pede para o usuário digitar o nome de 13 pessoas pelo teclado.
# i = 0
# while i < 13:
#     input("Digite um nome: ")
#     i += 1


#2. Crie um programa que imprime os números de 0 a 1000.
# numeros = 0
# while numeros <= 1000:
#     print (numeros)
#     numeros += 1


#3. Crie um programa que imprime os números pares de 0 a 2000.
# numeros = 0
# while numeros <= 2000:
#      print (numeros)
#      numeros += 2


#4. Crie um programa que imprime os números de 0 a 1000 em ordem decrescente (ou seja, de 1000 a 0).
# numeros = 1000
# while numeros >= 0:
#     print (numeros)
#     numeros -= 1


#5. Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final, imprima quantos torcedores torcem para o Grêmio.

# teamsCount = 0
# gremioCount = 0
# while teamsCount < 10:
#     userteam = input("Digite para qual time você torce: ")
#     if userteam == "Grêmio":
#         gremioCount += 1
#     teamsCount += 1
# print (f"Tivemos {gremioCount} torcedores Grêmistas")


#6. Crie um programa que pede para o usuário digitar 20 números com ponto flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final, imprima a string.

# i = 0
# listaNumeros = []
# while i < 20:
#     listaNumeros.append(float(input("Digite um número com ponto flutuante: ")))
#     i += 1
# print (listaNumeros)


#7. Crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados.

# i = 0
# total = 0
# while i <10:
#     x = int(input("Digite um número inteiro: "))
#     total = total+x
#     i += 1
# print (total)


#8. Crie um programa que pergunta para o usuário (via Teclado) quantos números ele irá digitar e armazena em uma variável chamada quant. Logo após, faça com que o usuário digite quant números inteiros, e para cada número digitado imprima na tela se o número é negativo, positivo ou zero.

# quant = int(input("Digite quantos números você irá digitar: "))
# i = 0
# while i < quant:
#     x = int(input("Digite um numero: "))
#     if x == 0:
#         print ("O número digitado é Zero!")
#     elif x > 0:
#         print ("O número digitado é Positivo!")
#     else:
#         print ("O número digitado é Negativo!")
#     i += 1


#9. Crie um programa que pede para o usuário digitar 2 valores inteiros via Teclado (val1 e val2). Se nenhum dos valores for negativo, escreva os números pares entre o menor e o maior valor.

# val1 = int(input("Digite o primeiro valor: "))
# val2 = int(input("Digite o segundo valor: "))
# if val1 >= 0 and val2 >= 0:
#     if val1 > val2:
#         numeros = val2
#         while numeros <= val1:
#             if numeros %2 == 0:
#                 print (numeros)
#                 numeros += 2
#             else:
#                 numeros += 1
#                 print (numeros)
#     else:
#         numeros = val1
#         while numeros <= val2:
#             if numeros %2 == 0:
#                 print (numeros)
#                 numeros += 2
#             else:
#                 numeros += 1
#                 print (numeros)


#10. Crie um programa que faça a soma dos valores de 0 até 198.

# i = 0
# total = 0
# while i <= 198:
#     total = total+i
#     i += 1
# print (total)


#11. Crie um programa que imprima a soma dos valores pares e a soma dos valores ímpares entre dois números quaisquer digitados pelo usuário.

# val1 = int(input("Digite o primeiro valor: "))
# val2 = int(input("Digite o segundo valor: "))
# totalPares = 0
# totalImpares = 0

# if val1 < val2:
#     i = val1
#     while i < val2:
#         if i %2 == 0:
#             totalPares += i
#         else:
#             totalImpares += i
#         i += 1
#     print (f"O valor da soma dos pares entre {val2} e {val1} é igual a: {totalPares}")
#     print (f"O valor da soma dos impares entre {val2} e {val1} é igual a: {totalImpares}")
# else:
#     i = val2
#     while i < val1:
#         if i %2 == 0:
#             totalPares += i
#         else:
#             totalImpares += i
#         i += 1
#     print (f"O valor da soma dos pares entre {val1} e {val2} é igual a: {totalPares}")
#     print (f"O valor da soma dos impares entre {val1} e {val2} é igual a: {totalImpares}")


#12. Crie um programa que pede para o usuário digitar números positivos via Teclado. Quando o usuário digitar um número negativo, informe a média de todos os números que ele informou.

# count = 0
# total = 0
# while valorPositivo >= 0:
#     valorPositivo = int(input("Digite números positivos: "))
#     if valorPositivo < 0:
#         break
#     total += valorPositivo
#     count += 1
# print (f"A média dos valores positivos digitados é: {total/count}")


#13. Crie um programa que calcule o fatorial de um número informado pelo usuário (não permita números negativos).

# print ("Quer descobrir o fatorial de um número?")
# valor = int(input("Digite aqui o número: "))
# if valor >= 0:
#     if valor == 0 or valor == 1:
#         print(f"Fatorial de {valor} é 1")
#     else:
#         total = valor
#         fatorial = 1
#         while total > 1:
#             fatorial *= total
#             total -= 1
#         print (f"O fatorial de {valor} é igual a: {fatorial}")
# else:
#     print ("Erro, o valor digitado não pode ser igual ou menor que Zero!")


#14. Crie um programa que diga se o número informado pelo usuário é primo ou não.

print ("Bora descobrir se um número é primo ou não?")
numero = int(input("Digite aqui o número: "))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print (f"O número {numero} não é primo :/ ")
            break
    else:
        print (f"O número {numero} é primo!")
elif numero <= 1 and numero >= 0:
    print (f"O número {numero} não é primo :/ ")
else:
    print (f"Os números negativos não são considerados primos!")
