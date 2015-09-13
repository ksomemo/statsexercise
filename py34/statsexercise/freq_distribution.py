import math


def sturges_rule(n):
    """スタージェスの公式

    度数分布の階級の個数を返す
    :param int n: データの個数
    """
    return math.log2(n) + 1
