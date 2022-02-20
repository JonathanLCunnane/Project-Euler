from time import perf_counter
from euler_library import Primes


def generate_pythagorean_triples():
    triples = []
    for m in range(2, 900):
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
            if a+b+c < 1500000: triples.append((a, b, c))
    return triples

def main():
    start = perf_counter()
    triples = generate_pythagorean_triples()
    sums = [sum(triple) for triple in triples]
    upto = 1500000
    non_unique = set()
    unique = set()
    for trip_sum in sums:
        for k in range(1, upto//trip_sum + 1):
            new = trip_sum * k
            if new in unique:
                non_unique.add(new)
            unique.add(new)
    unique -= non_unique
    end = perf_counter()
    elapsed_ms = (((end - start)*100000)//1)/100
    print(f"The number of unique integer right triangles for integers under {upto} is {len(unique)}.\nThis took {elapsed_ms}ms.")


if __name__ == "__main__":
    main()