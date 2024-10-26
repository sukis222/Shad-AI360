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
    for key, value in dct.items():
        if isinstance(value, dict):
            yield from traverse_dictionary(value)
        else:
            yield key, value


h = {"a": {"b": {"c": {"d": {"e": 1}}}}}
f = h
s = iter({"a": {"b": {"c": {"d": {"e": 1}}}}})



my_dict = {
    'key1': {'sub_key1': [1, 2, 3], 'sub_key2': [4, 5, 6]},
    'key2': {'sub_key3': [7, 8, 9], 'sub_key4': [10, 11, 12]},
    'deeper_level': {
        'sub_sub_key1': [{'inner_key': 'value'}, {'inner_key2': 'value2'}],
        'sub_sub_key2': ['a', 'b', 'c']
    }
}

# Функция для обхода словаря любой глубины
def traverse_dictionary(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            yield from traverse_dictionary(value)
        else:
            yield key, value

# Проходимся по всем элементам словаря
for element in traverse_dictionary(my_dict):
    print(element)



