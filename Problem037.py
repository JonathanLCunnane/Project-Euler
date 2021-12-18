# loop through all numbers and check if they are truncatable, 
# by checking if each of their truncatable variations are primes.
from time import perf_counter
from euler_library import Primes
def find_truncated(num_str):
    return [int(num_str[-x:]) for x in range(1, len(num_str))] + [int(num_str[:x]) for x in range(1, len(num_str)+1)]
start = perf_counter()
truncated_prime_sum = 0
for num in range(8,1000000):
    str_num = str(num)
    for truncated in find_truncated(str_num):
        if not Primes.is_prime(truncated):
            break
    else:
        truncated_prime_sum += num
print(f"'The truncated prime sum up to 1million is: {truncated_prime_sum}, and this took {(((perf_counter() - start)*100000)//1)/100}ms")