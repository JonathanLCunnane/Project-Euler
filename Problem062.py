from time import perf_counter
from euler_library import Combinatorics


num_of_perms_to_find = 5
perms_found = []
cubes = []
curr = 1
start = perf_counter()
while len(perms_found) < num_of_perms_to_find:
    perms_found = []
    perm_found = False
    curr_cube = str(curr**3)
    cubes.append(curr_cube)
    for cube in cubes[:-1]:
        if Combinatorics.is_permutation(curr_cube, cube):
            perm_found = True
            perms_found.append(cube)
    if perm_found:
        perms_found.append(curr_cube)
    curr += 1
smallest = perms_found[0]
end = (((perf_counter() - start)*100000)//1)/100
print(perms_found)
print(f"The smallest cube of {num_of_perms_to_find} cubes which are permutations of each other is {smallest}.\nThis took {end}ms")