import numpy as np
import numpy.typing as npt


def max_element(array: npt.NDArray[np.int_]) -> int | None:
    """
    Return max element before zero for input array.
    If appropriate elements are absent, then return None
    :param array: array,
    :return: max element value or None
    """
    zeroes = np.zeros(array.size, dtype="int32")
    mask = zeroes == array
    if (mask.sum() == 1 and mask[-1]) or mask.sum() == 0 or mask.size <= 1:
        return None


    return array[1:][mask[:-1]].max()

