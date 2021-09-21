#!/usr/bin/env python

import sys
from prime import prime


def factors(n, P=None):
  """
  Factor Tree returning only the leaves
  which are all prime factors of n.
  """
  if P is None:
    P = []
  if prime(n):
    return [n]
  x = 2
  while n % x != 0 and x < n:
    x += 1
  for c in [ x, n // x ]:
    if prime(c):
      P.append(c)
    else:
      factors(c, P)
  return P
    

if __name__ == "__main__":
  n = sys.argv[1]
  print("prime factors of {} are {}".format(n, factors(int(n))))

