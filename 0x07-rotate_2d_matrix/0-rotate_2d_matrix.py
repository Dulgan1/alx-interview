#!/usr/bin/python3
"""
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
        Prototype: def rotate_2d_matrix(matrix):
        Do not return anything. The matrix must be edited in-place.
        You can assume the matrix will have 2 dimensions and will not be
        empty.
"""


def rotate_2d_matrix(matrix):
    """Implements rotate_2d_matrix"""
    n = len(matrix)
    index = n - 1

    for i in range(int(n / 2)):
        for j in range(i, index - i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[index - j][i]
            matrix[index - j][i] = matrix[index - i][index - j]
            matrix[index - i][index - j] = matrix[j][index - i]
            matrix[j][index - i] = temp
