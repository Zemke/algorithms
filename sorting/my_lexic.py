#!/usr/bin/env python

import sys

def compare(a, b):
  min_length = min(len(a), len(b))
  x = a[:min_length]
  y = b[:min_length]
  if x.startswith(y):
    return len(a) - len(b)
  for xi in range(len(x)):
    if x[xi] == y[xi]:
      return compare(x[xi+1:], y[xi+1:])
    else:
      return -1 if x[xi] < y[xi] else 1
  return 0

def mysort(nn):
  count = 0
  while count < len(nn):
    mv = nn.pop()
    t_idx = 0
    while len(nn) < t_idx or (compare(mv, nn[t_idx]) > 0 and t_idx < count):
      t_idx += 1
    nn.insert(t_idx, mv)
    count += 1

if __name__ == "__main__":
  s = sys.argv[1:]
  mysort(s)
  print(", ".join(s))

