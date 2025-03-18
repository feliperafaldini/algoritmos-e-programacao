try:
    dist = float(input("Insira a distância percorrida pelo veículo em KM: "))
    fuel = float(input("Insira a quantidade de combustível gasto no percurso: "))

    fuel_usage = dist/fuel

    print(f"O consumo médio de combustível foi de {fuel_usage} km por litro de combustível.")
except Exception as e:
    print(f"Erro: {e}")