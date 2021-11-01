#!/usr/bin/env python

from math import inf


class TTT:
  DEPTH = 9

  def __init__(self, board=None, player=1):
    self.p = player
    if board is None:
      self.board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
      ]
    else:
      self.board = board

  def moves(self):
    mm = []
    for ri in range(len(self.board)):
      for ci in range(len(self.board[ri])):
        if self.board[ri][ci] == 0:
          mm.append((ri, ci))
    return mm

  def move(self, m):
    if m not in self.moves():
      raise Exception("invalid move")
    b = [[*self.board[0]], [*self.board[1]], [*self.board[2]]]
    b[m[0]][m[1]] = self.p
    return TTT(b, ((self.p-1)^1)+1)

  def terminal(self):
    b = self.board
    ln = [[b[0][0], b[1][1], b[2][2]],  # diagonals
          [b[0][2], b[1][1], b[2][0]],

          [b[0][0], b[0][1], b[0][2]],  # rows
          [b[1][0], b[1][1], b[1][2]],
          [b[2][0], b[2][1], b[2][2]],

          [b[0][0], b[1][0], b[2][0]],  # cols
          [b[0][1], b[1][1], b[2][1]],
          [b[0][2], b[1][2], b[2][2]]]
    for ln1 in ln:
      for p in [1,2]:
        if [p] * 3 == ln1:
          return p
    for row in b:
      for p in row:
        if p == 0:
          return -1  # still moves to make
    return 0  # draw

  def diff(self, o):
    diffs = []
    for ri in range(len(self.board)):
      for ci in range(len(self.board[ri])):
        oc = o.board[ri][ci]
        if oc != self.board[ri][ci]:
          diffs.append(((ri, ci), oc))
    return diffs

  @staticmethod
  def mx_heuristic(terminal, maxim): 
    if terminal == -1:
      raise Exception("heuristic must only be called on terminal states")
    return 0 if terminal == 0 else -inf if maxim else inf

  def __repr__(self):
    s = ""
    for row in self.board:
      s += str(row) + "\n"
    return s.strip()

  def __eq__(self, o):
    return (isinstance(o, TTT)
           and o.board == self.board
           and o.p == self.p)

  def __hash__(self):
    return hash((self.board, self.p))

  def __gt__(self, o):
    return len(self.moves()) > len(o.moves())


def minimax(node, depth, maxim, heuristic, acc=None):
  terminal = node.terminal()
  if depth == 0 or terminal != -1:
    v = heuristic(terminal, maxim)
    acc[depth].append((v, node))
    return v
  if maxim:
    v = -inf
    for m in node.moves():
      v = max(minimax(node.move(m), depth-1, False, heuristic, acc), v)
  else:
    v = +inf
    for m in node.moves():
      v = min(minimax(node.move(m), depth-1, True, heuristic, acc), v)
  acc[depth].append((v, node))
  return v


t = TTT()
while t.terminal() == -1:
  try:
    print(f"{t}\n")
    if t.p == 1:
      print("you: ", end='')
      m = tuple([int(i) for i in input()])
      t = t.move(m)
    else:
      acc = [[] for _ in range(TTT.DEPTH+1)]
      mx = minimax(t, TTT.DEPTH, True, TTT.mx_heuristic, acc)
      nx = max(acc[TTT.DEPTH-1])
      diff = t.diff(nx[1])
      if len(diff) > 1:
        raise Exception("More than one move has been done")
      m = diff[0][0]
      print(f"opp: {''.join([str(i) for i in m])}")
      t = t.move(m)
  except Exception as e:
    print(e)

print(t)
print('winner ', t.terminal())

