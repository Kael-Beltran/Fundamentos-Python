def compras():
    produto = float(input("Digite o valor do produto: "))
    parcelas = float(input("Digite a quantidade de parcelas: "))
    valor_parcela = produto / parcelas
    return valor_parcela

valor_parcela = compras()
print(f"O valor de uma parcela é {valor_parcela:.2f}$")