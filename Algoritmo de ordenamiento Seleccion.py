def ordenamiento_seleccion(lista):
    
    n = len(lista)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

mi_lista = [64, 25, 12, 22, 11]
ordenamiento_seleccion(mi_lista)
print("Lista ordenada:")
print(mi_lista)
