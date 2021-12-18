# We are going to loop through all of the quadratics from n^2 + an + b = 0, where a = -1000, b = -1000, 
# looping through the values from n = 0 to the maximum that it can increase while n^2 + an + b is prime. 
# Firstly, we need a function to check if a number is prime.
from time import perf_counter
def is_prime(num):
    # check up to the sqrt of the number rounded down
    try:
        end = int(num**(1/2))
    except TypeError:
        return False
    for check in range(2, end):
        if num % check == 0:
            return False
    return True
start = perf_counter()
maxa = -999
maxb = 2
max_primes_in_a_row = 0
for a in range(-999, 1000):
    for b in range(2, 1001):
        n = 0
        y = n**2 + a*n + b
        number_of_primes_in_a_row = 0
        while is_prime(y):
            number_of_primes_in_a_row += 1
            n += 1
            y = n**2 + a*n + b
        if number_of_primes_in_a_row > max_primes_in_a_row:
            max_primes_in_a_row = number_of_primes_in_a_row
            maxa = a
            maxb = b
print(f"The maximum number of consecutive primes from n = 0 is from the quadratic: n^2 + {maxa}n + {maxb}, with {max_primes_in_a_row}, and the product of a and b is {maxa*maxb}. This took: {(((perf_counter() - start)*100000)//1)/100}ms")