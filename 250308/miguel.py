def factorial(n):
    """Calcula el factorial de un número entero no negativo.

    Args:
      n: El número entero no negativo.

    Returns:
      El factorial de n, o 1 si n es 0.
    """

    if n < 0:
        return "El factorial no está definido para números negativos"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


# Ejemplo de uso
numero = 5
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es {resultado_factorial}")
