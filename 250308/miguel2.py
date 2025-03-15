#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Ejemplo de un modulo
"""

import miguel


def main():
    """
    Comentario de la función
    """
    numero = int(input("Ingresa un número: "))

    resultado = miguel.factorial(numero)

    print("El factorial es", resultado)


if __name__ == "__main__":
    main()
