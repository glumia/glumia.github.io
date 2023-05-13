/* C implementation of a naive prime numbers calculation algorithm.

   On my system (a Thinkpad X250 with an Intel i5-5300U CPU)
   it takes ~185ms to compute 10000 prime numbers.
 */

#include <stdio.h>

int main() {
  unsigned int i, j, is_prime, n;
  unsigned int NUM_PRIMES = 10000;
  unsigned int primes[NUM_PRIMES];

  primes[0] = 2;
  primes[1] = 3;

  for (i = 2; i < NUM_PRIMES; i++) {
    n = primes[i - 1] + 2;

    while (1) {
      is_prime = 1;
      for (j = 0; j < i; j++) {
        if (!(n % primes[j])) {
          is_prime = 0;
          break;
        }
      }
      if (is_prime) {
        primes[i] = n;
        break;
      }
      n += 2;
    }
  }

  printf("%d\n", primes[i - 1]);
}
