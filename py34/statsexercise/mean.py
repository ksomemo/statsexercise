def mean(xs):
    """算術平均"""
    return sum(xs) / len(xs)


def median(xs):
    """中央値"""
    l = len(xs)
    r = l % 2
    q = l // 2
    if r == 1:
        return xs[q]
    return mean([xs[q - 1], xs[q]])
