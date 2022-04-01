from time import perf_counter


def max_r(a: int):
    squared = a**2
    max_r = -1
    n = 1
    curr_remainder = (2*a) % squared
    while True:
        if curr_remainder == max_r:
            return max_r
        if curr_remainder > max_r:
            max_r = curr_remainder
        n += 1
        curr_remainder = ((a-1)**n + (a+1)**n) % squared


start = perf_counter()
upto = 1000
sum = 0
for num in range(3, upto+1):
    sum += max_r(num)
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The sum of r_max for 3 <= a <= {upto} is {sum}.\n This took {elapsed_ms}ms")