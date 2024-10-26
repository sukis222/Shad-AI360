import typing as tp


def traverse_dictionary_immutable(
        dct: tp.Mapping[str, tp.Any],
        prefix: str = "") -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param prefix: prefix for key used for passing total path through recursion
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    ans = []
    for elem in dct:
        if not isinstance(dct[elem], dict):
            ans.append((elem, dct[elem]))
        else:
            micro_ans = traverse_dictionary_immutable(dct[elem])
            for el in micro_ans:
                ans.append((f'{elem}.{el[0]}', el[1]))
    return ans



def traverse_dictionary_mutable(
        dct: tp.Mapping[str, tp.Any],
        result: list[tuple[str, int]],
        prefix: str = "") -> None:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :param result: list with pairs: (full key from root to leaf joined by ".", value)
    :param prefix: prefix for key used for passing total path through recursion
    :return: None
    """
    for elem in dct:
        if not isinstance(dct[elem], dict):
            result.append((elem, dct[elem]))
        else:
            micro_ans = traverse_dictionary_immutable(dct[elem])
            for el in micro_ans:
                result.append((f'{elem}.{el[0]}', el[1]))


def traverse_dictionary_iterative(
        dct: tp.Mapping[str, tp.Any]
        ) -> list[tuple[str, int]]:
    """
    :param dct: dictionary of undefined depth with integers or other dicts as leaves with same properties
    :return: list with pairs: (full key from root to leaf joined by ".", value)
    """
    ans = []
    for elem in dct:
        if not isinstance(dct[elem], dict):
            ans.append((elem, dct[elem]))
        else:
            micro_ans = traverse_dictionary_immutable(dct[elem])
            for el in micro_ans:
                ans.append((f'{elem}.{el[0]}', el[1]))
    return ans

