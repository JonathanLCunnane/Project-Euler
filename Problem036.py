from time import perf_counter
def reverse(num):
    num = str(num) #567
    new = ""
    for digit in range(len(num)):
        new += num[-digit-1]
    return new
start = perf_counter()
# loop throguh all numbers, and if reverse is equal to number, 
# then it is a palindrome, also check for binary version
sum = 0
for num in range(1,1000000):
    binary = format(num, "b")
    if str(num) == reverse(num) and binary == reverse(binary):
        sum += num
print(f"The sum of all double-base palindromes is: {sum}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")