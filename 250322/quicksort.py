#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: Quicksort
"""

import time
from random import randint


def quicksort(lista):
    # Hacemos una copia para no modificar la lista original
    lista = lista.copy()

    # Caso base: listas vacías o con un elemento ya están ordenadas
    if len(lista) <= 1:
        return lista

    # Elegimos un pivote (en este caso usamos el último elemento)
    pivote = lista[-1]

    # Dividimos la lista en tres partes
    menores = [x for x in lista[:-1] if x <= pivote]
    mayores = [x for x in lista[:-1] if x > pivote]

    # Ordenamos recursivamente y combinamos
    return quicksort(menores) + [pivote] + quicksort(mayores)


def main():
    """
    Función principal del programa
    """

    # 10000
    QTY = 10000
    aleatorios = [randint(0, QTY) for _ in range(QTY)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = time.perf_counter()
    ordenados = quicksort(ordenados)
    t_final = time.perf_counter()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    elapsed = t_final - t_inicio
    print(f"Tiempo transcurrido: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
