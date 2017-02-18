MOD_LARGE_NUM = 1e9 + 7

def fib(n):
    a, b = 0, 1
    step = 0
    while step < n:
        a, b = b, (a + b) % MOD_LARGE_NUM
        step += 1
    return b

def fib_types(long long int n):
    cdef long long int a, b, f3, step
    cdef long long int modulo
    modulo = 1000000007LL
    a = 0
    b = 1
    step = 0
    while step < n:
        f3 = (a + b) % modulo
        a = b
        b = f3
        step += 1
    return b