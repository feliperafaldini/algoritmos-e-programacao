nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"Aluno reprovado, média {media}")
else:
    print(f"Aluno aprovado, média {media}")
    