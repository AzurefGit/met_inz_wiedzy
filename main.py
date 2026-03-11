import numpy as np

from itertools import combinations


def exhaustive_alg(grid):
    for i in grid:
        print(i)



f = open("grid")
grid = f.read()
f.close()

rows = grid.split('\n')


grid = np.array(grid)
exhaustive_alg(rows)
# print(rows)