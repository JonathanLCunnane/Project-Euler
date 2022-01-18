from time import perf_counter


upto = 1000000
count = 0
start = perf_counter()
# the below phi uses the product rule for phi, which is phi(n) = n(1-1/p1)(1-1/p2)...(1-1/pn) where p1 to pn are the distinct primes under n
# we will use a sieve where all the numbers that are multiples of primes will be multiplied by (1-1/p) where p is the prime. 
# we need to sieve up to 'upto' variable.
phi_sieve = list(range(0, upto+1))
for denom in range(2, upto+1):
    # if the denom is prime then we need to sieve out all the occurances by multiplying all numbers with a factor of denom by (1-1/denom)
    if phi_sieve[denom] == denom:
        phi_sieve[denom] -= 1
        phi_sieve[denom*2::denom] = [i * (1-1/denom) for i in phi_sieve[denom*2::denom]]
    count += int(phi_sieve[denom])
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The amount of reduced proper fractions in the form n/d where d <= {upto} is {count}.\nThis took {elapsed_ms}ms.")