#!/usr/bin/python3
# Computes the square values of all integers of a matrix
def square_matrix_simple(matrix=[]):
    return list(list(map(lambda x: (x * x), row)) for row in matrix)


if __name__ == "__main__":
    square_matrix_simple(matrix)
