MOD = 1000000007


def fib_log(n):
    """Computes nth fibonacci term in logarithmic time"""
    mat_A = [1, 1, 1, 0]
    mat_A_n = [1, 0, 0, 1]
    cnt = n
    while cnt > 0:
        while cnt > 0 and cnt % 2 == 0:
            a = mat_A[0]
            b = mat_A[1]
            c = mat_A[2]
            d = mat_A[3]
            new_a = ((a * a) % MOD + (b * c) % MOD) % MOD
            new_b = ((a * b) % MOD + (b * d) % MOD) % MOD
            new_c = ((a * c) % MOD + (c * d) % MOD) % MOD
            new_d = ((d * d) % MOD + (b * c) % MOD) % MOD
            mat_A = [new_a, new_b, new_c, new_d]
            cnt /= 2
        while cnt % 2 == 1 and cnt > 0:
            ma, a = mat_A_n[0], mat_A[0]
            mb, b = mat_A_n[1], mat_A[1]
            mc, c = mat_A_n[2], mat_A[2]
            md, d = mat_A_n[3], mat_A[3]
            new_a = ((ma * a) % MOD + (mb * c) % MOD) % MOD
            new_b = ((ma * b) % MOD + (mb * d) % MOD) % MOD
            new_c = ((a * mc) % MOD + (c * md) % MOD) % MOD
            new_d = ((d * md) % MOD + (b * mc) % MOD) % MOD
            mat_A_n = [new_a, new_b, new_c, new_d]
            cnt -= 1
    return (mat_A_n[2] + mat_A_n[3]) % MOD
