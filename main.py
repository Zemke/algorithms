#!/usr/bin/env python3

import numpy as np
from sys import exit


def safe(grid, row_idx, col_idx):
  if row_idx < 0 or col_idx < 0:
    return None
  try:
    return grid[row_idx][col_idx]
  except IndexError:
    return None


def neighbors(grid, row_idx, col_idx):
  nn = {
    safe(grid, row_idx+1, col_idx): (row_idx+1, col_idx),
    safe(grid, row_idx-1, col_idx): (row_idx-1, col_idx),
    safe(grid, row_idx, col_idx+1): (row_idx, col_idx+1),
    safe(grid, row_idx, col_idx-1): (row_idx, col_idx-1),
  }
  del nn[None]
  return nn


M = np.array([['A', 'M'],
              ['G', 'E']], dtype=object)
print(M)


def do(M, size, W=''):
  for row_idx, row in enumerate(M):
    for col_idx, m in enumerate(M[row_idx]):
      if m is None:
        continue
      nn = neighbors(M, row_idx, col_idx)
      ww = [m] * len(nn)
      for n_idx, n_tuple in enumerate(nn.items()):
        n = n_tuple[0]
        n_row_idx, n_col_idx = n_tuple[1]
        ww[n_idx] += n
        mod_M = np.copy(M)
        mod_M[row_idx][col_idx] = None
        mod_M[n_row_idx][n_col_idx] = None
        print(ww[n_idx])
        print(mod_M)
        if np.count_nonzero(mod_M == None) == size:
          print("done", W + ww[n_idx])
        else:
          print("no")
          do(mod_M, size, ww[n_idx] + W)


do(M, M.size)

