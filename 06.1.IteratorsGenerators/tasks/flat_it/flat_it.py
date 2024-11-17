from collections.abc import Iterable, Iterator
from typing import Any


def flat_it(sequence: Iterable[Any]) -> Iterator[Any]:
    """
    :param sequence: iterable with arbitrary level of nested iterables
    :return: generator producing flatten sequence
    """
    for elem in sequence:
        if hasattr(elem, '__iter__') and type(elem) != str:
            for num in flat_it(elem):
                yield num
        elif type(elem) == str:
            for let in elem:
                yield let
        else:
            yield elem
