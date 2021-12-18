# we only need to check up to 8 digit numbers since the maximum that an 8 digit number 
# can produce in terms of its factorial sum of digits is 8 * 9!, which is 2,903,040
# a 7 digit number. A brute force approach is taken
from time import perf_counter
start = perf_counter()
def factorial(num):
    factorial = 1
    for digit in range(2, num + 1):
        factorial *= digit
    return factorial
def is_curious_number(num):
    sum = 0
    for digit in str(num):
        sum += factorial(int(digit))
    return (sum == num)
for num in range(10, 100000000):
    if is_curious_number(num):
        print(f"A new curious number found! It is: {num}, taking {(((perf_counter() - start)*100000)//1)/100}ms")
print(f"Finished with {(((perf_counter() - start)*100000)//1)/100}ms of time.")