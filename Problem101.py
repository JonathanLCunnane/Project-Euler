from time import perf_counter
import numpy as np


def f(n: int):
    val = 0
    next = 1
    for i in range(11):
        if i % 2 == 0:
            val += next
        else:
            val -= next
        next *= n
    return val


def get_coeffs(val_list: list):
    n = len(val_list)
    val_matrix = np.array(val_list)
    inp_matrix = [[(row+1)**col for col in range(n)] for row in range(n)]
    inp_matrix = np.array(inp_matrix)
    inv_inp_matrix = np.linalg.inv(inp_matrix)
    coeffs = inv_inp_matrix.dot(val_matrix)
    return [round(coeff) for coeff in coeffs]


def fit(val_list: list): # First incorrect term where the first k terms are correct.
    coeffs = get_coeffs(val_list)
    fit_val_sum = 0
    n = len(val_list) + 1
    for pwr, coeff in enumerate(coeffs):
        fit_val_sum += coeff*(n**pwr)
    return fit_val_sum



start = perf_counter()

vals = [f(n) for n in range(1, 11)]
total_fit_sum = 0
for k in range(1, 11):
    total_fit_sum += fit(vals[:k])

end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"The sum of FITs for the BOPs for the given function is {total_fit_sum}.\nThis took {elapsed_ms}ms.")