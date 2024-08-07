# Scratchpad
# Let's start by working out some simple matrix multiplication examples:
#
# 1. Identity matrix (2x2) * Random matrix (2x2)
# [[1, 0],   [[a, b],    [[a, b],
#  [0, 1]] *  [c, d]] =   [c, d]]
#
# 2. Simple 2x2 matrices
# [[1, 2],   [[5, 6],    [[1*5 + 2*7, 1*6 + 2*8],     [[19, 22],
#  [3, 4]] *  [7, 8]] =   [3*5 + 4*7, 3*6 + 4*8]] =    [43, 50]]
#
# Now, let's draft our test code:
#
# import pytest
# from typing import List, Union
#
# def compare_nested_lists(list1, list2, tolerance=1e-6):
#     if isinstance(list1, (int, float)) and isinstance(list2, (int, float)):
#         return abs(list1 - list2) < tolerance
#     return all(compare_nested_lists(l1, l2, tolerance) for l1, l2 in zip(list1, list2))
#
# def test_matrix_multiply():
#     # Test with integer matrices
#     matrix1 = [[1, 2], [3, 4]]
#     matrix2 = [[5, 6], [7, 8]]
#     expected = [[19, 22], [43, 50]]
#     assert matrix_multiply(matrix1, matrix2) == expected
#
#     # Test with float matrices
#     matrix1 = [[1.0, 2.0], [3.0, 4.0]]
#     matrix2 = [[5.0, 6.0], [7.0, 8.0]]
#     expected = [[19.0, 22.0], [43.0, 50.0]]
#     assert compare_nested_lists(matrix_multiply(matrix1, matrix2), expected)
#
#     # Test with mixed int and float matrices
#     matrix1 = [[1, 2.0], [3, 4.0]]
#     matrix2 = [[5.0, 6], [7.0, 8]]
#     expected = [[19.0, 22.0], [43.0, 50.0]]
#     assert compare_nested_lists(matrix_multiply(matrix1, matrix2), expected)
#
#     # Test with identity matrix
#     identity = [[1, 0], [0, 1]]
#     random_matrix = [[2, 3], [4, 5]]
#     assert matrix_multiply(identity, random_matrix) == random_matrix
#
#     # Test invalid dimensions
#     with pytest.raises(ValueError):
#         matrix_multiply([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
#
# The draft looks good, but we should add a test for empty matrices and ensure we're testing all the main functions.
# Let's write the final code:

import pytest
from typing import List, Union
from matrix_multiply import dot_product, get_column, matrix_multiply

TensorData = Union[int, float]
Tensor1D = List[TensorData]
Tensor2D = List[Tensor1D]


def compare_nested_lists(list1, list2, tolerance=1e-6):
    if isinstance(list1, (int, float)) and isinstance(list2, (int, float)):
        return abs(list1 - list2) < tolerance
    return all(compare_nested_lists(l1, l2, tolerance) for l1, l2 in zip(list1, list2))


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert compare_nested_lists(dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]), 32.0)
    assert compare_nested_lists(dot_product([1, 2.0, 3], [4.0, 5, 6.0]), 32.0)


def test_get_column():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert get_column(matrix, 0) == [1, 4, 7]
    assert get_column(matrix, 1) == [2, 5, 8]
    assert get_column(matrix, 2) == [3, 6, 9]


def test_matrix_multiply():
    # Test with integer matrices
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert matrix_multiply(matrix1, matrix2) == expected

    # Test with float matrices
    matrix1 = [[1.0, 2.0], [3.0, 4.0]]
    matrix2 = [[5.0, 6.0], [7.0, 8.0]]
    expected = [[19.0, 22.0], [43.0, 50.0]]
    assert compare_nested_lists(matrix_multiply(matrix1, matrix2), expected)

    # Test with mixed int and float matrices
    matrix1 = [[1, 2.0], [3, 4.0]]
    matrix2 = [[5.0, 6], [7.0, 8]]
    expected = [[19.0, 22.0], [43.0, 50.0]]
    assert compare_nested_lists(matrix_multiply(matrix1, matrix2), expected)

    # Test with identity matrix
    identity = [[1, 0], [0, 1]]
    random_matrix = [[2, 3], [4, 5]]
    assert matrix_multiply(identity, random_matrix) == random_matrix

    # Test invalid dimensions
    with pytest.raises(ValueError):
        matrix_multiply([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])

    # Test empty matrices
    with pytest.raises(ValueError):
        matrix_multiply([], [])
