from time import perf_counter
from euler_library import Basic


def iteration(iter_num):
    iter_num -= 1
    fraction = 2
    for iter in range(iter_num):
        fraction = 2 + (1/fraction)
    return 1 + (1/fraction)


# the pattern here is that the sum of the numerator and denominator is the denominator of the next iteration. 
# Therefore is we have the first iteration for example: 3/2 = 1.5,
# so we can conclude that the denominator for the next iteration (iter # 2) is 3 + 2 = 5.
# if we calculate its value, 1.4, and multiply by the denominator, we get the numerator.
# then we can compare their lengths

# first set the values given for the eighth expansion
numerator = 1393
denominator = 985
count = 1
upto = 1000
start = perf_counter()
for expansion in range(9, upto+1):
    numerator += 2 * denominator
    denominator = numerator - denominator
    if Basic.int_length(numerator) > Basic.int_length(denominator):
        count += 1
end = (((perf_counter() - start)*100000)//1)/100
print(f"The number of expansions with a numerator with more digits than the denominator in the first {upto} expansions is {count}.\nThis took {end}ms")