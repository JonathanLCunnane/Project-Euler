from time import perf_counter
def proper_divisors_sum(num):
    #if num = 1, return 0
    if num == 1:
        return 0
    #there is always a divisor of 1
    divisor_sum = 1
    #if a square number, firstly add the sqrt to the divisor sum
    sqrt = (num**(1/2))
    if sqrt % 1 == 0:
        divisor_sum += sqrt
    #check up to sqrt of num, adding two for each factor pair
    for divisor in range(2, int(sqrt)):
        result = num / divisor
        if result % 1 == 0:
            divisor_sum += divisor
            divisor_sum += result
    return divisor_sum

start = perf_counter()
upto = 10000
ignore = []
amicable_sum = 0
for current in range(4, upto + 1):
    if current in ignore:
        continue
    current_divisor_sum = proper_divisors_sum(current)
    current_double_divisor_sum = proper_divisors_sum(proper_divisors_sum(current))
    if current == current_double_divisor_sum and current != current_divisor_sum:
        print(current, current_divisor_sum)
        ignore.append(current_divisor_sum)
        amicable_sum += current
        amicable_sum += current_divisor_sum
print(f"The sum is: {amicable_sum}, with time of: {(perf_counter()-start)*1000}ms")