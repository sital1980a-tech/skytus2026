def fibonacci(n):
    a, b = 0, 1
    fib_series = []

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

N = int(input("Enter N: "))
print(fibonacci(N))
