class Primes:
    def fetch_primes(upper: int=100000, set: bool=True, raw: bool=False):
        """Returns a set of primes up to `upper`."""
        if upper % 2 == 1: upper += 1
        int_upper_over_two = int(upper/2)
        bools = [True] * int_upper_over_two
        bools[0] = False
        for odd in range(1, int_upper_over_two):
            if bools[odd]:
                current = odd*2+1
                start = current+odd
                bools[start::current] = ((int_upper_over_two-start-1)//current+1) * [False]
        if raw:
            return bools
        if set:
            return {2} | {prime*2+1 for prime in range(1,int_upper_over_two) if bools[prime]}
        return [2] + [prime*2+1 for prime in range(1,int_upper_over_two) if bools[prime]]
    def is_prime(num: int=1) -> bool:
        """Returns **True** if `num` is prime. Otherwise returns **False**."""
        # we are using the sieve to initially check a few numbers, and then checknig all numbers in the form 6k +/- 1, as all primes can be represented as such
        if num <= 3:
            return (num > 1)
        if num % 2 == 0 or num % 3 == 0:
            return False
        # we use 5 as we will use check to be the 6k - 1 term, therefore adding two to check in (check + 2) gives the 6k  
        for check in range(5, int(num ** 0.5), 6):
            if num % check == 0:
                return False
            if num % (check + 2) == 0:
                return False
        return True
    def is_coprime(num_one, num_two) -> bool:
        """Returns **True** if `num_one` is coprime to `num_two`. Otherwise returns **False**."""
        evens = {0, 2, 4, 6, 8}
        fives = {0, 5}
        last_one = int(str(num_one)[-1])
        last_two = int(str(num_two)[-1])
        if last_one in evens and last_two in evens: return False
        if last_one in fives and last_two in fives: return False
        if num_two == num_one + 1 or num_one == num_two + 1:
            return True
        while num_one != 0 and num_two != 0:
            if num_two > num_one:
                num_two %= num_one
            else:
                num_one %= num_two
        hcf = max(num_one, num_two)
        if hcf > 1:
            return False
        return True
class Combinatorics:
    def factorial(num: int = 0):
        """Returns the factorial as an int of `num`."""
        if num <= 1:
            return 1
        else:
            return num * Combinatorics.factorial(num-1)
    def nCr(n, r):
        if r > n or r < 0: return None
        return Combinatorics.factorial(n)/(Combinatorics.factorial(n-r)*Combinatorics.factorial(r))
    def swap(input: str, index_one: int, index_two: int) -> str:
        """Returns a list from `input` with index `index_one` swapped with `index_two`."""
        arr = list(input)
        arr[index_one], arr[index_two] = arr[index_two], arr[index_one]
        return arr
    def swaps(input: str, start_index: int = 0, perm_list: list = [], num: int = 1) -> set:
        """Returns a list of the number swaps from `start_index` of `input`.\n**NOTE: Do not use unless you know what you are doing!**"""
        if start_index == len(input):
            perm_list.append("".join(input))
        for swap in range(start_index, len(input)):
            swapped = Combinatorics.swap(input, start_index, swap)
            Combinatorics.swaps(swapped, start_index + 1, perm_list, num)
        return perm_list
    def permutations(input: str) -> set:
        """Returns a set of permutations for a input string `input`."""
        return set(Combinatorics.swaps(input, 0, [], Combinatorics.factorial(len(input))))
    def is_permutation(original: str, compare: str):
        if len(original) != len(compare): return False
        comparearr = [char for char in compare]
        for char in original:
            try:
                comparearr.remove(char)
            except ValueError:
                return False
        return True
class Factors:
    def prime_factors(num: int=1, initial: list=[], distinct: bool=False):
        """Returns the prime factors including the initial factors in `initial`.\nIt is recommended to not alter `initial`."""
        if num % 1 != 0:
            return initial
        else:
            num = int(num)
        if num < 2: return initial
        if Primes.is_prime(num):
            initial.append(num)
        else:
            for pos in Primes.fetch_primes(int(num**0.5), False):
                if num % pos == 0:
                    initial.append(pos)
                    Factors.prime_factors(num/pos, initial)
                    break
        return initial if not distinct else set(initial)
class Basic:
    def int_length(num: int) -> int:
        """Returns the length of a POSITIVE integer."""
        counter = 0
        while num > 0:
            num //= 10
            counter += 1
        return counter

if __name__ == "__main__":
    print(Primes.is_prime(9133))
    """inpt = int(input("Enter the number of which category you want to test:\n\t1. Primes\n"))
    from time import perf_counter
    if inpt == 1:
        start = perf_counter()
        Primes.fetch_primes(1000000000, True, True)
        print(f"Primes from 1 - 1,000,000,000 generated in {(((perf_counter() - start)*100000)//1)/100}ms")
        start = perf_counter()
        for num in range(1,1000000):
            Primes.is_prime(num)
        print(f"Checked if numbers 1 - 1,000,000 are prime in {(((perf_counter() - start)*100000)//1)/100}ms")
        start = perf_counter()
        for num_1 in range(1, 10000):
            for num_2 in range(1, 10000):
                Primes.is_coprime(num_1, num_2)
        print(f"Checked if numbers 1 - 10,000 and 1 - 10,000 are co-prime in {(((perf_counter() - start)*100000)//1)/100}ms")"""