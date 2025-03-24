idade = int(input("Insira a idade do trabalhador: "))
tempo = float(input("Insira o tempo de serviço do trabalhador: "))

if (idade >= 65 or tempo == 30 or (idade >= 60 and tempo >= 25)):
    print(f"O trabalhador pode se aposentar.")
else: 
    print(f"O trabalhador ainda não pode se aposentar.")