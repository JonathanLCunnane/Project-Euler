from time import perf_counter
from euler_library import Primes
def follows_conjecture(num):
    if Primes.is_prime(num): return True
    primes_under = Primes.fetch_primes(num)
    for prime in primes_under:
        diff = num - prime
        if diff <= 0:
            print(diff, num)
            return False
        if (diff/2)**0.5 % 1 == 0:
            return True
    return False
n = 33
start = perf_counter()
while True:
    if not follows_conjecture(n):
        print(f"The first number that does not follow Goldbach's other conjecture is {n}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")
        break
    n += 2