from time import perf_counter, time
from euler_library import Primes
import sys



def generate_prime_pairs(primes: list) -> set[set]:
    pairs = set()
    for prime_one in primes:
        for prime_two in primes:
            concat = int(str(prime_one)+str(prime_two))
            if Primes.is_prime(concat):
                reverse = int(str(prime_two)+str(prime_one))
                if Primes.is_prime(reverse):
                    pairs.add(concat)
                    continue
    return pairs


def lowest_prime_pair_set(upto) -> list:
    listprimes = Primes.fetch_primes(upto)
    pairs = generate_prime_pairs(listprimes)
    sets_found = []
    for prime_one in listprimes:
        for prime_two in listprimes:
            if prime_one == prime_two:
                continue
            if int(str(prime_one)+str(prime_two)) not in pairs or int(str(prime_two)+str(prime_one)) not in pairs:
                continue
            for prime_three in listprimes:
                if int(str(prime_one)+str(prime_three)) not in pairs or int(str(prime_three)+str(prime_one)) not in pairs:
                    continue
                if int(str(prime_two)+str(prime_three)) not in pairs or int(str(prime_three)+str(prime_two)) not in pairs:
                    continue
                for prime_four in listprimes:
                    if int(str(prime_one)+str(prime_four)) not in pairs or int(str(prime_four)+str(prime_one)) not in pairs:
                        continue
                    if int(str(prime_two)+str(prime_four)) not in pairs or int(str(prime_four)+str(prime_two)) not in pairs:
                        continue
                    if int(str(prime_three)+str(prime_four)) not in pairs or int(str(prime_four)+str(prime_three)) not in pairs:
                        continue
                    for prime_five in listprimes:
                        if int(str(prime_one)+str(prime_five)) not in pairs or int(str(prime_five)+str(prime_one)) not in pairs:
                            continue
                        if int(str(prime_two)+str(prime_five)) not in pairs or int(str(prime_five)+str(prime_two)) not in pairs:
                            continue
                        if int(str(prime_three)+str(prime_five)) not in pairs or int(str(prime_five)+str(prime_three)) not in pairs:
                            continue
                        if int(str(prime_four)+str(prime_five)) not in pairs or int(str(prime_five)+str(prime_four)) not in pairs:
                            continue
                        sets_found.append([prime_one, prime_two, prime_three, prime_four, prime_five])
    lowest_sum = sys.maxsize
    lowest_set = []
    for set_found in sets_found:
        temp_sum = sum(set_found)
        if sum(set_found) < lowest_sum:
            lowest_sum = temp_sum
            lowest_set = set_found
    return lowest_set, lowest_sum
start = perf_counter()
set_of_primes, sum_of_set = lowest_prime_pair_set(30000)
print(set_of_primes)
end = (((perf_counter() - start)*100000)//1)/100
print(f"The lowest prime pair set with 5 members is {set_of_primes}. The sum is {sum_of_set}.\nThis took {end}ms")