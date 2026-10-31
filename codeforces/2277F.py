#!/usr/bin/env python3

X = """
6
1
1
1
2
1 2
5 13
2 1
3
1 2
1 3
7 2 9
2 3 1
4
1 2
1 3
2 4
3 1 4 1
3 2 4 1
8
1 2
2 3
3 4
4 5
5 6
6 7
7 8
17 23 31 12 8 45 19 62
4 3 6 1 7 8 2 5
10
1 2
1 3
2 4
2 5
3 6
3 7
4 8
5 9
6 10
101 203 157 59 311 83 97 127 41 67
3 10 2 8 1 7 5 6 9 4
"""
X = X.strip().splitlines()
X = [[int(x1) for x1 in x.split(" ")] for x in X]
M = 998_244_353
at = 1
t = X[0][0]
assert 1 <= t <= 10**4
while at < len(X):
  n = X[at][0]
  assert len(X[at]) == 1
  assert 1 <= n <= 5*(10**5)
  end = n-1+2+1
  c = X[at:at+end]
  V1 = {i: [] for i in range(1, n+1)}
  if n > 0:
    for u,v in c[1:-2]:
      assert 1 <= u and u <= n and u != v
      V1[u].append(v)
      V1[v].append(u)  # two-way
  for r in range(1, n+1):
    V = {i: [] for i in range(1, n+1)}
    S = [r]
    seen = []
    while S:
      v = S.pop()
      seen.append(v)
      for v1 in V1[v]:
        if v1 not in seen:
          V[v].append(v1)
          S.append(v1)
    a = [*c[-2]]
    p = [*c[-1]]
    assert len(a) == n
    for i in range(len(a)):
      assert 0 <= a[i] < M
    for i in range(len(p)):
      assert 1 <= p[i] <= n
    assert len(p) == n
    assert len(p) == len(set(p))
    w = 0
    for i in range(len(p)):
      sub = []
      S = [p[i]]
      while S:
        v = S.pop()
        sub.append(v)
        for n1 in V[v]:
          if n1 not in sub and n1 != r:
            S.append(n1)
      w1 = 0
      for sub1 in sub:
        w1 += a[sub1-1]
        a[sub1-1] = 0
      a[p[i]-1] = w1
      w += w1
    print(w % M, end=' ')
  print()
  at += end

