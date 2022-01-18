from time import perf_counter
from euler_library import Factors


# if we say euler's totient function phi(n) = f(n), and the distinct prime factors of n are a, b, c ... z
# the value of f(n) = n * (1-1/a) * (1-1/b) * (1-1/c) * ... * (1-1/z)  

upto = 1000000
max_n_over_fn = 0
max_n = 0
start = perf_counter()
for num in range(1, upto+1):
    distinct_factors = Factors.prime_factors(num, [], True)
    fn = num
    for factor in distinct_factors:
        fn *= (1-1/factor)
    n_over_fn = num / fn
    if n_over_fn > max_n_over_fn:
        max_n_over_fn = n_over_fn
        max_n = num
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The n for which n/phi(n) is maximised is:\t{max_n}\nwith the maximum n/phi(n) being:\t{max_n_over_fn}.\nThis took {elapsed_ms}ms")

# looking back on this problem, the solution for which n/phi(n) is largest is when phi(n) is smallest, i.e when n has the smallest amonut of relatively prime factors.
# therefore, the maximum n/phi(n) will be p1 * p2 * p3 * ... * pn where p is a prime, to the largest product which fits under 1,000,000, which is 
# 2 * 3 * 5 * 7 * 11 * 13 * 17 = 510510 in this case.