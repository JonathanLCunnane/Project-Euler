# we will simply loop through all fractions iteratively from 10/10 to 10/99 to 20/99 ... 99/99
# if there is a duplicate or duplicates in the numerator and denominator, cancel them and
# check if it works as a curious fraction.
from time import perf_counter
start = perf_counter()
def check_indices(numerator, denominator, numerator_index, denominator_index):
    str_numerator = str(numerator)
    str_denominator = str(denominator)
    if str_numerator[1] == "0" and str_denominator[1] == "0":
        return 
    if str_numerator[numerator_index] == str_denominator[denominator_index]:
        try:
            not_numerator_index = int(not numerator_index)
            not_denominator_index = int(not denominator_index)
            if str_numerator[not_numerator_index] == str_denominator[not_denominator_index]:
                return
            division = numerator / denominator
            if int(str_numerator[not_numerator_index]) / int(str_denominator[not_denominator_index]) == division and division <= 1:
                print(f"Fraction found: {numerator}/{denominator}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")
        except ZeroDivisionError:
            return
for numerator in range(10,100):
    for denominator in range(10,100):
        check_indices(numerator, denominator, 0, 0)
        check_indices(numerator, denominator, 0, 1)
        check_indices(numerator, denominator, 1, 0)
        check_indices(numerator, denominator, 1, 1)