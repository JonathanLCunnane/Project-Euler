# if the number has 0 or 5 as its last digit, skip it immediately.
# the largest number that could be pandigital is a 4 digit number, 
# i.e. it has to be less than 10000
from time import perf_counter
def generate_concatenated_product(num):
    num_str = str(num)
    out = ""
    for counter in range(1,10):
        length = len(out)
        if length > 9:
            return 0
        if length == 9:
            return int(out)
        out += str(num * counter)
    return int(out)
start = perf_counter()
upto = 10000
largest_pandigital_num = 0
check = {1,2,3,4,5,6,7,8,9}
for num in range(1, upto):
    if num % 5 == 0:
        continue
    generated = generate_concatenated_product(num)
    if generated > largest_pandigital_num and {int(digit) for digit in str(generated)} == check:
        largest_pandigital_num = generated
print(f"The largest pandigital is: {largest_pandigital_num}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")