import pytest
from statsexercise import mean


@pytest.mark.parametrize('xs, expected', [
    ([1, 2, 3], 2),
    ([1, 2], 1.5)
])
def test_mean(xs, expected):
    assert mean.mean(xs) == expected
