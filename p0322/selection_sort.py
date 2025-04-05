def sort_selection(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [64, 25, 12, 22, 11]
print("El arreglo original es:", arr)
sort_selection(arr)
print("El arreglo ordenado es:", arr)
