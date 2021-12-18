from time import perf_counter
start = perf_counter()
total = 0
upto = 1000
for i in range(1, upto+1):
    total += i**i
print(f"The total of the first {upto} self-primes is {total}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")