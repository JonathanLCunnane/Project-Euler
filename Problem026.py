from time import perf_counter
# all recurring decimals can be written in the form 
# of x / 10^k - 1 i.e. some number divided by another 
# with only 9s in it. Also, logically, all of the 
# numbers which re not prime will have the same number 
# of recurring decimal places as the prime which they 
# are a multiple of, so we only need to check the reciprocals
# of the primes from 1 - 1000. Therefore, firstly we will find 
# the primes from 1 - 1000. (A sieve type method will be used)
upto = 1000
primes = list(range(2,upto))
start = perf_counter()
# the following filters out all numbers and then the last value if it is not prime
for index, num in enumerate(primes):
    if num == 0:
        continue
    for multiple_index in range(num*2-1, upto-num, num):
        primes[multiple_index - 1] = 0
for divisor in range(1, (int(primes[-1]**(1/2)) + 1)):
    if primes[-1] % divisor == 0:
        primes.remove(primes[-1])
        break
# ommit zeros from the array
for zero in range(primes.count(0)): primes.remove(0)
print(f"Primes generated in: {(((perf_counter() - start)*100000)//1)/100}ms")
# As every reciprocal of a prime creates a recurring decimal (apart from 2 and 5)
# which will be ommitted, and each recurring decimal can be represented by x / 10^k - 1
# we will loop through 9s until that number of 9s divided by the prime is a whole number.
# The number of 9s used to get the whole number will be the length of the recurring decimal,
# e.g. 1/7 = 142857/999999, therefore 999999/7 = 142857, and 1/7 = 0.142857142857...
primes.remove(2)
primes.remove(5)
highest_reccurance = 0
highest_reccurance_prime = 0
for prime in primes:
    nines = 9
    while (nines % prime != 0):
        nines = int(str(nines)+"9")
    nines = len(str(nines))
    if nines > highest_reccurance:
        highest_reccurance = nines
        highest_reccurance_prime = prime
print(f"The highest reccurance in the form 1/d is when d = {highest_reccurance_prime}, and has a reccurance of {highest_reccurance}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")