def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    s = []
    i = 0
    j = 0
    while i < len(lst_a) or j < len(lst_b):
        if i == len(lst_a):
            s.append(lst_b[j])
            j += 1
            continue
        elif j == len(lst_b):
            s.append(lst_a[i])
            i += 1
            continue

        if lst_a[i] < lst_b[j]:
            s.append(lst_a[i])
            i += 1
        else:
            s.append(lst_b[j])
            j += 1
    return s


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    """
    Merge two sorted lists in one sorted list using `sorted`
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: merged sorted list
    """
    return sorted(lst_a + lst_b)
