# Operador and

def pode_dirrigir():
    idade = int(input("Digite sua idade: "))
    TEM_HABILITACAO = True

    autorizado = idade >= 18 and TEM_HABILITACAO

    print(f"O Úsuario pode dirigir? {autorizado}")

pode_dirrigir()