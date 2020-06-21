"""Python implementation of a naive prime numbers calculation algorithm.

On my system (a Thinkpad X250 with an Intel i5-5300U CPU)
it takes ~3000ms to compute 10000 prime numbers.
"""


def primes(num_primes):
    """Compute the first `num_primes` prime numbers."""
    primes = [2, 3]

    for i in range(2, num_primes):
        n = primes[-1] + 2
        while True:
            if all(n % p for p in primes):
                primes.append(n)
                break
            n += 2

    return primes
