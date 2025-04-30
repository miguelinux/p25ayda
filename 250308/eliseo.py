
numero = int(input("Ingresa un número: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")
