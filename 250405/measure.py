import os
import sys
from random import randint
from time import time as tiempo

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)

# Usando path absoluto
algo_dir = os.path.join(parent_dir, "250322")

# Usando path relativo
# algo_dir = os.path.join("..","250322")

# Add the parent directory to sys.path
sys.path.append(algo_dir)

from heap_sort import heap_sort  # noqa E402
from merge_sort import merge_sort  # noqa E402
from radix_sort import radix_sort  # noqa E402
from random_sort import random_sort  # noqa E402
from selection_sort_2 import selection_sort  # noqa E402


QTY = 1_000_000
Sub_sets = [100, 1_000, 10_000, 100_000, 1_000_000]

results = []
# algorithms=[CocktailSort,insercion,bubble_sort]
algorithms = [selection_sort, merge_sort, heap_sort, radix_sort, random_sort]


if __name__ == "__main__":
    aleatorios = [randint(0, QTY) for _ in range(QTY)]  # nosec B311
    # ordenados = aleatorios.copy()

    for algo in algorithms:
        for set in Sub_sets:
            ordenados = aleatorios.copy()
            num_set = ordenados[0:set]
            if (
                (algo.__name__ == "sort_selection" or algo.__name__ == "radix_sort")
                and set == 1_000_000
            ) or (algo.__name__ == "random_sort" and set > 1001):
                results.append(0.0)
                continue
            t1 = tiempo()
            algo(num_set)
            t2 = tiempo()
            print(f"Set {len(num_set)} fn:{algo.__name__} completed in t:{t2 - t1}")
            results.append(t2 - t1)
            num_set.clear()
            ordenados.clear()
        print("result", results)
        results.clear()
    # print("Starting Measurement")
    # insercion(ordenados[0:100])
    # print(ordenados)
