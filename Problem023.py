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
        divisor_check_range = range(2, int(sqrt))
    else:
        divisor_check_range = range(2, int(sqrt) + 1)
    #check up to sqrt of num, adding two for each factor pair
    for divisor in divisor_check_range:
        result = num / divisor
        if result % 1 == 0:
            divisor_sum += divisor
            divisor_sum += result
    return divisor_sum
upper_limit = 28123
upper_range = upper_limit - 10
#find all abundant numbers under upper_limit
start = perf_counter()
abundant = []
for num in range(1, upper_range):
    if proper_divisors_sum(num) > num:
        abundant.append(num)
print(f"Abundant list created with time of: {(((perf_counter() - start)*100000)//1)/100}ms")
#change abundant array to set, since lookup times are much better in sets
abundant = set(abundant)
#find sums of abundant nums underneath 28124
sum_of_abundant_sums = 0
range = set(range(1, upper_limit + 1))
for index, num in enumerate(abundant):
    for adding in abundant:
        temp_sum = num + adding
        if temp_sum <= upper_limit and temp_sum in range:
            range.remove(temp_sum)
# therefore the sum of all numbers not able to created with abundant numbers is the sum of the numbers left in range
print(f"Sum of non-abundant sums is: {sum(range)} with time of: {(((perf_counter() - start)*100000)//1)/100}ms")