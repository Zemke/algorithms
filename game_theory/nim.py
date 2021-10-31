#!/usr/bin/env python3

import os


S = [2, 3, 5, 7, 11, 13]
D = [0, 1, 4, 6, 8, 9, 10, 12]  # if any of that's left, then opponent dead


def dead_end(A):
  """
  If the buckets A are in state where the game cannot be continued.
  """
  for a in A:
    if a != 1 and a != 0:
      return False
  return True

def can_dead_end(A):
  for s in S:
    for A_idx, a in enumerate(A):
      mod_A = [*A]
      mod_A[A_idx] = (mod_A[A_idx] - s)
      if dead_end(mod_A):
        return True
  return False


def winner(A, player_a = True, winners = [], top_level = True):  # [10, 10]
  # I'm the winner if I can dead-end.
  if can_dead_end(A):
    winners.append("a" if player_a else "b")
    return
  # Check other moves.
  moved = False
  for s in S:
    for A_idx, a in enumerate(A):
      mod_A = [*A]
      if (mod_A[A_idx] - s) >= 0:
        mod_A[A_idx] -= s
        # Don't play the move if it can be dead-ended next.
        if not can_dead_end(mod_A):
          moved = True
          winner(mod_A, not player_a, winners, False)
  if not moved:
    winners.append("b" if player_a else "a")
  if top_level:
    player_a = 0
    player_b = 0
    for w in winners:
      if w == 'a':
        player_a += 1
      else:
        player_b += 1
    print("a", player_a)
    print("b", player_b)
    return "a" if player_a > player_b else "b"


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  t = int(input().strip())
  for t_itr in range(t):
    n = int(input().strip())
    A = list(map(int, input().rstrip().split()))
    result = winner(A)
    print()
    fptr.write(result + '\n')
  fptr.close()

