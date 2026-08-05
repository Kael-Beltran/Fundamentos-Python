def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    return media

nota_final = calcular_media()
print(f"A nota final foi {nota_final:.2f}")