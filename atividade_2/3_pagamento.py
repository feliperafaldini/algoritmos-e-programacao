import os

os.system("cls")

metodos = [1, 2, 3, 4]
valor = float(input("Insira o valor do produto: "))

while (
    pagamento := int(
        input(
            "Selecione o método de pagamento:\n1 - Dinheiro ou Pix.\n2 - À vista no Cartão de Crédito.\n3 - Duas vezes no Cartão de Crédito.\n4 - Três vezes no Cartão de Crédito.\n"
        )
    )
) not in metodos:
    break

os.system("cls")

if pagamento == metodos[0]:
    valor_final = valor - (valor * 0.1)
    print(f"Total a pagar R$ {valor_final:.2f}")
elif pagamento == metodos[1]:
    valor_final = valor - (valor * 0.15)
    print(f"Total a pagar R$ {valor_final:.2f}")
elif pagamento == metodos[2]:
    valor_parcela = valor / 2
    print(f"Total a pagar R$ {valor:.2f} em duas parcelas de R$ {valor_parcela:.2f}")
elif pagamento == metodos[3]:
    valor_final = valor + (valor * 0.1)
    valor_parcela = valor_final / 3
    print(
        f"Total a pagar R$ {valor_final:.2f} em três parcelas de R$ {valor_parcela:.2f}"
    )
