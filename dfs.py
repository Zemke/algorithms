#!/usr/bin/env python3

import numpy as np


class Edge:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __repr__(self):
    return "Edge({},{})".format(self.x, self.y)

  @staticmethod
  def safe(grid, row_idx, col_idx):
    if row_idx < 0 or col_idx < 0:
      return None
    try:
      return grid[row_idx][col_idx]
    except IndexError:
      return None

    
  @staticmethod
  def neighbors(grid, row_idx, col_idx):
    nn = [
      Edge.safe(grid, row_idx+1, col_idx),
      Edge.safe(grid, row_idx-1, col_idx),
      Edge.safe(grid, row_idx, col_idx+1),
      Edge.safe(grid, row_idx, col_idx-1),
    ]
    return list(filter(lambda n: n is not None, nn))



M = np.array([['A', 'M'],
              ['G', 'E']])


def create_G(M):
  G = []
  for row_idx, row in enumerate(M):
    for col_idx, col in enumerate(M[row_idx]):
      m = M[row_idx][col_idx]
      nn = Edge.neighbors(M, row_idx, col_idx)
      for n in nn:
        G.append(Edge(m, n))
  return G


def adj(G, v):
  adj = []
  for w in G:
    if w.y == v:
      adj.append(w.x)
  return adj


def traverse_iter(G, v):
  S = [v]
  vv = []
  while len(S) > 0:
    v = S.pop()
    if v not in vv:
      vv.append(v)
      print(v, end=' ')
      for w in adj(G, v):
        S.append(w)


def traverse_rec(G, v, vv = []):
  for w in adj(G, v):
    if w not in vv:
      vv.append(w)
      print(w, end=' ')
      traverse_rec(G, w, vv)


print(M)
G = create_G(M)
print("G", G)
print('iter', end=': '); traverse_iter(G, G[0].x)
print()
print('rec', end=': '); traverse_rec(G, G[0].x)
print()

