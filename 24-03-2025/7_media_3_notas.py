nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))

media = (nota1 + nota2+ nota3) / 3

if media < 7:
    print(f"O aluno foi reprovado com média {media}")
elif media < 10:
    print(f"O aluno foi aprovado com média {media}")
else:
    print(f"O aluno foi aprovado com distinção. Média {media}")