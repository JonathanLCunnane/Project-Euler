from time import perf_counter
from euler_library import Primes


# we will check from spiral size three to until we find the 10% of diagonals being primes.
# We will calculate the percentage of diagonals that are
# prime. For a side length of n, the bottom right is n^2, the bottom left is n^2 - (n - 1), the
# top left is n^2 - 2(n - 1), and the top right is n^2 - 3(n - 1). So we simply check if these
# are prime, and find the percentage overall that are prime by summation.


start = perf_counter()
max_side_length = 30000
diag_total = 1
diag_primes = 0
side_len = 0
for n in range(3, max_side_length+1, 2):
    diag_total += 4
    squared = n**2
    summary = n - 1
    if Primes.is_prime(squared - summary):
        diag_primes += 1
    if Primes.is_prime(squared - 2*summary):
        diag_primes += 1
    if Primes.is_prime(squared - 3*summary):
        diag_primes += 1
    if diag_primes/diag_total < 0.1:
        side_len = n
        end = (((perf_counter() - start)*100000)//1)/100
        break
print(f"The side length at which the ratio of primes along the diagonals is less than 10% is {side_len}.\nThis took {end}ms")