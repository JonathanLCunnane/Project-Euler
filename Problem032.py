# we can deduce that we only need to check 2 digit numbers multiplied by 3 digit numbers, 
# up to when the product is a 4 digit number
from time import perf_counter
start = perf_counter()
digits = {1,2,3,4,5,6,7,8,9}
products = set()
for multiplicand in range(1, 10000):
    for multiplier in range(1,1000):
        product = multiplicand * multiplier
        list_of_digits = [int(digit) for digit in str(multiplicand)] + [int(digit) for digit in str(multiplier)] + [int(digit) for digit in str(product)]
        if set(list_of_digits) == digits and len(list_of_digits) == 9:
            print(multiplicand, multiplier, product)
            products.add(product)
sum = 0
for product in products: sum += product
print(f"Sum of pandigital products is: {sum}, and this took {(((perf_counter() - start)*100000)//1)/100}ms.")