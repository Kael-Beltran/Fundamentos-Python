def contagem_regressiva():
    valor_contagem = int(input("Digite um número maior que 10: "))
    if valor_contagem < 10:
        print("Valor inválido!!")
    else:
        while valor_contagem >= 1:
            print(f"Contagem regressiva: {valor_contagem}")
            valor_contagem -= 1
        print("DECOLANDO!!!")

contagem_regressiva()