#!/usr/bin/env python3

"""
Ejemplo de un algoritmo de ordenamiento
llamado: random-sort
"""

from random import randint
from time import time_ns as tiempo


def isSorted(lista):
    """
    Helper function to check if a list is sorted in ascending order.
    Returns True if sorted, False otherwise.
    """
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def random_sort(lista):
    from random import shuffle

    lista_ordenada = lista

    while not isSorted(lista_ordenada):
        shuffle(lista_ordenada)

    return lista_ordenada


def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(11)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = tiempo()
    ordenados = random_sort(ordenados)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:5])
    print("Ordenados:", ordenados[0:5])

    tiempo_transcurrido = (t_final - t_inicio) / 1e9

    minutos = int(tiempo_transcurrido // 60)
    segundos = tiempo_transcurrido % 60

    print(f"Tiempo: {minutos}:{segundos:.2f}")


if __name__ == "__main__":
    main()
