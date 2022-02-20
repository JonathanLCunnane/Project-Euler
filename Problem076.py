from time import perf_counter

# Firstly, initialise an array representing the ways to make 'index' with 1
upto = 100
ways = [1] * (upto + 1)
start = perf_counter()
# then for each index > 1, we add the ways of making the number from each number below it as follows.
for prev in range(2, upto):
    for num in range(prev, upto + 1):
        ways[num] += ways[num-prev]
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The number of ways to sum {upto} is {ways[upto]}.\nThis took {elapsed_ms}ms.")