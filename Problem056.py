from time import perf_counter


def digital_sum(num):
    return sum([int(digit) for digit in str(num)])


start = perf_counter()
a = 1
b = 1
max = 0
max_num = 0
upto = 100
for a in range(1,upto+1):
    for b in range(1,upto+1):
        power = a**b
        sum_of_digits = digital_sum(power)
        if sum_of_digits > max:
            max = sum_of_digits
            max_num = power
end = (((perf_counter() - start)*100000)//1)/100
print(f"The maximum digital sum of a^b where a, b < {upto} is {max} of the number {max_num}.\nThis took {end}ms")