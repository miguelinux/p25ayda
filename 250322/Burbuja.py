#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

from random import randint
from time import time_ns as tiempo


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so no need to check them
        swapped = False

        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, then the array is already sorted
        if not swapped:
            break

    return arr


def main():
    """
    Función principal del programa
    """
    # 10000
    QTY = 10000
    aleatorios = [randint(0, QTY) for _ in range(QTY)]  # nosec B311

    t_inicio = tiempo()
    ordenados = bubble_sort(aleatorios.copy())
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print(f"Tiempo: {(t_final - t_inicio)} s")


if __name__ == "__main__":
    main()
