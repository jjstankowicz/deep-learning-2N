
# Scratchpad
# ----------------
# Define types for better readability
# TensorData = Union[int, float]
# Tensor1D = List[TensorData]
# Tensor2D = List[List[TensorData]]

# Define a function to get the number of rows in a matrix
# def num_rows(matrix: Tensor2D) -> int:
#     return len(matrix)

# Define a function to get the number of columns in a matrix
# def num_cols(matrix: Tensor2D) -> int:
#     return len(matrix[0]) if matrix else 0

# Define a function to get a column from a matrix
# def get_column(matrix: Tensor2D, col_index: int) -> Tensor1D:
#     return list(map(lambda row: row[col_index], matrix))

# Define a function to multiply two matrices
# def matrix_multiply(matrix1: Tensor2D, matrix2: Tensor2D) -> Tensor2D:
#     if num_cols(matrix1) != num_rows(matrix2):
#         raise ValueError("Incompatible matrices for multiplication")
#     return list(map(lambda row: list(map(lambda col: sum(map(lambda x, y: x * y, row, col)), 
#                                          map(lambda j: get_column(matrix2, j), range(num_cols(matrix2))))), 
#                     matrix1))

from typing import List, Union

TensorData = Union[int, float]
Tensor1D = List[TensorData]
Tensor2D = List[List[TensorData]]

def num_rows(matrix: Tensor2D) -> int:
    """Returns the number of rows in a matrix."""
    return len(matrix)

def num_cols(matrix: Tensor2D) -> int:
    """Returns the number of columns in a matrix."""
    return len(matrix[0]) if matrix else 0

def get_column(matrix: Tensor2D, col_index: int) -> Tensor1D:
    """Returns a specific column from a matrix."""
    return list(map(lambda row: row[col_index], matrix))

def matrix_multiply(matrix1: Tensor2D, matrix2: Tensor2D) -> Tensor2D:
    """
    Multiplies two matrices using pure functions.
    
    Args:
        matrix1 (Tensor2D): The first matrix.
        matrix2 (Tensor2D): The second matrix.
    
    Returns:
        Tensor2D: The result of the matrix multiplication.
    
    Raises:
        ValueError: If the matrices cannot be multiplied due to incompatible dimensions.
    """
    if num_cols(matrix1) != num_rows(matrix2):
        raise ValueError("Incompatible matrices for multiplication")
    
    return list(map(lambda row: list(map(lambda col: sum(map(lambda x, y: x * y, row, col)), 
                                         map(lambda j: get_column(matrix2, j), range(num_cols(matrix2))))), 
                    matrix1))
