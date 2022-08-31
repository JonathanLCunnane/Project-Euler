from sys import maxsize
from time import perf_counter
from euler_library import Primes


# Sometimes trying to be smart is not the most efficient use of my time oh no. (Brute force below.)
"""# New idea if x not prime, n = xy, n =/ x /= y, x and y are ints. 
# Consider {1, 1, ..., x, y} first
# Then do the same for any factors of x
# Then any factors of y, recursively.
def get_factor_groups(n: int, existing: tuple = tuple()):
    grps = set()
    if Primes.is_prime(n):
        return grps
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            quot = n//i
            grps.add((i, quot, *existing))
            grps |= get_factor_groups(i, (quot, *existing))
            grps |= get_factor_groups(quot, (i, *existing))
    return grps


def unique_groups(groups: list[tuple()]):
    grps = {tuple(sorted(grp)) for grp in groups}
    return grps


def minimal_product_sums(upto: int):
    count = 0
    n = 4
    sums = [maxsize for n in range(upto - 1)]
    while n < upto * 2:
        grps = get_factor_groups(n)
        unique_grps = unique_groups(grps)
        for grp in unique_grps:
            set_size = len(grp) + n - sum(grp)
            if set_size <= upto and n <= sums[set_size - 2]:
                if sums[set_size - 2] == maxsize:
                    count += 1
                sums[set_size - 2] = n
        n += 1
    return sums
        

start = perf_counter()
upto = 12
minimal_products = minimal_product_sums(upto)
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The sum of minimal product sums from 2 <= k <= {upto} is: {sum(set(minimal_products))}.\nThis took {elapsed_ms}ms.")"""

start = perf_counter()
upto = 12000
upto_o2 = (upto // 2)
upto_m2 = upto * 2
sums = [maxsize for n in range(upto + 1)]

# 13 Nested loops since floor(log_2(12000)) = 13
for a in range(1, upto_o2):
    for b in range(a, upto_o2):
        prod = a * b
        if prod > upto_m2: break
        for c in range(b, upto_o2):
            prod = a * b * c
            if prod > upto_m2: break
            for d in range(c, upto_o2):
                prod = a * b * c * d
                if prod > upto_m2: break
                for e in range(d, upto_o2):
                    prod = a * b * c * d * e
                    if prod > upto_m2: break
                    for f in range(e, upto_o2):
                        prod = a * b * c * d * e * f
                        if prod > upto_m2: break
                        for g in range(f, upto_o2):
                            prod = a * b * c * d * e * f * g
                            if prod > upto_m2: break
                            for h in range(g, upto_o2):
                                prod = a * b * c * d * e * f * g * h
                                if prod > upto_m2: break
                                for i in range(h, upto_o2):
                                    prod = a * b * c * d * e * f * g * h * i
                                    if prod > upto_m2: break
                                    for j in range(i, upto_o2):
                                        prod = a * b * c * d * e * f * g * h * i * j
                                        if prod > upto_m2: break
                                        for k in range(j, upto_o2):
                                            prod = a * b * c * d * e * f * g * h * i * j * k
                                            if prod > upto_m2: break
                                            for l in range(k, upto_o2):
                                                prod = a * b * c * d * e * f * g * h * i * j * k * l
                                                if prod > upto_m2: break
                                                for m in range(l, upto_o2):
                                                    prod = a * b * c * d * e * f * g * h * i * j * k * l * m
                                                    if prod > upto_m2: break
                                                    curr_sum = a + b + c + d + e + f + g + h + i + j + k + l + m
                                                    set_size = 13 + prod - curr_sum
                                                    if set_size > upto: break
                                                    if prod < sums[set_size]:
                                                        sums[set_size] = prod
sums = sums[2:]                                                  
minimal_product_sums_sum = sum(set(sums))
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The sum of minimal product sums from 2 <= k <= {upto} is: {minimal_product_sums_sum}.\nThis took {elapsed_ms}ms.")