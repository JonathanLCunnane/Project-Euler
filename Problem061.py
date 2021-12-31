from time import perf_counter
from euler_library import Combinatorics
from random import shuffle



def is_triangle_num(num):
    if (-0.5+(0.25+2*num)**0.5) % 1 == 0:
        return True
    return False


def is_square_num(num):
    if ((num)**0.5) % 1 == 0:
        return True
    return False


def is_pentagonal_num(num):
    if ((1/6)+((1/36)+(2/3)*num)**0.5) % 1 == 0:
        return True
    return False


def is_hexagonal_num(num):
    if (0.25+(0.0625+0.5*num)**0.5) % 1 == 0:
        return True
    return False


def is_heptagonal_num(num):
    if (0.3+(0.09+0.4*num)**0.5) % 1 == 0:
        return True
    return False


def is_octagonal_num(num):
    if round(((1/3)+((1/9)+(1/3)*num)**0.5), 8) % 1 == 0:
        return True
    return False


def check(num, type):
    """Returns the type of number it is as a numeral, i.e. a triangle number would return `3`, if `3` is `type`."""
    if type == 8:
        if is_octagonal_num(num):
            return 8
    if type == 7:
        if is_heptagonal_num(num):
            return 7
    if type == 6:
        if is_hexagonal_num(num):
            return 6
    if type == 5:
        if is_pentagonal_num(num):
            return 5
    if type == 4:
        if is_square_num(num):
            return 4
    if type == 3:
        if is_triangle_num(num):
            return 3
    return None


def possible_pairs(initial_pairs: list[list], next_check: int):
    """If `initial_pairs` is [], all that pass the check will be accepted."""
    accepted_pairs = []
    if initial_pairs == []:
        for num in range(1000, 10000):
            if check(num, next_check):
                accepted_pairs.append([num])
        return accepted_pairs
    for initial_pair in initial_pairs: # [[2701], [2775], ....]
        initial_num = initial_pair[-1]
        str_initial_num = str(initial_num)
        if str_initial_num[2] == "0":
            continue
        for end in range(10, 100):
            curr = int(str_initial_num[2:]+str(end))
            if check(curr, next_check):
                accepted_pairs.append(initial_pair + [curr])
    return accepted_pairs


def correct_set_present(list_of_lists_of_six: list[list]):
    for list_of_six in list_of_lists_of_six:
        if str(list_of_six[0])[:2] == str(list_of_six[-1])[2:]:
            return list_of_six
    return False


def find_ordered_set():
    # loop through possible arrangements of 3, 4, 5, 6, 7, 8
    pairs = []
    for perm in Combinatorics.permutations("345678"):
        check_order = [int(check_type) for check_type in perm]
        set_empty = False
        for check_type in check_order:
            pairs = possible_pairs(pairs, check_type)
            if pairs == []:
                set_empty = True
                break
        if not set_empty:
            set_present = correct_set_present(pairs)
            if set_present:
                return set_present


def main():
    start = perf_counter()
    cyclic_set_of_six = find_ordered_set()
    end = (((perf_counter() - start)*100000)//1)/100
    out = ", ".join([str(num) for num in cyclic_set_of_six])
    sum_of_nums = sum(cyclic_set_of_six)
    print(f"The set is {out}. Its sum is {sum_of_nums}.\nThis took {end}ms.")


if __name__ == "__main__":
    main()