from time import perf_counter

upto = 7830457
num = 28433
start = perf_counter()
for i in range(upto):
    num *= 2
    if len(str(num)) >= 10:
        num = num % (10**10)
num += 1
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(num)