def insertion_sort(lista):
    
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_actual

lista = [12, 11, 13, 5, 6]
insertion_sort(lista)
print("Lista ordenada:", lista)
