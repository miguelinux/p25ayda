import random
import time

def quicksort(arr):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Elegir un pivote (en este caso, el primer elemento)
    pivot = arr[0]

    # Dividir la lista en tres partes:
    # 1. Elementos menores que el pivote
    # 2. Elementos iguales al pivote
    # 3. Elementos mayores que el pivote
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]

    # Aplicar recursivamente Quicksort a las sublistas "less" y "greater"
    return quicksort(less) + equal + quicksort(greater)

# Generar 15 números aleatorios entre 1 y 100
random_numbers = [random.randint(1, 100) for _ in range(15)]

# Imprimir los números generados
print("Números aleatorios:", random_numbers)

# Medir el tiempo de ejecución del Quicksort
start_time = time.time()  # Iniciar el cronómetro
sorted_numbers = quicksort(random_numbers)  # Ordenar los números
end_time = time.time()  # Detener el cronómetro

# Imprimir los números ordenados
print("Números ordenados:", sorted_numbers)

# Imprimir el tiempo de ejecución
execution_time = end_time - start_time
print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
