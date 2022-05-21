from time import perf_counter

from numpy import square


def square_sum(num: int):
    sum = 0
    while num > 0:
        curr = num % 10
        num = num // 10
        sum += curr**2
    return sum


def goes_to_eighty_nine(num: int):
    if num == 89:
        return True
    if num == 1:
        return False
    return goes_to_eighty_nine(square_sum(num))


start = perf_counter()

count = 0
# first create a dict of the first 567 numbers which has key: num, value: bool (True if goes to 89, False if goes to 1)
number_dict = {}
for n in range(1, 568):
    if goes_to_eighty_nine(n):
        count += 1
        number_dict[n] = True
    else:
        number_dict[n] = False

# then loop through the remaining numbers, checking for a value in the number_dict each time
for n in range(568, 10000000):
    curr_sum = square_sum(n)
    if number_dict[curr_sum]:
        count += 1

end = perf_counter()
elapsed_ms = (((perf_counter() - start)*100000)//1)/100
print(f"The number of numbers under 10,000,000 whose square digit chains reach 89 is {count}.\nThis took {elapsed_ms}ms.")