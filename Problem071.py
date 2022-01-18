from time import perf_counter


def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1%n2
    return n1


upto = 1000000
below = 3/7
highest_num = 0
highest_frac_under = 0
for num in range(int(3*upto/7), 1, -1):
    for den in range(upto, 1, -1):
        if gcd(num, den) == 1:
            if num/den >= below:
                continue
            if num/den > highest_frac_under:
                print(f"{num}/{den}")
                highest_frac_under = num/den
                highest_num = num