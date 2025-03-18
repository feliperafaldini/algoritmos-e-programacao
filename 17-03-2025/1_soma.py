while True:
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        result = num1 + num2

        print(f"A soma dos números é {result}")

    except Exception as e:
        print(f"Erro: {e}")