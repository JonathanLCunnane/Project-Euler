from time import perf_counter


"""def generate_pythagorean_triples(upto: int=20):
    triples = []
    for m in range(2, upto):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            triples.append((a, b))
    triples.sort(key=lambda triple: max(triple))
    return triples

triples = generate_pythagorean_triples(1000)
print(triples[:100])
count = 0
m = 0
for triple in triples:
    count += triple[1]/2
    if count > 2000:
        m = max(triple)
        break"""

M = 2
dimensions = []
count = 0
upto = 1000000
start = perf_counter()
while count < upto:
    M += 1
    # In this case we have x = M, yz = y + z. Shortest distance is sqrt(x**2 + yz**2) where z <= y <= x
    for yz in range(2, 2 * M + 1):
        # Firstly check if z < y < x if there is an integer path
        if ((yz)**2 + M**2)**0.5 % 1 == 0:
            # If yz <= x, then z <= y <= x always, so add yz//2 to count.
            if yz <= M:
                count += yz // 2
            # Else yz > M, therefore we can only add from z = y = x to z = ?, y = M, x = M. (Note: (yz + 1)//2 = ceil(yz / 2))
            else:
                count += M - (yz + 1)//2 + 1
end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"For a cuboid max dimensions of M x M x M, M = {M}, the number of shortest parts from opposite corners that are integers is {count}.\nThis took {elapsed_ms}ms.")