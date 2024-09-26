def filter_list_by_list(lst_a: list[int] | range, lst_b: list[int] | range) -> list[int]:
    """
    Filter first sorted list by other sorted list
    :param lst_a: first sorted list
    :param lst_b: second sorted list
    :return: filtered sorted list
    """
    s = []
    i = 0
    j = 0
    while i < len(lst_a) or j < len(lst_b):
        if i == len(lst_a):
            break
        elif j == len(lst_b):
            s.append(lst_a[i])
            i += 1
            continue

        if lst_a[i] == lst_b[j]:
            i += 1
            j += 1
        elif lst_a[i] < lst_b[j]:
            s.append(lst_a[i])
            i += 1
        elif lst_a[i] > lst_b[j]:
            j += 1
    return s
