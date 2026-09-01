def adicionar_nota(notas, nova_nota):
    notas.append(nova_nota)
    return notas

def inserir_nota(notas, posicao, nova_nota):
    notas.insert(posicao, nova_nota)
    return notas

def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)
    return notas

def remover_nota(notas, nota_remover):
    if nota_remover in notas:
        notas.remove(nota_remover)
    return notas

def remover_ultima_nota(notas):
    if notas:
        return notas.pop()
    return None

def encontrar_posicao(notas, nota_procurada):
    if nota_procurada in notas:
        return notas.index(nota_procurada)
    return -1

def quantidade_notas(notas):
    return len(notas)

def ordenar_notas(notas):
    return sorted(notas)

def inverter_notas(notas):
    return list(reversed(notas))

def somar_notas(notas):
    return sum(notas)

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

notas = [7.5, 6.0, 8.5, 9.0, 5.5]

print(f"Lista inicial: {notas}\n")

adicionar_nota(notas, 10.0)
print(f"1. Após append(10.0): {notas}")

inserir_nota(notas, 2, 8.0)
print(f"2. Após insert(2, 8.0): {notas}")

adicionar_varias_notas(notas, [6.5, 7.0])
print(f"3. Após extend([6.5, 7.0]): {notas}")

remover_nota(notas, 5.5)
print(f"4. Após remove(5.5): {notas}")

removida = remover_ultima_nota(notas)
print(f"5. Após pop() (removida {removida}): {notas}")

pos = encontrar_posicao(notas, 9.0)
print(f"6. Posição da nota 9.0: {pos}")

qtd = quantidade_notas(notas)
print(f"7. Quantidade total de notas: {qtd}")

notas_ordenadas = ordenar_notas(notas)
print(f"8. Notas ordenadas: {notas_ordenadas}")

notas_invertidas = inverter_notas(notas)
print(f"9. Notas invertidas: {notas_invertidas}")

soma = somar_notas(notas)
print(f"10. Soma das notas: {soma}")

media = calcular_media(notas)
print(f"11. Média da turma: {media:.2f}")