#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: Heap sort
"""

from random import randint
from time import time_ns as tiempo

# from time import time as tiempo


# funcion heapify que tranforma el arreglo en un HEAP (Arbol binario cuyo nodo padre es mayor a sus dos nodos hijos)
def heapify(lista, n, i):
    mayor = i
    izquierdo = 2 * i + 1  # Índice del hijo izquierdo
    derecho = 2 * i + 2  # Índice del hijo derecho

    # Si el hijo izquierdo es mayor que el nodo padre
    if izquierdo < n and lista[izquierdo] > lista[mayor]:
        mayor = izquierdo

    # Si el hijo derecho es mayor que el nodo más grande encontrado hasta ahora
    if derecho < n and lista[derecho] > lista[mayor]:
        mayor = derecho

    # Si el nodo más grande no es la raíz
    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]  # Intercambiar
        heapify(lista, n, mayor)  # Aplicar heapify recursivamente


def heap_sort(lista):
    lista_ordenada = lista

    n = len(lista_ordenada)

    # reorganizar el arreglo en un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista_ordenada, n, i)

    # Extraer elementos del Heap uno por uno
    for i in range(n - 1, 0, -1):
        lista_ordenada[i], lista_ordenada[0] = (
            lista_ordenada[0],
            lista_ordenada[i],
        )  # Mover la raíz al final
        heapify(lista_ordenada, i, 0)  # Restaurar la propiedad del Heap

    return lista_ordenada


def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(10000)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = tiempo()
    ordenados = heap_sort(ordenados)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print("Tiempo:", t_final - t_inicio)


if __name__ == "__main__":
    main()
