# for i in range (0, 192):
#     print (i)

# for i in range (747,938):
#     print (i)

# for i in range (191,0):
#     print(i)

# for i in range (747,939):
#     print (i)


def maiorValor(n):
  lista = []
  for i in range(0, n):
    lista.append(input("Digite um valor: "))
  return lista

valor = maiorValor(9)
print (valor)