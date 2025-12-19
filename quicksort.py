def quicksort(lista):
    # Caso base: se a lista tiver 1 ou 0 elementos, já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Escolhemos o elemento do meio como pivô
    pivo = lista[len(lista) // 2]
    
    # Criamos 3 sub-listas
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]
    
    # Chamamos a função novamente (recursão) e juntamos os resultados
    return quicksort(esquerda) + meio + quicksort(direita)

numeros = [10, 80, 30, 90, 40, 50, 70, 60, 20, 100, 30, 40, 80]
print(quicksort(numeros))
# Saída: [10, 20, 30, 30, 40, 40, 50, 60, 70, 80, 80, 90, 100]