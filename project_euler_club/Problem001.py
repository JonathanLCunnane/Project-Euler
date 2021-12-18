from time import perf_counter
start = perf_counter()
multiple_one = 3
multiple_two = 5
up_to = 1000
n_multiple_one = up_to//multiple_one
n_multiple_two = up_to//multiple_two
product = multiple_one*multiple_two
n_both = up_to//(product)
sum_of_multiples = int((multiple_one*n_multiple_one*(n_multiple_one+1)/2) + (multiple_two*n_multiple_two*(n_multiple_two+1)/2) - (product*n_both*(n_both+1)/2))
end = (((perf_counter() - start)*1000000000)//1)/1000000
print(f"The sum of all multiple of {multiple_one} or {multiple_two} up to {up_to} is {sum_of_multiples}.\nThis took {end}ms")