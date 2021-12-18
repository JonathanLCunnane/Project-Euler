from euler_library import Primes
from time import perf_counter
primes = Primes.fetch_primes(3950, False) # this sums to just above 1mil
start = perf_counter()
while sum(primes) > 1000000:
    primes.pop()
num = None
for prime in primes:
    summed = sum(primes)
    if Primes.is_prime(summed):
        num = summed
        break
    primes = primes[1:]
print(f"The prime below one million that is written with the most consecutive primes is: {num}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")