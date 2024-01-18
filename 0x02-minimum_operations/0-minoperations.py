#!/usr/bin/env python3
"""the goal is to find the minimum number of operations
needed to create exactly n 'H' characters in a text file"""


def minOperations(n):
    """Calculate the minimum number of operations required to reach a target number.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations.

    """
    if n <= 1:
        return 0
    min_ops = float('inf')

    for i in range(2, n + 1):
        if n % i == 0:
            operations = minOperations(i) + n // i
            min_ops = min(min_ops, operations)
    return min_ops