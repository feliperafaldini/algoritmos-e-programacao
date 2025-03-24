estados = ["MG", "SP", "RJ", "MS"]
produto = float(input("Insira o valor do produto: "))
estado = input("Insira qual o estado o produto irá ser vendido (sigla): ").upper()

if estado == estados[0]:
    result = produto + (produto*0.07)
    print(f"O valor final do produto é de {result}")
elif estado == estados[1]:
    result = produto + (produto*0.12)
    print(f"O valor final do produto é de {result}")
elif estado == estados[2]:
    result = produto + (produto*0.15)
    print(f"O valor final do produto é de {result}")
elif estado == estados[3]:
    result = produto + (produto*0.08)
    print(f"O valor final do produto é de {result}")