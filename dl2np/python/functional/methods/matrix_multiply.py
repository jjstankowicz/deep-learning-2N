# Scratchpad:
# Not allowed:
# - for loops
# - while loops
# - list comprehensions
# - external libraries
#
# First draft:
# from typing import List, Union
# 
# TensorData = Union[int, float]
# Tensor1D = List[TensorData]
# Tensor2D = List[Tensor1D]
# 
# def matrix_multiply(matrix1: Tensor2D, matrix2: Tensor2D) -> Tensor2D:
#     if not matrix1 or not matrix2 or len(matrix1[0]) != len(matrix2):
#         raise ValueError("Invalid matrix dimensions for multiplication")
#     
#     def dot_product(row: Tensor1D, col: Tensor1D) -> TensorData:
#         return sum(map(lambda x, y: x * y, row, col))
#     
#     def get_column(matrix: Tensor2D, col_index: int) -> Tensor1D:
#         return list(map(lambda row: row[col_index], matrix))
#     
#     return list(map(
#         lambda row: list(map(
#             lambda col_index: dot_product(row, get_column(matrix2, col_index)),
#             range(len(matrix2[0]))
#         )),
#         matrix1
#     ))
#
# Improvements:
# - Add type hints for helper functions
# - Use more descriptive variable names
# - Split long lines for better readability

from typing import List, Union

TensorData = Union[int, float]
Tensor1D = List[TensorData]
Tensor2D = List[Tensor1D]

def dot_product(vector1: Tensor1D, vector2: Tensor1D) -> TensorData:
    """
    Compute the dot product of two vectors.
    
    Args:
        vector1 (Tensor1D): First vector
        vector2 (Tensor1D): Second vector
    
    Returns:
        TensorData: Dot product of the two vectors
    """
    return sum(map(lambda x, y: x * y, vector1, vector2))

def get_column(matrix: Tensor2D, col_index: int) -> Tensor1D:
    """
    Extract a column from a matrix.
    
    Args:
        matrix (Tensor2D): Input matrix
        col_index (int): Index of the column to extract
    
    Returns:
        Tensor1D: Extracted column
    """
    return list(map(lambda row: row[col_index], matrix))

def matrix_multiply(matrix1: Tensor2D, matrix2: Tensor2D) -> Tensor2D:
    """
    Perform matrix multiplication.
    
    Args:
        matrix1 (Tensor2D): First matrix
        matrix2 (Tensor2D): Second matrix
    
    Returns:
        Tensor2D: Result of matrix multiplication
    
    Raises:
        ValueError: If matrix dimensions are invalid for multiplication
    """
    if not matrix1 or not matrix2 or len(matrix1[0]) != len(matrix2):
        raise ValueError("Invalid matrix dimensions for multiplication")
    
    def multiply_row_by_matrix(row: Tensor1D) -> Tensor1D:
        return list(map(
            lambda col_index: dot_product(row, get_column(matrix2, col_index)),
            range(len(matrix2[0]))
        ))
    
    return list(map(multiply_row_by_matrix, matrix1))