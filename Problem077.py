from time import perf_counter
from euler_library import Primes

# Firstly, initialise an array representing the ways to make 'index' with primes, and a primes array
start = perf_counter()
upto = 100 # an arbitrary limit
target = 5000
ways = [0] * (upto + 1)
ways[0] = 1 # set some known values for iteration
primes = Primes.fetch_primes(upto)
# then for each index > 1, we add the ways of making the number from each number below it as follows.
for prime in primes:
    for index in range(prime, upto + 1):
        ways[index] += ways[index-prime]
for way in ways:
    if way > target:
        end = perf_counter()
        elapsed_ms = (((end - start)*100000)//1)/100
        print(f"The number of ways to sum {ways.index(way)} is {way}, which is greater than {target}.\nThis took {elapsed_ms}ms.")
        break