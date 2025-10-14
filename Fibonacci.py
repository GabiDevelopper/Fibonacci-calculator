def fibonacci(n):
    suite = [0, 1] 
    for i in range(2, n):
        suite.append(suite[i - 1] + suite[i - 2])
    return suite

n = 20
fib = fibonacci(n)

print(f"Les {n} premiers termes de la suite de Fibonacci sont :")
print(fib)
