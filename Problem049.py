from time import perf_counter
from euler_library import Combinatorics, Primes
start = perf_counter()
upto = 9999
primes = Primes.fetch_primes(upto, False)
primes = primes[primes.index(997):]
for prime_one in primes:
    for prime_two in primes[primes.index(prime_one)+1:]:
        prime_three = prime_two * 2 - prime_one
        if prime_three in primes:
            if prime_one != 1487:
                if Combinatorics.is_permutation(str(prime_one), str(prime_two)) and Combinatorics.is_permutation(str(prime_one), str(prime_three)):
                    print(f"The three primes are: {prime_one, prime_two, prime_three}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")