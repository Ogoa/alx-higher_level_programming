#!/usr/bin/python3
# Computes the square values of all integers of a matrix
def square_matrix_simple(matrix=[]):
    squares = []
    for x in matrix:
        squares.append(list(map(lambda i: (i * i), x)))
    return squares


if __name__ == "__main__":
    square_matrix_simple(matrix)
