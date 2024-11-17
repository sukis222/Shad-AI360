from collections.abc import Generator
from typing import Any


def transpose(matrix: list[list[Any]]) -> list[list[Any]]:
    """
    :param matrix: rectangular matrix
    :return: transposed matrix
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def uniq(sequence: list[Any]) -> Generator[Any, None, None]:
    """
    :param sequence: arbitrary sequence of comparable elements
    :return: generator of elements of `sequence` in
    the same order without duplicates
    """
    lll = []
    for i in range(len(sequence)):
        if sequence.count(sequence[i]) > 1:
            if lll.count(sequence[i]) == 0:
                lll.append(sequence[i])
        else:
            lll.append(sequence[i])
    return (i for i in lll)


def dict_merge(*dicts: dict[Any, Any]) -> dict[Any, Any]:
    """
    :param *dicts: flat dictionaries to be merged
    :return: merged dictionary
    """
    s = dict()
    for elem in dicts:
        for pod_elem in elem:
            s[pod_elem] = elem[pod_elem]

    return s


def product(lhs: list[int], rhs: list[int]) -> int:
    """
    :param rhs: first factor
    :param lhs: second factor
    :return: scalar product
    """
    return sum([lhs[i] * rhs[i] for i in range(len(lhs))])
