from prime import prime
def allPrimes(num):
    primes = []
    for i in range(1, num+1):
        if prime(i) is True:
            primes.append(i)
    return primes

#print(allPrimes(20))
