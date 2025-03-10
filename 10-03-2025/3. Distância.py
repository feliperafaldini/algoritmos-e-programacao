x1 = float(input("Insira o valor de x do ponto 1: "))
y1 = float(input("Insira o valor de y do ponto 1: "))
x2 = float(input("Insira o valor de x do ponto 2: "))
y2 = float(input("Insira o valor de y do ponto 2: "))

distancia = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print(f"A distância dos pontos é de {distancia}")
