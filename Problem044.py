from time import perf_counter
from sys import maxsize
def is_pentagonal(num):
    disc = 1+24*num
    if disc < 0:
        return False
    if ((1+disc**0.5)/6)%1 == 0:
        return True
    return False
def generate_pentagonal(upto):
    pentagonal_arr = []
    for n in range(1, upto+1):
        pentagonal_arr.append(n*(3*n-1)/2)
    return pentagonal_arr
start = perf_counter()
arr = generate_pentagonal(20000)
d = maxsize
for num in arr:
    for compare in arr:
        if compare == num:
            continue
        if is_pentagonal(num-compare):
            if is_pentagonal(num+compare):
                smallest = min(abs(num-compare), abs(compare-num))
                if smallest < d:
                    d = smallest
print(f"The value when D is minimised is {d}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")