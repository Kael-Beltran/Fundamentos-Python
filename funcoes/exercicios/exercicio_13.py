def salario():
    salario = float(input("Digite o seu sálario: "))
    vendas = float(input("Digite o valor do produto: "))
    porcetagem = float(input("Digite o porcentual da sua comissão: "))
    extra = (vendas * porcetagem) / 100
    salario_final = salario + extra
    return salario, salario_final

salario, salario_final = salario()
print(f"O seu salario inicial é {salario}, com o valor das vendas ele ficou por {salario_final}")