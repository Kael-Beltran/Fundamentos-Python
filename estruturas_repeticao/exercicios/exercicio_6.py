def somar_ate():
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma


resultado = somar_ate(numero)
print(resultado)