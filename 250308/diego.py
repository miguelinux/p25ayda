def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Ejemplo de uso
num = 5
print(f"Factorial de {num} es {factorial_recursive(num)}")
