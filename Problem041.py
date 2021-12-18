from time import perf_counter
from euler_library import Primes, Combinatorics
start = perf_counter()
max = 0
for num in Combinatorics.permutations("1234567"):
    int_num = int(num)
    if int_num > max:
        if Primes.is_prime(int_num):
            max = int_num
print(f"The largest pandigital is: {max}, taking {(((perf_counter() - start)*100000)//1)/100}ms to find")