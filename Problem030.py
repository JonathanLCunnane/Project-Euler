from time import perf_counter
start = perf_counter()
# we will brute force this up to 100,000,000 and print out the sum of all numbers 
# that can be represented by their sums of powers of 5 of the digits as we go along
upto = 100000000
nums = []
sum_of_nums = 0
for num in range(10, upto):
    if sum([int(x)**5 for x in str(num)]) == num:
        nums.append(num)
        sum_of_nums += num
        print(f"A new number: {num}, was found. This took {(((perf_counter() - start)*100000)//1)/100}ms.\nAll oof the nums are: {nums} and their sum is {sum_of_nums}.")
print(f"Complete at {(((perf_counter() - start)*100000)//1)/100}ms")