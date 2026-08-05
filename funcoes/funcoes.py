def exibir_mensagem():
    print("Hello World!")


def somar():
    valor1 = 50
    valor2 = 60
    total = valor1 + valor2
    print(f"O resultado da soma é {total}")


def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    return media


exibir_mensagem()
somar()
nota_final = calcular_media()
print(f"A nota final foi {nota_final:.2f}") 