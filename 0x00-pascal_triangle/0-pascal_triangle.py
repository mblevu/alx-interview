#!/usr/bin/python3
"""pascals triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: Pascal's triangle with n rows.

    Example:
        >>> pascal_triangle(5)
        [[1],
         [1, 1],
         [1, 2, 1],
         [1, 3, 3, 1],
         [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
