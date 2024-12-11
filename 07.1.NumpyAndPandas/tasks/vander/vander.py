import numpy as np
import numpy.typing as npt


def vander(array: npt.NDArray[np.float64 | np.int_]) -> npt.NDArray[np.float64]:
    """
    Create a Vandermod matrix from the given vector.
    :param array: input array,
    :return: vandermonde matrix
    """
    ones = np.ones((array.shape[0]))

    array = array.reshape((-1, 1))
    array = array * ones
    st = np.arange(0, ones.size)
    return array ** st

