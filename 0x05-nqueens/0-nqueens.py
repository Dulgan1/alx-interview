#!/usr/bin/python3
"""
 The N queens puzzle is the challenge of placing N non-attacking queens
 on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N

    If the user called the program with the wrong number of arguments, print
    Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1
    If N is smaller than 4, print N must be at least 4, followed by a new
    line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line

Format: see example

You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking

Example:

./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid
    """
    if 1 in board[row]:
        return False

    upper_diag = zip(range(row, -1, -1),
                     range(col, -1, -1))
    for i, j in upper_diag:
        if board[i][j] == 1:
            return False

    lower_diag = zip(range(row, len(board), 1),
                     range(col, -1, -1))
    for i, j in lower_diag:
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, col):
    """
    Helper function for nqueens
    """
    if col >= len(board):
        print_board(board, len(board))
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            result = nqueens_helper(board, col + 1)
            if result:
                return True
            board[i][col] = 0
    return False


def print_board(board, n):
    """
    Prints positions of the queens
    """
    b = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b.append([i, j])
    print(b)


def nqueens(n):
    """
    Finds all possible solutions to the n-queens problem
    """
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    nqueens_helper(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        exit(1)
    elif int(queens) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(queens))
