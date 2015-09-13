import math
from statsexercise import mean


def ssd(xs):
    """偏差平方和

    sum of squared deviation
    """
    avg = mean.mean(xs)
    return sum(map(lambda x: (x - avg) ** 2, xs))


def variance(xs):
    """分散"""
    return ssd(xs) / len(xs)


def sd(xs):
    """標準偏差

    standard deviation
    """
    return math.sqrt(variance(xs))
