from time import perf_counter
from euler_library import Factors
start = perf_counter()
num = 647
count = 0
first = 0
while count != 4:
    distinct = len(Factors.prime_factors(num, [], True))
    if distinct < 4:
        num += 1
        count = 0
        continue
    elif distinct == 4:
        if count == 0:
            first = num
        else:
            pass
        count += 1
        num += 1
        continue
    num += 1
    count = 0  
print(f"The first of four consecutive integers to have four distinct prime factors is {first}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")