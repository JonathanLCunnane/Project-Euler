from time import perf_counter
from euler_library import Combinatorics
start = perf_counter()
upto = 10000000
for num in range(1, upto):
    set_num = set([int(i) for i in str(num)])
    if set([int(i) for i in str(num * 2)]) == set_num:
        if set([int(i) for i in str(num * 3)]) == set_num:
            if set([int(i) for i in str(num * 4)]) == set_num:
                if set([int(i) for i in str(num * 5)]) == set_num:
                    if set([int(i) for i in str(num * 6)]) == set_num:
                        end = (((perf_counter() - start)*100000)//1)/100
                        print(f"The number with the same digits in x, 2x, ..., 6x is: {num}.\nThis took {end}ms.")
                        break
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue