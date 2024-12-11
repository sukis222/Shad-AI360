import numpy as np
import numpy.typing as npt


def nonzero_product(matrix: npt.NDArray[np.int_]) -> int | None:
    """
    Compute product of nonzero diagonal elements of matrix
    If all diagonal elements are zeros, then return None
    :param matrix: array,
    :return: product value or None
    """

    E = np.eye(max(matrix.shape[1], matrix.shape[0]))
    mask = E == 1
    mask = mask[:matrix.shape[0], :matrix.shape[1]]
    print(mask)

    sq_mat = matrix[mask]
    new_mask = sq_mat != 0
    if new_mask.sum() == 0:
        return None
    else:
        return sq_mat[new_mask].prod()



X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
print(nonzero_product(X))