import math


def is_prime(m):
    n = math.floor(math.sqrt(m)) + 1
    for i in range(2, n):
        if(m % i == 0):
            return False
    return True


def primes(n):
    return [i for i in range[2, n] if is_prime(i)]
