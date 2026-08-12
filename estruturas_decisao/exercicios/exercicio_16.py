def login():
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "1234"
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        print("Login realizado com sucesso")
    elif usuario == USUARIO_CORRETO:
        print("Senha incorreta")
    else:
        print("Usuário não encontrado")

login()