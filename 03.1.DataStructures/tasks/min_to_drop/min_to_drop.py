import typing as tp
from collections import Counter


def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    """
    :param seq: sequence of elements
    :return: number of elements need to drop to leave equal elements
    """
    cnt = Counter(seq)
    if len(seq) == 0:
        return 0
    else:
        return len(seq) - cnt.most_common()[0][1]
