generos = ["h", "m"]

altura = float(input("Insira a altura da pessoa (em metros com ponto): "))

genero = input("Insira o genero da pessoa: ")

if genero == generos[0]:
    result = (72.7 * altura) - 58
    print(f"O peso ideal do homem de {altura} é {result}")
elif genero == generos[1]:
    result = (62.1 * altura) - 44.7
    print(f"O peso ideal da mulher de {altura} é {result}")