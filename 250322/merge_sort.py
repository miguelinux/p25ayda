#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: Merge Sort
"""

from random import randint
from time import time_ns as tiempo

# from time import time as tiempo

def merge_sort(arr):
    if len(arr) > 1:

        # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Sort the two halves
        merge_sort(sub_array1)
        merge_sort(sub_array2)

        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

    # Until we reach the end of either start or end, pick larger among
    # elements start and end and place them in the correct position in the sorted array
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

    # When all elements are traversed in either arr1 or arr2,
    # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
    return arr

def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(10000)]  # nosec B311

    t_inicio = tiempo()
    ordenados = merge_sort(aleatorios)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print("Tiempo:", t_final - t_inicio)


if __name__ == "__main__":
    main()
