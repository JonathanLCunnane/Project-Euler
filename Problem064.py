from time import perf_counter
from math import log
from fractions import Fraction


def periodic_continued_fraction(num: int):
    # continued fraction generation via en.wikipedia.org/wiki/Periodic_continued_fraction#Canonical_form_and_repetend
    sqrtnum = num**0.5
    mn = 0
    dn = 1
    an = int(sqrtnum)
    double_an = 2 * an
    a_nplus1 = None
    periodic_shorthand = [an, []]
    while a_nplus1 != double_an:
        m_nplus1 = dn * an - mn
        d_nplus1 = (num - m_nplus1**2)/(dn)
        a_nplus1 = int((sqrtnum+m_nplus1)/(d_nplus1))
        periodic_shorthand[1].append(a_nplus1)
        mn = m_nplus1 
        dn = d_nplus1
        an = a_nplus1
    return periodic_shorthand


def has_odd_period_length(num: int):
    period = periodic_continued_fraction(num)[1]
    if len(period) % 2 == 0:
        return False
    return True


def main():
    upto = 10000
    next_square = 4
    next_skip = 2
    count = 0
    start = perf_counter()
    for num in range(2, upto + 1):
        if num == next_square:
            next_skip += 1
            next_square = next_skip ** 2
            continue
        if has_odd_period_length(num):
            count += 1
    end = perf_counter()
    elapsed_ms = (((end - start)*100000)//1)/100
    print(f"The amount of continued fractions of sqrt N with an odd period where N <= {upto} is {count}.\nThis took {elapsed_ms}ms.")

if __name__ == "__main__":
    main()