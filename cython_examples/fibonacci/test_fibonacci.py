import cProfile
import pstats

import fibonacci
from python_smart import fib_log

PY_LOG_NAME = 'log_python.cprofile'
CY_LOG_NAME = 'log_cython.cprofile'
CY_LOG_NAME2 = 'log_cython2.cprofile'
CY_LOG_NAME3 = 'log_cython3.cprofile'
PY_LOG_LOG = 'log_py_logarithmic.cprofile'

MOD_LARGE_NUM = 1e9 + 7

FIB_IDX = 9223372036854775  # 2^63 - 5 / 1000


def sanity_check():
    for ii in range(200):
        print fibonacci.fib_types(ii), fibonacci.fib(ii), fib_log(ii)


def pyfib(n):
    a, b = 0, 1
    step = 0
    while step < n:
        a, b = b, (a + b) % MOD_LARGE_NUM
        step += 1
    return b


def cython():
    print(fibonacci.fib(FIB_IDX))


def cython2():
    print(fibonacci.fib_types(FIB_IDX))


def cython3():
    print(fibonacci.fib_log(FIB_IDX))

def python():
    print(pyfib(FIB_IDX))


def logarithmic_py():
    print(fib_log(FIB_IDX))


if __name__ == '__main__':
    sanity_check()
    # cProfile.run('python()', filename=PY_LOG_NAME)
    # cProfile.run('cython()', filename=CY_LOG_NAME)
    cProfile.run('cython2()', filename=CY_LOG_NAME2)
    cProfile.run('cython3()', filename=CY_LOG_NAME3)

    cProfile.run('logarithmic_py()', filename=PY_LOG_LOG)

    # print('\n{}\n{}\n{}\n'.format('=' * 10, 'python', '=' * 10))
    # py_stats = pstats.Stats(PY_LOG_NAME)
    # py_stats.print_stats()

    # print('\n{}\n{}\n{}\n'.format('=' * 10, 'cython', '=' * 10))
    # cy_stats = pstats.Stats(CY_LOG_NAME)
    # cy_stats.print_stats()

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'cython2', '=' * 10))
    cy_stats2 = pstats.Stats(CY_LOG_NAME2)
    cy_stats2.print_stats()

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'pylog', '=' * 10))
    py_stats2 = pstats.Stats(PY_LOG_LOG)
    py_stats2.print_stats()

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'cylog', '=' * 10))
    py_stats3 = pstats.Stats(CY_LOG_NAME3)
    py_stats3.print_stats()
