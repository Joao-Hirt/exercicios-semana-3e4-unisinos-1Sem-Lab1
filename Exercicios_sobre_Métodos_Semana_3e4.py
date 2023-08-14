#1: Crie um método que recebe dois valores val1 e val2 (assuma que serão inteiros). O método deve retornar verdadeiro se val1 for divisível por val2 e falso caso contrário.

# def valores(val1, val2):
#     if val1 % val2 == 0:
#         return True
#     else:
#         return False

# resultado = valores(4, 2)
# print (resultado)


#2: Crie um método chamado maiorValor que recebe 3 valores por parâmetro (assuma que serão inteiros) e retorna o maior dos três valores.

# def maiorValor(val1, val2, val3):
#      if val1 > val2 and val1 > val3:
#           return val1
#      elif val2 > val1 and val2 > val3:
#           return val2
#      else:
#           return val3

# valorMaior = maiorValor(3,4,80)
# print (valorMaior)


#3: Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e retorna a soma de todos os valores entre 0 e o valor recebido. Caso o valor seja negativo, o método deve retornar -1.

# def valorPorParametro(val1):
#     if val1 > 0:
#         soma = sum(range(val1+1))
#         return (soma)
#     else:
#         return (-1)
    
# valorFinal = valorPorParametro (-4)
# print (valorFinal)


#4: Crie um método que recebe um valor por parâmetro (assuma que será uma string) e retorna a quantidade de letras ou outros caracteres que não sejam espaço que existem neste texto.

# def parametroLetras(a):
#     quantLetras = 0
#     for i in a:
#         if i.isalpha():
#             quantLetras += 1
#     return quantLetras

# resultado = parametroLetras ("Who Dey!")
# print (resultado)


#5: Crie um método que recebe uma lista por parâmetro e imprime os elementos da lista recebida.

# def parametrodeLista(lista):
#     for i in lista:
#         print (i)


#6: Crie um método que recebe uma lista por parâmetro (assuma que será uma lista de string) e retorna a menor string da lista (com menos caracteres).

# def menorString(lista):
#     menor = lista[0]
#     for i in lista:
#         if len(i) < len(menor):
#             menor = i
#     return (menor)

# lista = ["bengals", "eagles", "steelers", "browns", "jets", "chiefs"]
# acheamenorstring = menorString(lista)
# print(acheamenorstring)


#7: Crie um método que recebe dois parâmetros, que serão um inteiro N e uma string S (nesta ordem). O método deve imprimir na tela N vezes a string S.

# def parametrosVezes (n,s):
#     for i in range(n):
#         print (s)

# resultado = parametrosVezes(2, "WHO DEY! WHO DEY! WHO DEY THINK GON BEAT THEM BENGALS, NOOOOBODY")


#8: Crie um método que recebe um inteiro X por parâmetro e imprime os valores de 1 até X (inclusive).

# def metodoContador(x):
#     for i in range(1,x+1):
#         print (i)
# resultado = metodoContador(7)


#9: Crie um método que recebe 3 notas por parâmetro e retorna o conceito atingido pela média aritmética das notas.

# def mediaNotas (n1, n2, n3):
#     if (n1 >= 0 and n2 >= 0 and n3 >= 0):
#         notafinal = (n1+n2+n3)/3
#         if notafinal <= 4.0:
#             return("D")
#         elif notafinal <= 7.0:
#             return("C")
#         elif notafinal <= 9.0:
#             return("B")
#         else:
#             return("A")

# resultado = mediaNotas(9.4, 8.3, 9.3)
# print (resultado)


#10: Crie um método que recebe um inteiro por parâmetro e retorna verdadeiro caso seja um valor primo e falso caso contrário. Caso o parâmetro seja negativo o método deve retornar falso.

# def primoOuNao (x):
#     if x <= 1:
#         return False
#     if x == 2:
#         return True
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
    
# descobrir = primoOuNao (2)
# print (descobrir)

