#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: RADIX SORT

El algoritmo de ordenamiento radix sort es un algoritmo de ordenamiento que ordena
los elementos de una lista de acuerdo a su representación en base a un dígito específico.
"""

from random import randint
from time import time_ns as tiempo


def counting_sort(lista, exp):
    """
    Función para ordenar numeros mediante un digito especifico (Requerida para radix_sort)
    """
    n = len(lista)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = lista[i] // exp % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        num = lista[i]
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1

    for i in range(n):
        lista[i] = output[i]


def radix_sort(lista):
    """
    Función para ordenar una lista de numeros mediante el algoritmo de radix sort

    """
    if not lista:
        return []
    lista_ordenada = lista.copy()
    max_num = max(lista_ordenada)
    exp = 1
    while max_num // exp > 0:
        counting_sort(lista_ordenada, exp)
        exp *= 10
    return lista_ordenada


def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(1000)]  # nosec B311

    t_inicio = tiempo()
    ordenados = radix_sort(aleatorios)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print("Tiempo:", t_final - t_inicio)


if __name__ == "__main__":
    main()
