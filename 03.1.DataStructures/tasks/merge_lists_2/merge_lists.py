import typing as tp
import  heapq

def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    """
    :param seq: sequence of sorted sequences
    :return: merged sorted list
    """
    my_heap: tp.List[int] = []
    ans = []
    for i in seq:
        for j in i:
            heapq.heappush(my_heap, j)

    while len(my_heap) > 0:
        ans.append(heapq.heappop(my_heap))

    return ans
