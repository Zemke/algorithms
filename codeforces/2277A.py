#!/usr/bin/env python3

from collections import Counter

X = """
6
3 1
0 2 1
4 2
1 2 3 4
5 2
0 1 0 1 0
5 4
0 0 1 0 0
5 1
4 0 0 0 2
6 2
0 0 2 1 0 0
"""
X = X.strip().splitlines()
X = [[int(n) for n in x.split(" ")] for x in X]
t = X[0][0]
assert 1 <= t <= 500
at = 1
while at < len(X):
  assert len(X[at]) == 2
  n, k = X[at]
  assert 1 <= k <= n <= 100
  at += 1
  a = sorted(X[at])
  assert len(a) == n
  at += 1
  C = Counter(a)
  mx = max(C)
  assert C[mx] > 0
  for i in range(mx+1):
    if C[i] == 0:
      print(i)
      break
    C[i] -= 1
    cons = sorted((a1,c) for a1,c in C.items() if a1 <= i)
    torm = k-1
    if sum(c for _,c in cons) < torm:
      print(i)
      break
    while torm > 0:
      for a1,c in cons:
        C[a1] -= (torm1 := min(torm, C[a1]))
        torm -= torm1
  else:
    print(i+1)

