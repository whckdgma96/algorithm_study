def factorial(n):
    #factorial(N) = N * factorial(N-1)
    if n ==1:
        return 1
    return n * factorial(n-1)


print(factorial(5))