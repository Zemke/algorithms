#!/bin/python3


S_least = 2
S = { S_least, 3, 5, 7, 11, 13 }


def Mex(S):
    """
    Smallest non-negative number in a set.
    """
    n = 0
    while n in S:
      n += 1
    return n


def Grundy(n):
  """
  Grundy(n) = Mex[Grundy(n-1), Grundy(n-2), ... ]
  """
  if 0 <= n <= S_least:
    return 0
  pp = set();
  for s in S:
    if (n - s) >= 0:
      pp.add(Grundy(n - s))
  return Mex(pp)


print(Grundy(15))

