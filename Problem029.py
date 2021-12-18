# this is brute forced
from time import perf_counter
distinct = {4}
start = perf_counter()
for a in range(2, 101):
    for b in range(2,101):
        distinct.add(a**b)
print(f"Number of distinct terms is: {len(distinct)}, and took {(((perf_counter() - start)*100000)//1)/100}ms")