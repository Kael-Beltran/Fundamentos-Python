def energia():
    kWh = float(input("Quantos kWh voce consumiu esse mês: "))
    valor = float(input("Qual o valor do kWh: "))
    preco = kWh * valor
    print(f"O consumo mensal é {preco:.2f}$")

energia()