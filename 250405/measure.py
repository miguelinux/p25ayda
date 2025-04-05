from random import randint
from time import time as tiempo

from heap_sort import heap_sort
from merge_sort import merge_sort
from radix_sort import radix_sort
from random_sort import random_sort
from selection_sort import sort_selection


QTY = 1_000_000
Sub_sets = [100, 1_000, 10_000, 100_000, 1_000_000]

results = []
# algorithms=[CocktailSort,insercion,bubble_sort]
algorithms = [sort_selection, merge_sort, heap_sort, radix_sort, random_sort]


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
