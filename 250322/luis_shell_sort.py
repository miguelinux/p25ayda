#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: <Shell sort>
"""

from random import randint
from time import time_ns as tiempo

# from time import time as tiempo


def shell_sort(arr):
  """
  Ordena una lista usando el algoritmo Shell Sort.

  Args:
    arr: La lista a ordenar.
  """
  n = len(arr)
  gap = n // 2  # Inicializa el gap (intervalo)

  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
    gap //= 2  # Reduce el gap para la siguiente iteración

def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(10000)]  # nosec B311

    t_inicio = tiempo()
    ordenados =shell_sort(aleatorios)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print("Tiempo:", t_final - t_inicio)


if __name__ == "__main__":
    main()
