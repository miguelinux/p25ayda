#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: Insercio
"""

import time
from random import randint


def insercion(lista):
    lista2 = lista
    for i in range(1, len(lista2)):
        item = lista2[i]
        j = i - 1
        while j >= 0 and item < lista2[j]:
            lista2[j + 1] = lista2[j]
            j -= 1
        lista2[j + 1] = item
    return lista2


def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(10000)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = time.perf_counter()
    ordenados = insercion(ordenados)
    t_final = time.perf_counter()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    elapsed = t_final - t_inicio
    print(f"Tiempo transcurrido: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
