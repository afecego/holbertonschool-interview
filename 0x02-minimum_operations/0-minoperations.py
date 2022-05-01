#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste"""


def minOperations(n):
    """Given a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file."""

    result = 0
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            while n % i == 0:
                n = n / i
                result += i
        return result
