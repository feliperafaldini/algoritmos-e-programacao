try:
    nome = input("Insira o nome do aluno: ")
    notas = []

    for i in range(3):
        notas.append(float(input(f"Insira a nota número {i+1}: ")))

    media = (notas[0] + notas[1] + notas[2]) / 3

    print(f"Média do aluno {nome} foi de {media}.")

except Exception as e:
    print(f"Erro: {e}")