import cProfile
import pstats

import helloworld as hw

PY_LOG_NAME = 'log_python.cprofile'
CY_LOG_NAME = 'log_cython.cprofile'

def say_hello(name):
    print('Hello World! Hello {}!'.format(name))


def cython_10k():
    for ii in range(0, 10000):
        hw.say_hello('Mircea')


def python_10k():
    for ii in range(0, 10000):
        say_hello('Mircea')


if __name__ == '__main__':
    cProfile.run('python_10k()', filename=PY_LOG_NAME)
    cProfile.run('cython_10k()', filename=CY_LOG_NAME)

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'python', '=' * 10))
    py_stats = pstats.Stats(PY_LOG_NAME)
    py_stats.print_stats()

    print('\n{}\n{}\n{}\n'.format('=' * 10, 'cython', '=' * 10))
    cy_stats = pstats.Stats(CY_LOG_NAME)
    cy_stats.print_stats()