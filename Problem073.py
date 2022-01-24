from time import perf_counter


def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1


d = 12000
start = perf_counter()
count = 0
for denom in range(2, d+1):
    for numer in range(2, denom):
        if numer * 3 <= denom:
            continue
        if numer * 2 >= denom:
            break
        if gcd(denom, numer) == 1:
            count += 1
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The number of reduced proper fractions between 1/3 and 1/2 when ordered up to a denominator of {d} is {count}.\nThis took {elapsed_ms}ms.")