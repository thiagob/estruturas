def prime_numbers(limit):
    primes = []
    for n in range(limit):
        if n > 1:
            prime = True
            for i in primes:
                if n % i == 0:
                    prime = False
                    break
            if prime:
                primes.append(n)
    return primes


pn = prime_numbers(100)
print(pn)
print(len(pn))
