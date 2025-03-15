def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para calcular su factorial: "))

# Calcular el factorial
resultado = factorial(numero)

# Mostrar el resultado
print(f"El factorial de {numero} es {resultado}")