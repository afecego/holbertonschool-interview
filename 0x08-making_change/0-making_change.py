#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total"""

    if total <= 0:
        return 0

    if coins == [] or coins is None:
        return -1

    coins.sort(reverse=True)

    count = 0

    for i in coins:
        if total % i <= total:
            count += int(total / i)
            total = total % i

    return count if total == 0 else -1
