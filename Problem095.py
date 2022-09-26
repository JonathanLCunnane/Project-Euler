from time import perf_counter


start = perf_counter()

def proper_divisors(n: int):
    divs = {1}
    for f in range(2, int(n**0.5) + 1):
        if n % f == 0:
            divs.update({f, n // f})
    return divs

upto = 1000000
found = {}
skip = set()
longest_chain = set()
longest_chain_length = 0
for n in range(1, upto+1):
    if n in skip:
        continue
    if n in found:
        divs = found[n]
    else:
        divs = proper_divisors(n)
        found[n] = divs
    chain = [n]
    while True:
        next_addition = sum(divs)
        if next_addition in skip or next_addition > upto:
            break
        if next_addition in chain:
            chain_len = len(chain) - chain.index(next_addition)
            if chain_len > longest_chain_length:
                longest_chain_length = chain_len
                longest_chain = chain[chain.index(next_addition):]
            #chain.append(next_addition)
            #print(chain, chain_len)
            break
        if next_addition == 1:
            #chain.append(next_addition)
            #print(chain)
            break
        chain.append(next_addition)
        if next_addition in found:
            divs = found[next_addition]
        else:
            divs = proper_divisors(next_addition)
    skip.update(chain)
    

end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The longest chain is: {longest_chain}\nIts length is: {longest_chain_length}\nThe smallest value in the chain is: {min(longest_chain)}\nThis took {elapsed_ms}ms.")