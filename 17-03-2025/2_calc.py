while True:
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        sum = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        print(f"Os números {num1} e {num2}\nSomados = {sum}\nSubtraidos = {sub}\nMultiplicados = {mult}\nDividos = {div}")
    except Exception as e:
        print(f"Erro: {e}")