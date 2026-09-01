def quantidade_elementos(lista):
    for nome in lista:
        print(f"O nome da lista é: {nome}")
    return len(lista)

lista_de_frutas = ["Maçã", "Banana", "Laranja", "Uva", "Manga", "Morango"]

quantidade_elementos(lista_de_frutas)