def idade():
    ano = int(input("Digite o ano de nascimento: "))
    mes = int(input("Em que mês você nasceu; "))
    dia = int(input("Digite o dia em que nasceu: "))
    dia_atual = 11
    mes_atual = 8
    ano_atual = 2026

    calculo_dia = dia_atual - dia
    calculo_mes = mes_atual - mes
    calculo_ano = ano_atual - ano
    return calculo_ano, calculo_mes, calculo_dia

anos,mes,dias = idade()
print(f"Você nasceu aproximadamente a {anos} anos, {mes} messes, {dias} dias atás.")