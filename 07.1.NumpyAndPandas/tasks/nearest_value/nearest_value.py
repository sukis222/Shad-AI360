import numpy as np
import numpy.typing as npt


def nearest_value(matrix: npt.NDArray[np.float64], value: float) -> float | None:
    """
    Find nearest value in matrix.
    If matrix is empty return None
    :param matrix: input matrix
    :param value: value to find
    :return: nearest value in matrix or None
    """
    if matrix.size == 0:
        return None
    mat = abs(matrix - value)

    mim = mat.min()
    mim_mass = np.ones(matrix.shape) * mim

    min_bool = mim_mass == mat

    return matrix[min_bool].max()

