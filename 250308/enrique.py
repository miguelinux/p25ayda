def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Solicitar al usuario un número
numero = int(input("Introduce un número: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
