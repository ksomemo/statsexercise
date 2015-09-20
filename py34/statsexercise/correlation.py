from statsexercise import mean


def cov(xs, ys):
    """共分散"""
    n = len(xs)
    avg_x = mean.mean(xs)
    avg_y = mean.mean(ys)
    xs = map(lambda x: x - avg_x, xs)
    ys = map(lambda x: x - avg_y, ys)

    return sum(x * y for x, y in zip(xs, ys)) / n
