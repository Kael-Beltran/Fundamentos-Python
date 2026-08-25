def validar_senha():
    e_mail = "aluno123@gmail.com"
    senha = "1234"
    tentativas = 0
    max_tentativas = 3

    while tentativas < max_tentativas:
        e_mail_input = input("Qual seu E-mail? ")
        senha_input = input("Qual sua Senha? ")

        if e_mail_input == e_mail and senha_input == senha:
            print("\nPode acessar o seu E-mail!")
            break
        else:
            tentativas += 1
            restantes = max_tentativas - tentativas

            if restantes > 0:
                print(f"E-mail ou senha incorreta! Você ainda tem {restantes} tentativa(s).\n")
            else:
                print("\nNúmero máximo de tentativas atingido. Acesso bloqueado!")


validar_senha()