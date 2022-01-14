from time import perf_counter


# e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, ..., 2k, 1, 1, ...]
# generate the first 100 a's
upto = 100
start = perf_counter()
e = [2, [1 if (i+2) % 3 != 0 else int(((i+2)/3)*2) for i in range(upto-1)]]
frac_approximations = []
numerator_nm2 = e[0]
denominator_nm2 = 1
numerator_nm1 = e[1][0] * e[0] + 1
denominator_nm1 = e[1][0]
for an in e[1][1:]:
    numerator_n = an*numerator_nm1 + numerator_nm2
    denominator_n = an*denominator_nm1 + denominator_nm2
    numerator_nm2, numerator_nm1, denominator_nm2, denominator_nm1 = numerator_nm1, numerator_n, denominator_nm1, denominator_n
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The 100th approximation for e using continued fractions is: {numerator_n}/{denominator_n}.\nThe sum of digits in the numerator is: {sum([int(digit) for digit in str(numerator_n)])}.\nThis took {elapsed_ms}ms") 