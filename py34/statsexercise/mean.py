from statsexercise.util import product


def mean(xs):
    """算術平均"""
    return sum(xs) / len(xs)


def median(xs):
    """中央値"""
    sorted_xs = sorted(xs)
    l = len(sorted_xs)
    r = l % 2
    q = l // 2
    if r == 1:
        return sorted_xs[q]
    return mean([sorted_xs[q - 1], sorted_xs[q]])

def harmonic_mean(xs):
    """調和平均"""
    return len(xs) / sum(1/x for x in xs)


def geometric_mean(xs):
    """幾何平均"""
    return product(xs) ** (1 / len(xs))
