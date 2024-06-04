def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            arr[k] = L[i] if L[i] < R[j] else R[j]
            i += (arr[k] == L[i])
            j += (arr[k] == R[j])
            k += 1

        arr[k:] = L[i:] if i < len(L) else R[j:]

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Arreglo ordenado:", arr)
