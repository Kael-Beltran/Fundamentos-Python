from variaveis.exercicios.exercicio_9 import produto


def compras():
    produto = float(input("Digite o valor do produto: "))
    desconto = float(input("Digite o desconto do produto: "))
    valor_final =(produto * desconto) / 100
    return produto, valor_final

valor = compras()
print(f"O produto de {produto} reais com o desconto ficou {valor:.2f} reais!")
    