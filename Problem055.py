from time import perf_counter
def palindrome(num):
    return int(str(num)[::-1])
def is_palindrome(num):
    str_num = str(num)
    length = len(str_num)
    if length % 2 == 1:
        half = (length-1)/2
    else:
        half = length/2
    for check in range(int(half)):
        if str_num[check] != str_num[-(check+1)]:
            return False
    return True
def is_lychrel_num(num):
    check = num + palindrome(num)
    for i in range(49):
        if is_palindrome(check):
            return False
        check += palindrome(check)
    return True
start = perf_counter()
upto = 10000
lychrel_count = 0
for num in range(1,upto):
    if is_lychrel_num(num):
        lychrel_count += 1
end = (((perf_counter() - start)*100000)//1)/100
print(f"The number of lychrel numbers under {upto} is {lychrel_count}.\nThis took {end}ms")