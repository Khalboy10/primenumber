from allPrime import allPrimes as ap
def factors(num):
    pFactors = []
    myPrime = ap(num)
    for i in myPrime:
        if num % i == 0:
            pFactors.append(i)
    return pFactors

print(factors(20))