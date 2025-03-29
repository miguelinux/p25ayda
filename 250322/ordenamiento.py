#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un algoritmo de ordenamiento
llamado: <PONER AQUI EL NOMBRE>
"""

from random import randint
from time import time_ns as tiempo

# from time import time as tiempo


def nombre_del_algoritmo(lista):
    lista.sort()
    return lista


def main():
    """
    Función principal del programa
    """
    aleatorios = [randint(0, 10000) for _ in range(10000)]  # nosec B311
    ordenados = aleatorios.copy()

    t_inicio = tiempo()
    ordenados = nombre_del_algoritmo(ordenados)
    t_final = tiempo()

    print("Aleatorios:", aleatorios[0:15])
    print("Ordenados:", ordenados[0:15])
    print("Tiempo:", t_final - t_inicio)


if __name__ == "__main__":
    main()
