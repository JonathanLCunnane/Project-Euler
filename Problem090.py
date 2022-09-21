from time import perf_counter
from itertools import combinations



# Brute force attempt.
def passes_checks(cube_alpha, cube_beta) -> bool:
    sqrs = [[0, 1], [0, 4], [0, 6], [1, 6], [2, 5], [3, 6], [6, 4], [8, 1]]
    for sqr in sqrs:
        if not(
            sqr[0] in cube_alpha and sqr[1] in cube_beta
            or
            sqr[1] in cube_alpha and sqr[0] in cube_beta
        ):
            return False
    return True
    


start = perf_counter()

cubes = list(combinations(range(10), 6))
valid_cubes = []
count = 0
for cube_one in cubes:
    for cube_two in cubes[cubes.index(cube_one) + 1:]:
        passed_cube_one = {side if side != 9 else 6 for side in cube_one}
        passed_cube_two = {side if side != 9 else 6 for side in cube_two}
        if passes_checks(passed_cube_one, passed_cube_two):
            count += 1



end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"{count}.\nThis took {elapsed_ms}ms.")