from time import perf_counter

def reversed(num: int):
    reverse = 0
    while num > 0:
        curr = num % 10
        reverse *= 10
        reverse += curr
        num //= 10
    return reverse

upto = 1000000000
start = perf_counter()
count = 0
for i in range(1, upto + 1):
    if i % 10 == 0:
        continue
    reverse = reversed(i)
    summ = reversed(i) + i
    temp = summ
    reversable = True
    while temp > 0:
        curr = temp % 10
        if curr % 2 == 0:
            reversable = False
            break
        temp //= 10
    if reversable:
        count += 1  
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"{count} below {upto}.\nThis took {elapsed_ms}ms")