from itertools import combinations, product, permutations
from time import perf_counter



# Very brute force method oops.
operators = ["+", "-", "*", "/"]
groupings = ["x.x.x.x", "(x.x).x.x", "x.(x.x).x", "x.x.(x.x)", "(x.x).(x.x)", "(x.x.x).x", "x.(x.x.x)", "((x.x).x).x", "(x.(x.x)).x", "x.((x.x).x)", "x.(x.(x.x))"]
maximum = -1
maximum_number_set = []
start = perf_counter()


for numbers in combinations(range(10), 4):
    curr_products = set()
    for numb_perm in permutations(numbers, len(numbers)):
        for operator_perm in product(operators, repeat=len(numbers)-1):
            for group in groupings:
                formula = group
                for n in numb_perm: formula = formula.replace("x", str(n), 1)
                for op in operator_perm: formula = formula.replace(".", op, 1)
                try:
                    val = eval(formula) # Oh god the eval() function
                    if val % 1 == 0 and val > 0: curr_products.add(int(val))
                except: pass
    prev = -1
    for count, n in enumerate(curr_products):
        if count + 1 != n:
            if prev > maximum:
                maximum = prev
                maximum_number_set = numbers
            break
        prev = n


end = perf_counter()
elapsed_ms = (((perf_counter() - start)*100000)//1)/100
print(f"The highest number of consecutive integers from 1 that can be created is: {maximum}.\nThe set for this is: {maximum_number_set}\nTherefore the answer is: {''.join([str(num) for num in maximum_number_set])}\nThis took {elapsed_ms}ms.")