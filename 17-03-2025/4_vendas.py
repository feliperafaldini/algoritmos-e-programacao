import re

try:
    nome = input("Insira o nome do vendedor: ")
    fixo = float(input(f"Insira o salário de {nome} (em reais): "))
    vendas = float(input(f"Insira o valor de vendas de {nome} (em reais): "))

    comissao = vendas*0.15

    print(f"Vendedor: {nome}\nSalário Fixo: R$ {fixo}\nSalário com vendas: R$ {fixo+comissao}")
except Exception as e:
    print(f"Erro: {e}")