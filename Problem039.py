from time import perf_counter
from euler_library import Primes
def generate_pythagorean_triples():
    triples = []
    for m in range(2, 22):
        for n in range(1, m):
            last_n = int(str(n)[-1])
            last_m = int(str(m)[-1])
            n_mod = last_n % 2
            m_mod = last_m % 2
            is_opposite_in_parity = ((n_mod == 0 and m_mod % 2 == 1) or (n_mod == 1 and m_mod % 2 == 0))
            is_coprime = Primes.is_coprime(n, m)
            if not (is_coprime and is_opposite_in_parity):
                continue
            
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a+b+c < 1000: triples.append((a, b, c))
    return triples
start = perf_counter()
triples = generate_pythagorean_triples()
print(f"Triples generated in {(((perf_counter() - start)*100000)//1)/100}ms")
perimeters = [triple[0] + triple[1] + triple[2] for triple in triples]
max_p = 0
max_count = 0
for p in range(12, 1001):
    count = 0
    for check in perimeters:
        if p % check == 0:
            count += 1
    if count > max_count:
        max_count = count
        max_p = p
print(f"The largest number of pythagorean triple solutions for p <= 1000 is {max_count}, with the triangle's perimeter being {max_p}.\nThis took {(((perf_counter() - start)*100000)//1)/100}ms")