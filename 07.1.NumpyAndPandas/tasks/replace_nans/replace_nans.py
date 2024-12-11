import numpy as np
import numpy.typing as npt


def replace_nans(matrix: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Replace all nans in matrix with average of other values.
    If all values are nans, then return zero matrix of the same size.
    :param matrix: matrix,
    :return: replaced matrix
    """
    nan_mask = ~np.isnan(matrix)
    if (nan_mask).sum() == 0 or matrix.size == 0:
        return np.zeros(matrix.shape)
    av = matrix[nan_mask].mean()
    print(av)
    return np.where(~nan_mask, av, matrix)

print(replace_nans(np.array([np.nan])))