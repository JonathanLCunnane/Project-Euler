from time import perf_counter, sleep
from euler_library import Combinatorics as cmb


def factorial_digit_sum(num: int) -> int:
    return sum([cmb.factorial(int(digit)) for digit in str(num)])


def factorial_chain_len(num: int) -> int:
    seen = [num]
    next = factorial_digit_sum(num)
    while next not in seen:
        seen.append(next)
        next = factorial_digit_sum(seen[-1])
    return len(seen)


def main():
    start = perf_counter()
    upto = 1000000
    count = 0
    for num in range(1, upto + 1):
        if factorial_chain_len(num) == 60:
            count += 1
    end = perf_counter()
    elapsed_ms = (((end - start)*10000000)//1)/10000
    print(f"The number of factorial chains below {upto} with a length of 60 is {count}.\nThis took {elapsed_ms}ms.")


if __name__ == "__main__":
    main()