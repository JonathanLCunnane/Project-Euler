from time import perf_counter


# the smallest solution can be found by looping through the continued fraction convergents, and 
# seeing if x as the numerator and y as the denominator satisfies the equation.


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


def convergent_fractions_approximations(periodic_shorthand: list):
    # you must break out of this generator or it will continue to generate convergents, as there are infinitely many
    """Returns a tuple in the form `(numerator, denominator)`"""
    numerator_nm2 = periodic_shorthand[0]
    denominator_nm2 = 1
    yield (numerator_nm2, denominator_nm2)
    numerator_nm1 = periodic_shorthand[1][0] * periodic_shorthand[0] + 1
    denominator_nm1 = periodic_shorthand[1][0]
    yield (numerator_nm1, denominator_nm1)
    if periodic_shorthand[1][1:] == []:
        periodic_shorthand[1] = [periodic_shorthand[1][0]] * 2
    for an in periodic_shorthand[1][1:]:
            numerator_n = an*numerator_nm1 + numerator_nm2
            denominator_n = an*denominator_nm1 + denominator_nm2
            yield (numerator_n, denominator_n)
            numerator_nm2, numerator_nm1, denominator_nm2, denominator_nm1 = numerator_nm1, numerator_n, denominator_nm1, denominator_n
    while True:
        for an in periodic_shorthand[1]:
            numerator_n = an*numerator_nm1 + numerator_nm2
            denominator_n = an*denominator_nm1 + denominator_nm2
            yield (numerator_n, denominator_n)
            numerator_nm2, numerator_nm1, denominator_nm2, denominator_nm1 = numerator_nm1, numerator_n, denominator_nm1, denominator_n


def main():
    max_x = 0
    max_x_D = 0
    upto = 1000
    start = perf_counter()
    for D in range(1, upto+1):
        if D**0.5 % 1 == 0:
            continue
        periodic_shorthand = periodic_continued_fraction(D)
        for x, y in convergent_fractions_approximations(periodic_shorthand):
            if x**2 - (D*y**2) == 1:
                if x > max_x:
                    max_x = x
                    max_x_D = D
                break
    end = perf_counter()
    elapsed_ms = (((end - start)*100000)//1)/100
    print(f"The largest x obtained for minimal solutions to the equation x^2 - Dy^2 = 1 for D <= {upto} is: {max_x}, at D = {max_x_D}.\nThis took {elapsed_ms}ms")


if __name__ == "__main__":
    main()