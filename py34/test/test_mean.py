import pytest
from statsexercise import mean


@pytest.mark.parametrize('xs, expected', [
    ([1, 2, 3], 2),
    ([1, 2], 1.5)
])
def test_mean(xs, expected):
    assert mean.mean(xs) == expected


@pytest.mark.parametrize('xs, expected', [
    ([1, 2, 3, 5], 2.5),
    ([1, 2, 5], 2),
    ([2, 1, 3, 5], 2.5),
    ([2, 1, 5], 2),
])
def test_median(xs, expected):
    assert mean.median(xs) == expected


def test_harmonic_mean():
    assert mean.harmonic_mean([1, 2, 4]) == 12 / 7
