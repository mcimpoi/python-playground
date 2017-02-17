import cProfile
import pstats

import fibonacci

PY_LOG_NAME = 'log_python.cprofile'
CY_LOG_NAME = 'log_cython.cprofile'

MOD_LARGE_NUM = 1e9 + 7
FIB_IDX = 9000000


def sanity_check():
    for ii in range(100):
        assert(fibonacci.fib(ii) == pyfib(ii))


def pyfib(n):
    a, b = 0, 1
    step = 0
    while step < n:
        a, b = b, (a + b) % MOD_LARGE_NUM
        step += 1
    return b


def cython():
    print(fibonacci.fib(FIB_IDX))


def python():
    print(pyfib(FIB_IDX))


if __name__ == '__main__':
    cProfile.run('python()', filename=PY_LOG_NAME)
    cProfile.run('cython()', filename=CY_LOG_NAME)

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'python', '=' * 10))
    py_stats = pstats.Stats(PY_LOG_NAME)
    py_stats.print_stats()

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'cython', '=' * 10))
    cy_stats = pstats.Stats(CY_LOG_NAME)
    cy_stats.print_stats()