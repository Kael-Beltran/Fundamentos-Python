def adicionar_cliente(fila, cliente):
    fila.append(cliente)
    for nome in fila:
        print(f"O nome da lista é: {nome}")
    return fila

def atender_cliente(fila):
    cliente_atendido = fila.pop(0)
    for nome in fila:
        print(f"O nome da lista é: {nome}")
    return cliente_atendido

fila_de_clientes = []

while True:
    nome_cliente = input("Digite o nome do cliente (ou 'sair' para encerrar): ")
    if nome_cliente.lower() == "sair":
        break
    adicionar_cliente(fila_de_clientes, nome_cliente)

if fila_de_clientes:
    atender_cliente(fila_de_clientes)