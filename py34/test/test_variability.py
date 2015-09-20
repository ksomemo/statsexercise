import math
from statsexercise import variability


def test_ssd():
    xs = [2, 4, 6]
    assert variability.ssd(xs) == 8


def test_pvariance():
    xs = [2, 4, 6]
    assert variability.pvariance(xs) == 8/3


def test_pstdev():
    xs = [2, 4, 6]
    assert variability.pstdev(xs) == math.sqrt(8/3)


def test_variance():
    xs = [2, 4, 6]
    assert variability.variance(xs) == 8/2


def test_stdev():
    xs = [2, 4, 6]
    assert variability.stdev(xs) == math.sqrt(8/2)
