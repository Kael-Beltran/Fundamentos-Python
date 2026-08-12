def senha():
    SENHA_CORRETA = "python123"
    login = input("Informe a sua senha para logar no seu email: ")

    if login == SENHA_CORRETA:
        print("Senha valida, pode acessar seu email!")
    else:
        print("Senha invalida!")

senha()