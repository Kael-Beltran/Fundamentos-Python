def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")

lista_de_nomes = ["Kael", "Murillo", "Manoel", "Gasque", "Eduardo"]
mostrar_nomes(lista_de_nomes)

# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nome(lista_de_nomes, 'Isabela')

# Adicionando novo nome em uma posição específica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lista: {nomes}")

adicionar_nome_posicao(lista_de_nomes, 'Beltrão', 2)

# Juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista {nomes}")

novos_nome = ["Nicolas", "Ferraz"]
juntar_nomes(lista_de_nomes, novos_nome)

# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido da lista {nomes}")

remover_nome_pelo_valor(lista_de_nomes, "Gasque")

# Removendo nome pelo índice (CORRIGIDO)
def remover_nome_pelo_indice(nomes, posicao):
    if 0 <= posicao < len(nomes):
        removido = nomes.pop(posicao)
        print(f"O nome '{removido}' da posição {posicao} foi removido!")
    else:
        print("Posição inválida!")

remover_nome_pelo_indice(lista_de_nomes, 3)

# Descobrindo a posição (index) pelo nome (CORRIGIDO)
def encontra_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("O nome não está na lista!")
    else:
        posicao = nomes.index(nome)
        print(f"A posição do nome {nome} é {posicao}")

encontra_nome_pelo_valor(lista_de_nomes, "Murillo")

# Contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"A quantidade de nomes da lista é {quantidade}")

quantidade_de_nomes(lista_de_nomes)

# Ordenando os elementos da lista
def ordenar_nome(nomes):
    lista_de_nomes_ordenados = sorted(nomes, reverse=True)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")

ordenar_nome(lista_de_nomes)

# Operações matemáticas - Calcular média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A média das notas é {media}")

notas_semestre = [7, 4, 10, 8]
calcular_media(notas_semestre)

# Gerenciar notas (CORRIGIDO)
def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    notas_ordenadas = sorted(notas)
    media = sum(notas) / len(notas)
    return notas_ordenadas, media

notas_ordenadas, media = gerenciar_notas(notas_semestre, 6.5)
print(f"Notas ordenadas = {notas_ordenadas}")
print(f"A média das notas é {media}")

# Lista de Listas
def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f"Minha lista de produtos: {produtos}")

lista_produtos = [
    ["Arroz", 2, 32.00],
    ["Feijão", 3, 8.50]
]
novo_produto = ["Café", 2, 28.00]
adicionar_produto(lista_produtos, novo_produto)

def quantidade_total_produtos(produtos):
    quantidade = []

    for produto in produtos:
        quantidade.append(produto[1])

    return sum(quantidade)

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f"A quantidade total de produtos {quantidade_produtos}")

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valor = produto[1] * produto[2]
        valores.append(valor)

    return sum(valores)

preco_total_produtos = valor_total_produtos(lista_produtos)
print(f"O valor total de produtos {preco_total_produtos}")