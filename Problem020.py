from math import factorial
from time import perf_counter
start = perf_counter()
sum = 0
for digit in str(factorial(100)):
    sum += int(digit)
print(f"Total sum of 100! is: {sum}")
print((perf_counter()-start)*1000)
