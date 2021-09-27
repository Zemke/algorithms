#!/usr/bin/env python

# could be much greater in Python 3
maxint = 9223372036854775807

def Dijkstra(G, source):
  """
  Stupid Dijkstra without priority queue.
  Lower weight is better.
  """
  Q = set()
  dist = {}
  for v in G:
    dist[v] = maxint
    Q.add(v)
  dist[source] = 0
  while len(Q) > 0:
    u = None
    least = maxint
    for v in Q:
      if v is None or dist[v] < least:
        u = v
        least = dist[v]
    Q.remove(u)
    for v in u.nn:
      if v not in Q:
        continue
      alt = v.weight + dist[u]
      if alt < dist[v]:
        dist[v] = alt
  return dist


G = [None]  # TODO let G be a list of vertices
# target vertex has the lowest dist
dist = Dijkstra(G, G[0])
t = None
t_d = None
for v, d in dist.items():
  if v.row == len(rows) - 1:
    if t is None or d < t_d:
      t = v
      t_d = d

# reverse iterate the result from Dijkstra for shortes path
prev = t
for row in range(len(rows)-2, -1, -1):
  nn = []
  for v in G:
    if v.row == row:
      if prev == v.nn[0]:
        nn.append(v)
      elif prev == v.nn[1]:
        nn.append(v)
  if len(nn) < 2 or dist[nn[0]] < dist[nn[1]]:
    prev = nn[0]
  else:
    prev = nn[1]
  # now prev is part of the shortest path
  summ += 100 - prev.weight

