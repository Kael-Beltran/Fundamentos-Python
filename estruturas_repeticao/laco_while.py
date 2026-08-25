def mostrar_numero_while():
    contador = 0
    while contador <= 10:
        contador += 1
        print(f"Numero do conatdaor agora é: {contador}")

# mostrar_numero_while()

def contagem_regressiva():
    valor_contagem = int(input("Digite um número maior que 10: "))
    if valor_contagem < 10:
        print("Valor inválido!!")
    else:
        while valor_contagem >= 1:
            print(f"Contagem regressiva: {valor_contagem}")
            valor_contagem -= 1
        print("DECOLANDO!!!")

# contagem_regressiva()

def soma_com_while():

    while True:
        num_1 = int(input("Digite o primeiro valor: "))
        num_2 = int(input("Digite o segundo valor: "))

        if num_1 == 0:
            print(f"Função da soma encerrada!")
            break
        else:

        num_2 == 0:
        soma = num_1 + num_2
        print(f"O resultado da soma é {soma}")

soma_com_while()