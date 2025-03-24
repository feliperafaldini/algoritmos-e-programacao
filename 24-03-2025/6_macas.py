macas = int(input("Insira uma quantidade de maçãs: "))

if macas < 12:
    result = macas * 0.8
    print(f"O valor total de {macas} foi R$ {result}")
else:
    result = macas * 0.65
    print(f"O valor total de {macas} foi R$ {result}")