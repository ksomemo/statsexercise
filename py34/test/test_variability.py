from statsexercise import variability


def test_ssd():
    xs = [2, 4, 6]
    assert variability.ssd(xs) == 8


def test_variance():
    xs = [2, 4, 6]
    assert variability.variance(xs) == 8/3


def test_sd():
    import math
    xs = [2, 4, 6]
    assert variability.sd(xs) == math.sqrt(8/3)
