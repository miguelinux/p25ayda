import random
import time


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Generar 15 números aleatorios entre 0 y 1000
numeros_aleatorios = [random.randint(0, 1000) for _ in range(15)]  # nosec B311

# Medir tiempo de ejecución
inicio = time.time()

# Ordenar los números
numeros_ordenados = quicksort(numeros_aleatorios)

fin = time.time()
tiempo_ejecucion = fin - inicio

# Imprimir resultados
print("Números aleatorios generados:")
print(numeros_aleatorios)
print("\nNúmeros ordenados con Quicksort:")
print(numeros_ordenados)
print(f"\nTiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
