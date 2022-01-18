from time import perf_counter
from euler_library import Combinatorics, Primes


"""# for the following function if we have n1 = (3)(7)xyz, n2 = (5)(2)xyz with a gcd of xyz,
# when we subtract the remainder from each other, i.e. n1 - n2
# also shown as n1%n2, then the greatest common divisor of the two 
# will not change. i.e. new = n1%n2 = (11)xyz. Then if we take the smaller
# of n1 and n2 and do the same new%n2 = xyz. If we did this one more time,
# the difference would be, so we go until the difference is zero. If the size 
# of numbers is switched, the first time we use mod they will be ordered.
def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1


# for the following phi function, we are using the fact that phi(n) is the number 
# of integers k for which 1 <= k <= n for which n and k are coprime, i.e. gcd(n, k) == 1
def phi(n):
    if n < 3:
        if n > 0:
            return 1
        n = -n
    phi = 2
    k = n - 2
    while k-1:
        if gcd(n, k) == 1:
            phi += 1
        k -= 1
    return phi"""


# we want to minimise n/φ(n), therefore we need to minimise the number of factors of n since n/φ(n) = 1/(1-1/p1)(1-1/p2)...(1-1/pn)
# if n is prime, φ(n) = n-1, so they are not permutations, so we will choose the next thing
# which is two prime factors. sqrt(10^7) = 3162, so we need to multiply primes 'close' to that value, lets say between in a 
# 3000 interval, so between 1662 and 4662.
# using the product formula, φ(n) = n(1-1/p1)(1-1/p2)...(1-1/pn) where p1 -> pn are prime factors
# therefore . In our case we only want two prime factors, so
# n = p1p2, φ(n) = n(1-1/p1)(1-1/p2) = p1p2(1-1/p1)(1-1/p2) = (p1-1)(p2-1), therefore 
# n/φ(n) = n/(p1-1)(p2-1) = p1p2/(p1-1)(p2-1)
min_ratio = 5 # from testing most ratios are below 5
min_n = 0
upto = 10000000
start = perf_counter()
for p1 in range(1662, 5000):
    if not Primes.is_prime(p1):
        continue
    for p2 in range(1662, 5000):
        if not Primes.is_prime(p2):
            continue
        n = p1 * p2
        if n > upto:
            break
        phi_n = (p1-1)*(p2-1)
        if Combinatorics.is_int_permutation(n, phi_n):
            ratio = n/phi_n
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The n for which n/φ(n) is lowest for 1 <= n <= 10^7 and n is a permutation of φ(n) is : {min_n, min_ratio}.\nThis took: {elapsed_ms}ms.")