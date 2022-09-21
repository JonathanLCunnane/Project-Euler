from time import perf_counter


# Brute force attempt


def m(x_a, y_a, x_b, y_b):
    if x_a == x_b:
        return None
    return (y_a - y_b)/(x_a - x_b)


def det(x_a, y_a, x_b, y_b):
    return x_a * y_b - y_a * x_b


start = perf_counter()

x_max, y_max = 50, 50
x_0, y_0 = 0, 0
count = 0
for x_1 in range(x_max + 1):
    for y_1 in range(y_max + 1):
        for x_2 in range(x_max + 1):
            for y_2 in range(y_max + 1):
                if det(x_1, y_1, x_2, y_2) == 0:
                    continue
                d_0_1 = x_1**2 + y_1**2
                d_0_2 = x_2**2 + y_2**2
                d_1_2 = (x_2 - x_1)**2 + (y_2 - y_1)**2
                if d_0_1 + d_0_2 == d_1_2:
                    count += 1
                elif d_0_2 + d_1_2 == d_0_1:
                    count += 1
                elif d_0_1 + d_1_2 == d_0_2:
                    count += 1
# Each point is generated twice (could be cleaned up), therefore:
count = count//2

end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"{count}.\nThis took {elapsed_ms}ms.")