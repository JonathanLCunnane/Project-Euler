from time import perf_counter

# brute force by looping from 0123456789 to 9876543210 
# and checking if the number has digits 0 - 9, and if it does, 
# add to the permutation counter. When the permutation counter 
# is at 1mil, print out the current permutation.

digits = set(str(1234567890))
digitsexczero = set(str(123456789))
perm_counter = 0
for num in range(123456789, 1000000000):
    if set(str(num)) == digitsexczero:
        perm_counter += 1
        if perm_counter == 1000000:
            print(num)
            break
for num in range(1000000000, 9876543210):
    if set(str(num)) == digits:
        perm_counter += 1
        if perm_counter == 1000000:
            print(num)
            break