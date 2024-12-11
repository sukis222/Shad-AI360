import numpy as np
import numpy.typing as npt


def add_zeros(x: npt.NDArray[np.int_]) -> npt.NDArray[np.int_]:
    """
    Add zeros between values of given array
    :param x: array,
    :return: array with zeros inserted
    """
    x = x.reshape(-1, 1)
    nules = np.zeros((x.shape[0], 1), dtype='int32')
    x = np.concatenate([x, nules], axis=1)
    return x.reshape(-1)[:-1]

