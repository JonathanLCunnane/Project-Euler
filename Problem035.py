from time import perf_counter
from euler_library import Primes
def generate_rotations(num):
    for pos in range(1, len(num)+1):
        yield int(num[pos:] + num[:pos])
start = perf_counter()
upto = 1000000
to_skip = {"0", "2", "4", "5", "6", "8"}
def is_num_to_skip(num):
    for digit in num:
        if digit in to_skip:
            return True
circular = 4 # because 4 one digit circular primes
for num in range(10, upto + 1):
    # if number has 0, 2, 4, 5, 6, 8 in then just continue
    str_num = str(num)
    if is_num_to_skip(str_num): continue
    # loop through all rotations of number
    for rotation in generate_rotations(str_num):
        # if all rotations are prime, prime is circular.
        if not Primes.is_prime(rotation):
            break
    else:
        circular += 1
print(f"The number of circular primes under {upto} is {circular}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")