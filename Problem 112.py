from time import perf_counter, sleep


def is_bouncy(num: int):
    increasing = True
    decreasing = True

    last_digit = num % 10
    temp = num
    temp //= 10
    while temp > 0:
        next_digit = temp % 10
        if not (next_digit >= last_digit):
            decreasing = False
        if not (next_digit <= last_digit) or temp == 0:
            increasing = False
        temp //= 10
        last_digit = next_digit
    if not (increasing or decreasing):
        return True
    return False


proportion = 0
num = 0
count = 0
start = perf_counter()
while proportion != 0.99:
    num += 1
    if is_bouncy(num):
        count += 1
        proportion = count/num
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The number below which has 99% bouncy numbers is: {num}.\nThis took {elapsed_ms}ms.")