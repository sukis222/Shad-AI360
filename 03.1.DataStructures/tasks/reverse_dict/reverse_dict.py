import typing as tp
import collections

def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    """
    :param dct: dictionary to revert in format {key: value}
    :return: reverted dictionary {value: [key1, key2, key3]}
    """
    dct_2 = collections.defaultdict(list)
    for elem in dct:
        dct_2[dct[elem]].append(elem)

    return dict(dct_2)

