# Operador and e or

def show_veigh():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade? "))
    nome_esta_na_lista =bool(input("Qual a nome da lista? "))

    posso_entrar = (POSSUI_INGRESSO or POSSUI_INGRESSO) and idade > 18

    print(f"Vou conseguir entar no show? {posso_entrar}")

show_veigh()