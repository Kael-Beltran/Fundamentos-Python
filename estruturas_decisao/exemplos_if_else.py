def aluno_aprovado():
    nota_1 = float(input("Qual a sua primeira nota? "))
    nota_2 = float(input("Qual a sua segunda nota? "))

    media = (nota_1 + nota_2) / 2

    if media >= 7:
        print("Você passou de ano! Parabens!")
    elif media >=6 and media <7:
        print("Aluno de recuperação")
    else:
        print("Você reprovou de ano, estude mais!")

aluno_aprovado()


def login():
    e_mail = "kaelandrade1530@gmail.com"
    senha = "1234"
    codigo_secreto = "#456@"

    e_mail_input = input("Qual seu E-mail?")
    senha_input = input("Qual sua Senha?")

    if e_mail_input == e_mail and senha_input == senha:
        print("Pode acessar o seu E-mail")
        acessar_admin = input("Deseja acessar o administrador?(Digite S para sim e N para não)")
        if acessar_admin == "S":
            codigo_secreto = input("Digite o seu codigo:")
            if codigo_secreto == codigo_secreto:
                print("Acesso Admin Liberado")
            else:
                print("Codigo secreto incorreto!")
        elif acessar_admin == "N" :
            print("Ok. Você acessou como úsuario comun!")
        else:
            print("Opção invalida!")
    else:
        print("Email ou senha incorreta!")

login()