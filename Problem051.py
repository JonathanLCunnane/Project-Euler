# we will start by generating primes under 1,000,000. If we need more primes, 
# then we will generate these later.
# we also know that the last digit cannot be the one that changes, as this would
# mean that we would have an even number in our set of eight, i.e. not a prime
#  
# loop through the primes, and find the different combinations with zero first,
# then one, two etc. seeing if there are eight primes among them. 
# if there are more than two values that are not prime, then we will skip to the next prime
# number
from time import perf_counter
from euler_library import Primes, Combinatorics
def duplicates(num):
    strnum = str(num)
    dupes = []
    for digit in strnum:
        count = strnum.count(digit)
        if count > 1:
            dupes.append(digit)
            strnum = strnum.translate({ord(digit): ""})
    return dupes
upto = 1000000
start = perf_counter()
prime_list = Primes.fetch_primes(upto, False)
prime_set = set(prime_list)
digits = ["0","1","2","3","4","5","6","7","8","9"]
for prime in prime_list:
    for duplicate_digit in duplicates(prime):
        not_prime_lives = 2
        prime_count = 1
        for digit in digits:
            strprime = str(prime)
            if not_prime_lives == -1:
                break
            if digit == duplicate_digit:
                continue
            strprime = strprime.translate({ord(duplicate_digit): digit})
            if int(strprime) not in prime_set:
                not_prime_lives -= 1
            elif strprime[0] == "0":
                not_prime_lives -= 1
            else:
                prime_count += 1
        if prime_count >= 8:
            end = (((perf_counter() - start)*100000)//1)/100
            print(f"The lowest 8 number prime digit replacement is: {prime}.\nThis took {end}ms")
            for digit in digits:
                strprime = str(prime)
                strprime = strprime.translate({ord(duplicate_digit): digit})
                print(f"Is {strprime} prime: {Primes.is_prime(int(strprime))}")
            break
    else:
        continue
    break
