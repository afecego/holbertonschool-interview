#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100"""

    if len(grid) > 100 or len(grid[0]) > 100:
        return ("Error")

    count = 0


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:

                if grid[i - 1][j] != 1:
                    count += 1

                if grid[i][j - 1] != 1:
                    count += 1

                if j + 1 > len(grid[i]) - 1 or grid[i][j + 1] != 1:
                    count += 1

                if i + 1 > len(grid) - 1 or grid[i + 1][j] != 1:
                    count += 1

    return count
