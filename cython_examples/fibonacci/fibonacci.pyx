# MOD_LARGE_NUM = 1e9 + 7
MOD_LARGE_NUM = 1000000007

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


def fib_log(long long int n):
    """Computes nth fibonacci term in logarithmic time"""
    cdef long long int Aa, Ab, Ac, Ad
    cdef long long int An_a, An_b, An_c, An_d, MOD
    Aa, Ab, Ac, Ad = 1, 1, 1, 0
    An_a, An_b, An_c, An_d = 1, 0, 0, 1
    cnt = n
    MOD = 1000000007LL
    while cnt > 0:
        while cnt > 0 and cnt % 2 == 0:
            a, b, c, d = Aa, Ab, Ac, Ad
            new_a = ((a * a) % MOD + (b * c) % MOD) % MOD
            new_b = ((a * b) % MOD + (b * d) % MOD) % MOD
            new_c = ((a * c) % MOD + (c * d) % MOD) % MOD
            new_d = ((d * d) % MOD + (b * c) % MOD) % MOD
            Aa, Ab, Ac, Ad = new_a, new_b, new_c, new_d
            cnt /= 2
        while cnt % 2 == 1 and cnt > 0:
            a, b, c, d = Aa, Ab, Ac, Ad
            ma, mb, mc, md = An_a, An_b, An_c, An_d
            new_a = ((ma * a) % MOD + (mb * c) % MOD) % MOD
            new_b = ((ma * b) % MOD + (mb * d) % MOD) % MOD
            new_c = ((a * mc) % MOD + (c * md) % MOD) % MOD
            new_d = ((d * md) % MOD + (b * mc) % MOD) % MOD
            An_a, An_b, An_c, An_d = new_a, new_b, new_c, new_d
            cnt -= 1
    return An_c + An_d