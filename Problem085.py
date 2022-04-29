from time import perf_counter
from math import comb
from sys import maxsize


closest = 0
smallest_diff = maxsize
start = perf_counter()
for n in range(2, 2001):
    for m in range(2, 2001):
        curr = (comb(n+1, 2) * comb(m+1, 2))
        if curr > 2500000:
            break
        curr_diff = abs(2000000 - curr)
        if curr_diff < smallest_diff:
            closest = n*m
            smallest_diff = curr_diff
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The grid area of the grid which has the number of rectangles closest to 2000000 is {closest}.\nThis took {elapsed_ms}ms")
        