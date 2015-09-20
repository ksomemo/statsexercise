import math
from statsexercise import mean


def ssd(xs):
    """偏差平方和

    sum of squared deviation
    """
    avg = mean.mean(xs)
    return sum(map(lambda x: (x - avg) ** 2, xs))


def pvariance(xs):
    """母集団の分散"""
    return ssd(xs) / len(xs)


def pstdev(xs):
    """母集団の標準偏差"""
    return math.sqrt(pvariance(xs))


def variance(xs):
    """分散"""
    return ssd(xs) / (len(xs) - 1)


def stdev(xs):
    """標準偏差"""
    return math.sqrt(variance(xs))
