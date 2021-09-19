#!/usr/bin/env python3

import numpy as np


def safe(grid, row_idx, col_idx):
  if (row_idx >= 0 and row_idx < len(grid)
      and col_idx >= 0 and col_idx < len(grid[row_idx])):
    return grid[row_idx][col_idx]
  return None


def neighbors(grid, row_idx, col_idx):
  nn = {
    safe(grid, row_idx+1, col_idx): (row_idx+1, col_idx),
    safe(grid, row_idx-1, col_idx): (row_idx-1, col_idx),
    safe(grid, row_idx, col_idx+1): (row_idx, col_idx+1),
    safe(grid, row_idx, col_idx-1): (row_idx, col_idx-1),
  }
  if None in nn:
    del nn[None]
  return nn


M = np.array([['A', 'M'],
              ['G', 'E']], dtype=object)
print(M)


def do(M, m, row_idx, col_idx, size, W=''):
  nn = neighbors(M, row_idx, col_idx)
  for n_idx, n_tuple in enumerate(nn.items()):
    n_row_idx, n_col_idx = n_tuple[1]
    mod_M = np.copy(M)
    mod_M[row_idx][col_idx] = None
    mod_M[n_row_idx][n_col_idx] = None
    n = n_tuple[0]
    candidate = W + m + n
    if len(candidate) == size:
      print("done", candidate)
    else:
      do(mod_M, n, n_row_idx, n_col_idx, size, W + m)


for row_idx, row in enumerate(M):
  for col_idx, m in enumerate(M[row_idx]):
    do(M, m, row_idx, col_idx, M.size)

