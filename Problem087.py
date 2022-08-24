from time import perf_counter
from euler_library import Primes


# For this problem, we will say that a number is represented by x^2 + y^3 + z^4 : x, y, and z are prime.
start = perf_counter()
upto = 50000000
x_max = (upto - 24)**0.5
y_max = (upto - 20)**(1/3)
z_max = (upto - 12)**0.25
primes = Primes.fetch_primes(upper=x_max, set=True)
unique = set()

for x in primes:
    if x > x_max:
        continue
    for y in primes:
        if y > y_max:
            continue
        for z in primes:
            if z > z_max:
                continue
            sum = x**2 + y**3 + z**4
            if sum >= upto:
                continue
            unique.add(sum)       

end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The amount of unique prime pair triples under {upto} is {len(unique)}.\nThis took {elapsed_ms}ms.")