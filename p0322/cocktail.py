#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: CocktailSort
"""

from random import randint
from time import time as tiempo

# from time import time_ns as tiempo


def CocktailSort(lista):
    lista_ordenada = lista
    change = True
    start = 0
    end = len(lista_ordenada) - 1
    while change:  # Start shacking!
        change = False
        # Forward pass, highest number at the end
        for idx in range(start, end):
            if lista_ordenada[idx] > lista_ordenada[idx + 1]:
                lista_ordenada[idx], lista_ordenada[idx + 1] = (
                    lista_ordenada[idx + 1],
                    lista_ordenada[idx],
                )
                change = True

        if not change:
            break

        # Backward pass, lowest number at the begining
        for idx in range(end - 1, start - 1, -1):
            if lista_ordenada[idx] > lista_ordenada[idx + 1]:
                lista_ordenada[idx], lista_ordenada[idx + 1] = (
                    lista_ordenada[idx + 1],
                    lista_ordenada[idx],
                )
                change = True

        # Lower number already in place, save some time
        start += 1

    return lista_ordenada


def main():
    """
    Función principal del programa
    """
    # 10000
    QTY = 10000
    aleatorios = [randint(0, QTY) for _ in range(QTY)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = tiempo()
    ordenados = CocktailSort(ordenados)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print(f"Tiempo: {(t_final - t_inicio)} s")


if __name__ == "__main__":
    main()
