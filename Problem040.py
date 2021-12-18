from time import perf_counter
start = perf_counter()
decimal = "."
for num in range(1, 1000000):
    decimal += str(num)
print(int(decimal[1])*int(decimal[10])*int(decimal[100])*int(decimal[1000])*int(decimal[10000])*int(decimal[100000])*int(decimal[1000000]))