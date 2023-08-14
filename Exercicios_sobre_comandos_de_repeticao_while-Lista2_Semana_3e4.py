#1. Faça o código que implementa o algoritmo descrito no fluxograma abaixo:

# count = 0
# while count < 10:
#     numero = int(input("Digite um número: "))
#     if numero < 0:
#         print ("Número Negativo.")
#     elif numero == 0:
#         print ("Zero.")
#     else:
#         print ("Número Positivo.")
#     count += 1


#2. Faça um programa que escreva na tela todos os números inteiros entre 0(inclusive) e 1000 (inclusive).

# numero = 0
# while numero <=1000:
#     print (numero)
#     numero += 1


#3. Faça um programa que escreva na tela todos os valores inteiros que estão entre dois valores digitados pelo usuário (num1 e num2). Caso num1 seja maior do que num2, imprima uma mensagem de erro e não imprima.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# if num1 < num2:
#     cont = num1+1
#     while cont < num2:
#         print (cont)
#         cont += 1
# else:
#     print ("Erro! O primeiro valor tem que ser menor que o segundo!")


#4. Faça um programa que escreva na tela todos os valores inteiros entre dois valores digitados pelo usuário (num1 e num2). Caso num1 seja maior do que num2, seu programa deve imprimir os valores entre num1 e num2 da mesma forma.

# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))

# if num1 < num2:
#     cont = num1+1
#     while cont < num2:
#         print (cont)
#         cont += 1
# else:
#     cont = num1-1
#     while cont > num2:
#         print (cont)
#         cont -= 1


#5. Faça um programa que imprima na tela a soma de todos os valores entre 1 e 1000.

# cont = 1
# soma = 0
# while cont <= 1000:
#     soma += cont
#     cont +=1
# print (soma)


#6. Faça um programa que solicita ao usuário que ele digite números que sejam positivos e pares. Quando o usuário digitar um número que não seja o solicitado, imprima na tela a soma dos valores positivos e pares digitados.

# num = int(input("Digite um número positivo e par: "))
# soma = 0
# while num > 0 and num %2 == 0:
#     soma += num
#     num = int(input("Digite um número positivo e par: "))
# print (soma)


#7. O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que solicita ao usuário que ele digite seu usuário e senha. O programa só termina quando ele acertar o usuário e a senha. Quando ele acertar, você deve informar a mensagem: LOGIN EFETUADO COM SUCESSO.

# user = input("Digite o seu usuário: ")
# password = input("Agora digite a sua senha: ")
# while user != "USER10" or password != "PASSWORD1234":
#     print ("Usuário e/ou Senha incorretos, tente novamente.")
#     user = input("Digite o seu usuário: ")
#     password = input("Agora digite a sua senha: ")
# print ("LOGIN EFETUADO COM SUCESSO.")


#8. O usuário e a senha de um cliente são, respectivamente, USER10 e PASSWORD1234. Sabendo disso, faça um programa que solicita ao usuário que ele digite seu usuário e senha. O programa termina quando ele acertar o usuário e a senha ou quando ele exceder o máximo de 3 tentativas. Quando ele acertar, o programa deve informar a mensagem: LOGIN EFETUADO COM SUCESSO. Caso ele exceda a quantidade de tentativas, o programa deve informar a mensagem: NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO!

user = input("Digite o seu usuário: ")
password = input("Agora digite a sua senha: ")
tentativas = 0
acerto = False
while user != "USER10" or password != "PASSWORD1234":
    print ("Usuário e/ou Senha incorretos, tente novamente.")
    user = input("Digite o seu usuário: ")
    password = input("Agora digite a sua senha: ")
    tentativas += 1
    if user == "USER10" and password == "PASSWORD1234":
        acerto = True
    if tentativas == 2:
        break
if not acerto and tentativas > 0:
    print ("NÚMERO MÁXIMO DE TENTATIVAS EXCEDIDO.")
else:
    print ("LOGIN EFETUADO COM SUCESSO.")