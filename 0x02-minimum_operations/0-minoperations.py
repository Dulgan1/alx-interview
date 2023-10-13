#!/usr/bin/env python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result in exactly n H characters
in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH
=> Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6"""


def minOperations(n):
    """Method implements conditions above"""
    op = 0

    if n <= 1:
        return op

    for i in range(2, n + 1):
        while (n % i == 0):
            op = op + i
            n = n / i
            if n < i:
                break
    return op
