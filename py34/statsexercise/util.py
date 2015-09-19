import operator
import functools

def product(xs):
    """リストの積"""
    return functools.reduce(operator.mul, xs, 1)
