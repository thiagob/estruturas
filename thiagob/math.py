def fibonacci_r(n):
    if n <= 1:
        return n
    
    return fibonacci_r(n-1) + fibonacci_r(n-2)

def fibonacci_i(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib[n]