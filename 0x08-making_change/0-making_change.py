#!/usr/bin/python3
"""determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    if coins is None or coins is []:
        return -1

    new_coins = []
    coins.sort(reverse=True)
    for i in coins:
        new_coins.append(i)

    new = 0
    for j in new_coins:
        if total / j <= total:
            new += int(total / j)
            total = total % j
    if total == 0:
        return new
    else:
        return -1
