def fibonacci(n):
    # Base case
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage:
if __name__ == "__main__":
    n = 10
    fib_sequence = [fibonacci(i) for i in range(n)]
    print(fib_sequence)
