def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

minha_lista = [64, 25, 12, 22, 11, 90, 34, 78, 56, 43, 89, 10, 5, 3, 1, 99, 100, 67, 88, 77, 45, 23, 15, 8, 6]
print(ordenacaoPorSelecao(minha_lista))  # Output: [11, 12, 22, 25, 64, 90, ...]
