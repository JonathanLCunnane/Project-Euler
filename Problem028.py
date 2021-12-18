from time import perf_counter
# starting from the middle of the grid at 1, we will add up the four different direactions of 
# diagonals. Going up each time the top right will be (if n is width) n^2, top left will be 
# n^2 - n + 1, bottom left will be n^2 - 2n + 2, bottom right will be n^2 - 3n + 3
grid_size = 1001
# middle total starts at 1
total = 1
start = perf_counter()
for width in range(3, grid_size + 1, 2):
    width_squared = width ** 2
    total += 4 * width_squared - 6 * width + 6
print(f"Total of Spiral is: {total}, and this took {(((perf_counter() - start)*100000)//1)/100}ms.")
