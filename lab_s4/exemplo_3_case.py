
nota = 0

#Entrada de dados
nota = int(input("Entre com sua nota para verificar sua classificação entre A | B | C | D\n"))

match nota:
    case n if n >= 9:
        # Se a nota for maior ou igual a 9, o programa imprime a mensagem abaixo.
        print("Parabéns! Sua nota é A.")
    case n if n >= 7:
        # Se a nota não for maior ou igual a 9, mas for maior ou igual a 7, o programa imprime a mensagem abaixo.
        print("Sua nota é B.")
    case n if n >= 5:
        # Se a nota não for maior ou igual a 7, mas for maior ou igual a 5, o programa imprime a mensagem abaixo.
        print("Sua nota é C.")
    case _:
        # Se a nota não for maior ou igual a 5, o programa imprime a mensagem abaixo.
        print("Sua nota é D.")