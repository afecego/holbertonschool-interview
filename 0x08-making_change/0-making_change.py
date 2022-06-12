#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given
amount total"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    count = 0

    for i in coins:
        if total % i == 0:
            count += int(total / i)
            return count

        if total - 1 >= 0:
            if int(total / i) > 1:
                count += int(total / i)
                total = total % i
            else:
                count += 1
                total -= i
                if total == 0:
                    break

    if total == 0:
        return count
    else:
        return -1
