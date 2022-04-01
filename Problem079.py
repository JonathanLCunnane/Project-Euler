from time import perf_counter
from decimal import Decimal, getcontext
from euler_library import Primes
getcontext().prec = 10**2 + 3


def sum_first_hundred_decimal_places(num: int):
    sqrt = str(Decimal(num).sqrt())
    decimalplaces = sqrt.replace(".", "")[:100]
    return sum([int(digit) for digit in decimalplaces])


def main():
    upto = 100
    currsqr = 2
    sumofdigits = 0
    start = perf_counter()
    for n in range(2, upto + 1):
        if currsqr**2 == n:
            currsqr += 1
            continue
        sumofdigits += sum_first_hundred_decimal_places(n)
    end = perf_counter()
    elapsed_ms = (((end - start)*100000)//1)/100
    print(f"The sum of the first 100 digits of the square roots of all irrational square roots up to 100 is: {sumofdigits}.\nThis took {elapsed_ms}ms.")
        

if __name__ == "__main__":
    main()