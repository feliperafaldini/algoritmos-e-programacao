nome = input("Insira o nome do nadador: ")
idade = int(input(f"Insira a idade de {nome}: "))

if idade >= 5 and idade <= 7:
    print(f"O nadador {nome} está na categoria Infantil A.")
elif idade >= 8 and idade <= 10:
    print(f"O nadador {nome} está na categoria Infantil B.")
elif idade >= 11 and idade <= 13:
    print(f"O nadador {nome} está na categoria Juvenil A.")
elif idade >= 14 and idade <= 17:
    print(f"O nadador {nome} está na categoria Juvenil B.")
elif idade > 18:
    print(f"O nadador {nome} está na categoria Sênior.")
