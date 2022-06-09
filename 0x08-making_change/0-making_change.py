#!/usr/bin/python3
"""determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    if coins is None:
        return -1

    coins.sort(reverse=True)

    new = 0
    for i in coins:
        if total / i <= total:
            new += int(total / i)
            total = total % i
    if total == 0:
        return new
    return -1
