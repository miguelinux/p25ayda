#!/usr/bin/env python3

from random import randint
from time import time_ns as tiempo


def is_sorted(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista


def main():
    aleatorios = [randint(0, 10000) for _ in range(11)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = tiempo()
    ordenados = selection_sort(ordenados)
    t_final = tiempo()

    print("Aleatorios:", aleatorios)
    print("Ordenados:", ordenados)

    tiempo_transcurrido = (t_final - t_inicio) / 1e9

    minutos = int(tiempo_transcurrido // 60)
    segundos = tiempo_transcurrido % 60

    print(f"Tiempo: {minutos}:{segundos:.2f}")


if __name__ == "__main__":
    main()
