from time import perf_counter



# Triangle base b, two sides a
# h^2 + b^2/4 = a^2
# b = a +/- 1
# Therefore: h^2 + (a -/+ 1)^2/4 = a^2
# 4h^2 + a^2 -/+ 2a + 1 = 4a^2
# 3a^2 +/- 2a = 4h^2 + 1
# 9a^2 +/- 6a + 1 = 12h^2 + 4
# (3a +/- 1)^2 = 12h^2 + 4
# ((3a +/- 1)/2)^2 - 3h^2 = 1
# Let x = (3a +/- 1)/2, y = h
# x^2 - 3y^2 = 1, A Pell's equation! (where n = 3)
# We find that the fundamental solution is x_1 = 2, y_1 = 1
# So we can use the iterative formulae:
# x_k+1 = x_1*x_k + n*y_1*y_k
# y_k+1 = x_1*y_k + y_1*x_k
# Which in this case will be:
# x_k+1 = 2*x_k + 3*y_k
# y_k+1 = 2*y_k + x_k
# Then we need to find if the area and a are integral:
# A = (a +/- 1)*h/2
# x = (3a +/- 1)/2, therefore a = (2x -/+ 1)/3
# A = ((2x -/+ 1)/3 +/- 1)*y/2
# A = y*(2x +/- 2)/6
# A = y*(x +/- 1)/3

upto = 1000000000
perim_sum = 0
start = perf_counter()
prev_x = 2
prev_y = 1
while True:
    x = 2*prev_x + 3*prev_y
    y = 2*prev_y + prev_x

    # Firstly consider when b = a + 1
    # A = y*(x + 1)/3, a = (2x - 1)/3, P = 3*a + 1
    A3 = y*(x + 1)
    a3 = 2*x - 1
    if A3 % 3 == 0 and a3 % 3 == 0:
        if A3 > 0 and a3 > 0:
            perim_sum += a3 + 1

    # Then consider when b = a - 1
    # A = y*(x - 1)/3, a = (2x + 1)/3, P = 3*a - 1
    A3 = y*(x - 1)
    a3 = 2*x + 1
    if A3 % 3 == 0 and a3 % 3 == 0:
        if A3 > 0 and a3 > 0:
            if a3 - 1 > upto: break
            perim_sum += a3 - 1

    prev_x = x
    prev_y = y

end = perf_counter()
elapsed_ms = (((perf_counter() - start)*100000)//1)/100
print(f"The sum of perimeters of the 'almost perfect' equilateral triangles with integral areas is: {perim_sum}\nThis took {elapsed_ms}ms.")