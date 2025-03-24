num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

if num1 == num2:
    result = num1 + num2
    print(f"O resultado da soma de {num1} + {num2} foi {result}")
else:
    result = num1 * num2
    print(f"O resultado da multiplicação de {num1} * {num2} foi {result}")
