#!/usr/bin/env python3

import ast
import csv
import os
import sys
import time
from collections import defaultdict
from random import randint

# Agregando directorio 250322 que esta una carpeta fuera del directorio que contiene este archivo (250405)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
algo_dir = os.path.join(parent_dir, "250322")
sys.path.append(algo_dir)


# Agregando directorio relativo
# sys.path.append("../p0322")


def func_alg_imported(codigo_fuente):
    tree = ast.parse(codigo_fuente)
    funciones_importadas = defaultdict(int)

    # Solo requiero tener el nombre de la funcion de ordenamiento... el valor lo modificare con el tiempo que tardo en ejecutar
    for nodo in ast.walk(tree):
        if isinstance(nodo, ast.ImportFrom):  # from módulo import función
            for alias in nodo.names:
                funciones_importadas[alias.name] += 0
        elif isinstance(nodo, ast.Import):  # import módulo
            for alias in nodo.names:
                funciones_importadas[alias.name] += 0

    return dict(funciones_importadas)


def main():
    # Importando los algoritmos de ordenamientos
    codigo = """
from heap_sort import heap_sort
from merge_sort import merge_sort
from radix_sort import radix_sort
from selection_sort_2 import selection_sort
from insercion import insercion
from Burbuja import bubble_sort
from cocktail import CocktailSort
	"""

    dic_alg = func_alg_imported(codigo)
    dic_meas = {}

    # Diferentes tipos de pruebas
    tests = [100, 1000, 10000, 100000, 1000000]
    # tests = [10,100]

    for QTY in tests:
        aleatorios = [randint(0, QTY) for _ in range(QTY)]
        ordenados = aleatorios.copy()

        for alg in dic_alg.keys():
            print("iniciando algoritmo: ", alg, " Numero de elementos: ", QTY)

            t_inicio = time.perf_counter()
            eval(alg + "(ordenados)")
            t_final = time.perf_counter()

            elapsed = t_final - t_inicio
            tiempo = f"{elapsed:.6f}"

            print(
                "finalizacion algoritmo: ",
                alg,
                "con ",
                QTY,
                " elementos en ",
                tiempo,
                " segundos",
            )

            dic_alg[alg] = tiempo

        dic_meas[QTY] = dic_alg.copy()

    with open("DiegoJesusGomezCortes_tiempos.csv", "w", newline="") as f:
        campos = ["Algoritmo"] + list(
            next(iter(dic_meas.values())).keys()
        )  # ['nombre', 'edad', 'ciudad']
        escritor = csv.DictWriter(f, fieldnames=campos)

        escritor.writeheader()

        for nombre, info in dic_meas.items():
            fila = {"Algoritmo": nombre}
            fila.update(info)
            escritor.writerow(fila)


if __name__ == "__main__":
    main()
