from time import perf_counter


# if we represent the n-digit number by x^y, when x stays the same, when y > n, x^y will never be y digits long as y increases. 
# Also, if x^y is ever y digits long, it will be y digits long from y = 1 to when y > n. Therefore we only need to check for 1 <= x < 10 
count = 0
start = perf_counter()
for x in range(1, 10):
    y = 1
    power = x**y
    while len(str(power)) == y:
        count += 1
        y += 1
        power = x**y
end = (((perf_counter() - start)*100000)//1)/100
print(f"There are {count} n-digit numbers that are an nth power.\nThis took {end}ms")