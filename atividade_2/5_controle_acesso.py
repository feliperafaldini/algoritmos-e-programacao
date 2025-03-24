idade = int(input("Insira a idade: "))

while (socio := int(input("É sócio: \n(1) - SIM\n(2) - NÃO\n"))) != 1 or socio != 2:
    break

if (
    (idade < 18 and socio == 1)
    or (idade > 18 and idade < 65)
    or (idade >= 65 and socio == 1)
):
    print("Acesso permitido.")
else:
    print("Acesso negado.")
