from time import perf_counter

# the number is 19 digits long, but has to end with two zeros, 
# so we only need to find a 17 digit number starting from 9 digit numbers squared

square_found = False
num = 100000000
start = perf_counter()
while not square_found:
    # if num does not end with 3, 7 last digit cannot be 9 so reject
    if str(num)[-1] != "3" or str(num)[-1] != "7":
        num += 1
        continue
    square = str(num**2)
    num += 1
    if square[0] != "1":
        continue
    if square[2] != "2":
        continue
    if square[4] != "3":
        continue
    if square[6] != "4":
        continue
    if square[8] != "5":
        continue
    if square[10] != "6":
        continue
    if square[12] != "7":
        continue
    if square[14] != "8":
        continue
    square_found = square
    break
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
square_num = int(str(square_found) + "00")
print(f"The num which has a square in the form 1_2_3_4_5_6_7_8_9_0 is {int(square_num**0.5)}, and the sqaure is {square_found}.\nThis took {elapsed_ms}ms.")