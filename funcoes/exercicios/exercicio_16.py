def imc():
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura * altura)
    return imc

imc = imc()
print(f"O seu imc é {imc:.2f}")