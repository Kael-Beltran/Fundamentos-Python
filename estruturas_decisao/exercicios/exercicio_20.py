def caixa_eletronico():
    saldo = float(input("Informe o seu saldo disponível: "))
    saque = float(input("Informe o valor do saque: "))

    if saque <= 0:
        print("Valor de saque inválido")
    elif saque > saldo:
        print("Saldo insuficiente")
    else:
        novo_saldo = saldo - saque
        print(f"Saque realizado com sucesso! Novo saldo: R$ {novo_saldo}")

caixa_eletronico()