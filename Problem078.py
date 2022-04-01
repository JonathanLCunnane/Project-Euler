from time import perf_counter


def generalised_pentagonal_numbers(upto: int) -> list:
    pentag = [1, 2]
    n = 2
    nneg = -2
    while pentag[-1] < upto:
        pentag.append(int((3*n**2-n)/2))
        pentag.append(int((3*nneg**2-nneg)/2))
        n += 1
        nneg -= 1
    return pentag


def partition_list(upto: int) -> list:
    """
    Returns a list where the index `n` is the value of `p(n)`
    """
    p = [0] * (upto + 1)
    p[0] = 1
    p[1] = 1
    pentags = generalised_pentagonal_numbers(upto)
    for n in range(2, upto + 1):
        currsum = 0
        k = 1
        for pentag in pentags:
            if pentag > n:
                break
            if k > 0:
                currsum += p[n-pentag]
                if k == 2:
                    k = -1
                    continue
            else:
                currsum -= p[n-pentag]
            k += 1

        p[n] = currsum
    return p


def main():
    upto = 60000
    index = -1
    start = perf_counter()
    p = partition_list(upto)
    for n in p:
        if n % 1000000 == 0:
            index = p.index(n)
            break
    end = perf_counter()
    elapsed_ms = (((end - start)*100000)//1)/100
    print(f"The value of n for which p(n) % 1mil = 0 is when n = {index}, and p(n) = {p[index]}.\nThis took {elapsed_ms}ms.")


if __name__ == "__main__":
    main()