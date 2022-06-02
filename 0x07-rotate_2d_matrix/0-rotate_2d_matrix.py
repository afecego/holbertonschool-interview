#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """The matrix must be edited in-place"""
    row = len(matrix)

    for j in range(row):
        col_row = []
        for i in matrix:
            a = i[j]
            col_row.append(a)
        col_row.reverse()
        matrix[j] = col_row
