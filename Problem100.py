from time import perf_counter

# ((n+1)n)/((m+1)m) = 1/2
# ((m+1)m)/((n+1)n) = 2
# 1/2*m(m+1) = 2*1/2*n(n+1)
# 4m^2+4m = 8n^2+n
# 4m^2+4m+2= 8n^2+n+2
# (2m+1)^2 + 1 = 2(2n+1)^2
# (2m+1)^2 - 2(2n+1)^2 = -1
# Let x = 2m+1, y = 2n+1
# x^2 - 2y^2 = -1, which is a variation of a Pells equation where n=2.
# (x - sqrt(2)y)(x + sqrt(2)y) = -1
# In this case the fundamental solution is x_1 = 1, y_1 = 1.
# Hence:
# x_k+1 = 3*x_k + 4*y_k
# y_k+1 = 3*y_k + 2*x_k


start = perf_counter()
upto = 10**12
x_1 = 1
y_1 = 1
x_k = 1
y_k = 1
m = 0
n = 0
while m + 1 < upto:
    x_kp = 3*x_k + 4*y_k
    y_kp = 3*y_k + 2*x_k
    m = (x_kp - 1)/2
    n = (y_kp - 1)/2
    x_k = x_kp
    y_k = y_kp

end = perf_counter()
elapsed_ms = (((end - start)*100000)//1)/100
print(f"{int(n + 1):,} blue discs and {int(m + 1):,} total discs.\nThis took {elapsed_ms}ms.")