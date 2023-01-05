from time import perf_counter
from math import log10

start_ms = perf_counter()

fnm1 = 1
fn = 1
n = 1
start_pan = False
end_pan = False
while log10(fn) < 8:
    fn, fnm1 = fn + fnm1, fn
    n += 1
while not (start_pan and end_pan):
    start_pan = False
    end_pan = False
    end = {char for char in str(fn%(10**9))}
    if "0" in end:
        fn, fnm1 = fn + fnm1, fn
        n += 1
        continue
    if len(end) == 9:
        end_pan = True
        start = {char for char in str(fn)[:9]}
        if "0" in start:
            fn, fnm1 = fn + fnm1, fn
            n += 1
            continue
        if len(start) == 9:
            start_pan = True
            print(n)
    fn, fnm1 = fn + fnm1, fn
    n += 1

end_ms = perf_counter()
elapsed_ms = (((end_ms - start_ms)*100000)//1)/100
print(f"The fibbonaci number which is 1-9 pandigital at the beginning and the end is at position {n}.\nThis number is: {fnm1}.\nThis took {elapsed_ms}ms.")