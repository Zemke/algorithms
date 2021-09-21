#!/usr/bin/env python

from sys import exit


primes = [2, 3, 5, 7, 11, 13, 17, 19,
          23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79,
          83, 89, 97]
DP_prime = dict(enumerate([(i in primes) for i in range(0, 101) ]))


def prime(n):
  """
  Is prime with the help of dynamic programming.
  """
  if n in DP_prime:
    return DP_prime[n]
  for i in range(2, n):
    if n % i == 0:
      DP_prime[n] = False
      return DP_prime[n]
  DP_prime[n] = True
  return DP_prime[n]


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

