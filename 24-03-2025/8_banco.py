saldo = float(input("Insira o saldo médio do cliente: "))

if saldo < 200:
    result = 0
    print(f"O crédito do cliente de saldo R$ {saldo} é de R$ {result}")
elif saldo < 400:
    result = saldo * 0.2
    print(f"O crédito do cliente de saldo R$ {saldo} é de R$ {result}")
elif saldo < 600:
    result = saldo * 0.3
    print(f"O crédito do cliente de saldo R$ {saldo} é de R$ {result}")
else:
    result = saldo * 0.4
    print(f"O crédito do cliente de saldo R$ {saldo} é de R$ {result}")