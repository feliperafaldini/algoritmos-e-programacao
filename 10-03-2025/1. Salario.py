salario = float(input("Insira o salário do funcionário: "))
inss = salario * 0.08
imposto_renda = salario * 0.11
sindicato = salario * 0.05

salario_liquido = salario - inss - imposto_renda - sindicato

print(f"O salário do funcionário foi de R$ {salario_liquido}")
