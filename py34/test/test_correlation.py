from statsexercise import correlation as cor


def test_cov():
    xs = [50, 50, 80, 70, 90]
    ys = [50, 70, 60, 90, 100]
    assert cor.cov(xs, ys) == 188
