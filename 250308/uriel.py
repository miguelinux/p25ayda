# Héctor Uriel Aguilera Peña
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib


if __name__ == "__main__":
    numero_terminos = 20
    serie_fibonacci = fibonacci(numero_terminos)
    print(
        f"Los primeros {numero_terminos} términos de la serie de Fibonacci son: {serie_fibonacci}"
    )
