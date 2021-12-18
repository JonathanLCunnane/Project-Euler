from time import perf_counter
from euler_library import Combinatorics
start = perf_counter()
pandigitals = Combinatorics.permutations("0123456789")
sum = 0
for num in pandigitals:
    if num[0] == "0":
        continue
    if int(num[1] + num[2] + num[3]) % 2 == 0:
        if int(num[2] + num[3] + num[4]) % 3 == 0:
            if int(num[3] + num[4] + num[5]) % 5 == 0:
                if int(num[4] + num[5] + num[6]) % 7 == 0:
                    if int(num[5] + num[6] + num[7]) % 11 == 0:
                        if int(num[6] + num[7] + num[8]) % 13 == 0:
                            if int(num[7] + num[8] + num[9]) % 17 == 0:
                                sum += int(num)
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
        else:
            continue
    else:
        continue
print(f"The sum of all 0-9 pandigitals with this property is {sum}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")