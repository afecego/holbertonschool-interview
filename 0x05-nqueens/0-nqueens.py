#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard"""
import sys


def nonAttack(sol, ln, i):
    """"""
    for j in range(ln):
        if(sol[j] == i or sol[j] + ln - j == i or sol[j] + j - ln == i):
            return False
    return True


def nextSafe(sol, ln):
    """"""
    for i in range(len(sol)):
        if nonAttack(sol, ln, i):
            sol[ln] = i
            if ln < len(sol) - 1:
                nextSafe(sol, ln + 1)
            else:
                result = []
                for i in range(len(sol)):
                    a = [i, sol[i]]
                    result.append(a)
                print (result)


if len(sys.argv) != 2:
    print ('Usage: nqueens N\n')
    sys.exit(1)
else:
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number\n')
        sys.exit(1)
    if type(n) is not int:
        print('N must be a number\n')
        sys.exit(1)
    if n < 4:
        print ('N must be at least 4\n')
        sys.exit(1)
    else:
        sol = []
        for i in range(n):
            sol.append(i)
        nextSafe(sol, 0)
