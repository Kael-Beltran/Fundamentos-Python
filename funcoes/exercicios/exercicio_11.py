def salario():
    horas = float(input("Quanto você ganha por hora? "))
    quantidade = int(input("Quantas horas você trabalha por dia?"))
    dia = horas * quantidade
    return dia

ganho = salario()
print(f"Você ganha {ganho}, por dia!")