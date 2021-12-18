from time import perf_counter
from euler_library import Combinatorics
total = 0
for n in range(1,101):
    for r in range(1, 101):
        comb = Combinatorics.nCr(n, r)
        if not comb:
            continue
        if comb > 1000000:
            total += 1
print(total)