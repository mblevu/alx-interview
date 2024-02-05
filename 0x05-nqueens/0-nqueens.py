#!/usr/bin/python3
"""N Queens problem module
"""
import sys
from typing import List


def is_safe(board, row, col, n):
    """Checks if a queen can be placed on board at row, col
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board: List[List[int]], col: int, n: int) -> bool:
    """Solves the N Queens problem
    """
    if col == n:
        print_solution(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n) or res
            board[i][col] = 0
    return res


def print_solution(board):
    """Prints the solution to the N Queens problem
    """
    n = len(board)
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                res.append([i, j])
    print(res)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for j in range(n)] for i in range(n)]
    solve_nqueens(board, 0, n)
