def jogo_adivinhacao():
    print("--- Jogo da Adivinhação ---")
    tentativas = 0

    while True:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número secreto é MAIOR. Tente novamente!\n")
        elif palpite > numero_secreto:
            print("O número secreto é MENOR. Tente novamente!\n")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
            break

jogo_adivinhacao(42)