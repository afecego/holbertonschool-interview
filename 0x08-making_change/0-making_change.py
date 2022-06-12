#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    i, count = (0, 0)
    tmp = total
    leng = len(coins)

    while(i < leng and tmp > 0):
        if (tmp - coins[i]) >= 0:
            tmp -= coins[i]
            count += 1
        else:
            i += 1

    check = tmp > 0 and count > 0
    return -1 if check or count == 0 else count
