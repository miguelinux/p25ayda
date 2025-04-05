#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: Radix Sort
"""

from random import randint
from time import time_ns as tiempo


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Lista de salida
    count = [0] * 10  # Para contar los dígitos (0-9)

    # Contar ocurrencias del dígito actual
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convertir count[i] en la posición real de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el array ordenado según el dígito actual
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el array ordenado a arr[]
    for i in range(n):
        arr[i] = output[i]


def radix_sort(lista):
    lista_ordenada = lista  # Copia para no modificar la original
    max_num = max(lista_ordenada)  # Encontramos el número más grande
    exp = 1  # Empezamos con el dígito menos significativo

    while max_num // exp > 0:
        counting_sort(lista_ordenada, exp)
        exp *= 10  # Pasamos a la siguiente posición decimal

    return lista_ordenada


def main():
    """
    Función principal del programa
    """
    # Lista de 10,000 números aleatorios
    aleatorios = [randint(0, 10000) for _ in range(10000)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = tiempo()
    ordenados = radix_sort(ordenados)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print("Tiempo:", t_final - t_inicio, "ns")


if __name__ == "__main__":
    main()
