from time import perf_counter

# generate factorials and check digit number,
# and when the digit number is 1000, terminate the program.

fibbonaci_minus_one = 1
fibbonaci = 2
length = 1000
index_number = 3
start = perf_counter()
while len(str(fibbonaci)) != length:
    fibbonaci, fibbonaci_minus_one = fibbonaci_minus_one + fibbonaci, fibbonaci
    index_number += 1
print(f"The first fibbonaci number with {length} digits is: {fibbonaci}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms, and has index {index_number}")