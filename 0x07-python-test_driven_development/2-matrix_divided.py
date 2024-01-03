#!/usr/bin/python3
'''Implements a function that divides all elements of a matrix

The function supplied, matrix_divided(), for example:
    >>> print(matrix_divided([[1, 2], [5, 6]], 2))
    [[0.55, 1], [2.5, 3]]
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix and rounds them to 2 decimal places

    Args:
        matrix (:obj: `list` of :obj: `int` or  `float`): The specified matrix
        div (int or float): The divisor

    Returns:
        :obj: `list` of :obj: `list`: A new matrix

    Raises:
        TypeError: If matrix contains elements that are not int ot float
        If div is not an int or float
        ZeroDivisionError: If div is zero
    '''

    div_list = []

    if not is_matrix(matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                + " of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        div_list.append(list(round(num / div, 2) for num in row))

    return div_list


def is_matrix(matrix):
    '''Checks if the matrix meets all the set conditions

    Args:
        matrix (list): The matrix being evaluated

    Returns:
        bool: True if all conditions are satisfied otherwise
        false if any condition is not met
    '''

    if not isinstance(matrix, list):
        return False

    for row in matrix:
        if not isinstance(row, list):
            return False
        for n in row:
            if not isinstance(n, (int, float)):
                return False

    return True
