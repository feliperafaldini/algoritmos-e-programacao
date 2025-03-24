operacoes = ["+", "-", "*", "/"]

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

operacao = input("Insira a operação matemática: ")

try:
    
    if operacao == operacoes[0]:
        result = num1 + num2
        print(f"O resultado de {num1} {operacao} {num2} é {result}")
    elif operacao == operacoes[1]:
        result = num1 - num2
        print(f"O resultado de {num1} {operacao} {num2} é {result}")
    elif operacao == operacoes[2]:
        result = num1 * num2
        print(f"O resultado de {num1} {operacao} {num2} é {result}")
    elif operacao == operacoes[3]:
        result = num1 / num2
        print(f"O resultado de {num1} {operacao} {num2} é {result}")

except Exception as e:
    print(f"Erro: {e}")
