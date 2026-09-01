def adicionar_nota(notas, nota):
    notas.append(nota)
    for nome in notas:
        print(f"O nome da lista é: {nome}")
    return notas

def remover_nota(notas, nota):
    notas.remove(nota)
    for nome in notas:
        print(f"O nome da lista é: {nome}")
    return notas

def media_notas(notas):
    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade
    for nome in notas:
        print(f"O nome da lista é: {nome}")
    return media

lista_de_notas = [7.5, 8.0, 6.5, 9.0]

adicionar_nota(lista_de_notas, 10.0)
remover_nota(lista_de_notas, 6.5)
media_notas(lista_de_notas)