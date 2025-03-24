prova1 = float(input("Insira a nota da primeira prova: "))
peso1 = float(input("Insira o peso da primeira prova: "))
prova2 = float(input("Insira a nota da segunda prova: "))
peso2 = float(input("Insira o peso da segunda prova: "))
prova3 = float(input("Insira a nota da terceira prova: "))
peso3 = float(input("Insira o peso da terceira prova: "))

media = ((prova1 * peso1) + (prova2 * peso2) + (prova3 * peso3)) / (
    peso1 + peso2 + peso3
)

if media >= 7:
    print(f"Média: {media}\nAprovado")
elif media >= 5 and media < 7:
    print(f"Média: {media}\nEm recuperação.")
else:
    print(f"Média: {media}\nAluno reprovado")
