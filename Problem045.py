from time import perf_counter
def is_pentagonal(num):
    disc = 1+24*num
    if disc < 0:
        return False
    if ((1+disc**0.5)/6)%1 == 0:
        return True
    return False
def is_hexagonal(num):
    disc = (1+8*num)**0.5
    if disc < 0:
        return False
    if ((1+disc)/4)%1 == 0:
        return True
    return False
n = 285
start = perf_counter()
while True:
    n += 1
    triangle = n*(n+1)*0.5
    if is_pentagonal(triangle):
        if is_hexagonal(triangle):
            print(f"The next Triangle number that is also Pentagonal and Hexagonal is {triangle}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms.")
            break