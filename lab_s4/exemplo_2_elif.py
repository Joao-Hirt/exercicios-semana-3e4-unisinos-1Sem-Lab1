nota = 0

#Entrada de dados
nota = int(input("Entre com sua nota para verificar sua classificação entre A | B | C | D\n"))

if nota >= 9:
    # Se a nota for maior ou igual a 9, o programa imprime a mensagem abaixo.
    print("Parabéns! Sua nota é A.")
elif nota >= 7:
    # Se a nota não for maior ou igual a 9, mas for maior ou igual a 7, o programa imprime a mensagem abaixo.
    print("Sua nota é B.")
elif nota >= 5:
    # Se a nota não for maior ou igual a 7, mas for maior ou igual a 5, o programa imprime a mensagem abaixo.
    print("Sua nota é C.")
else:
    # Se a nota não for maior ou igual a 5, o programa imprime a mensagem abaixo.
    print("Sua nota é D.")