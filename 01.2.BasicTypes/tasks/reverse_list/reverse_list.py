def reverse_iterative(lst: list[int]) -> list[int]:
    lst2 = []
    for j in range(len(lst) - 1, -1, -1):
        lst2.append(lst[j])
    return lst2


def reverse_inplace_iterative(lst: list[int]) -> None:
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1


def reverse_inplace(lst: list[int]) -> None:
    lst.reverse()


def reverse_reversed(lst: list[int]) -> list[int]:
    return list(reversed(lst))


def reverse_slice(lst: list[int]) -> list[int]:
    return lst[::-1]
