from statsexercise import freq_distribution as fd


def test_sturges_rule():
    assert fd.sturges_rule(8) == 4
