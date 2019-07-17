# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=jp
from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *
from heapq import *
import operator
import math
from fractions import gcd
from random import randint

setrecursionlimit(10**8)
INF = 1 << 30

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

def dijkstra(edges, s):
  N = len(edges)
  result = [INF] * N; result[s] = 0
  que = [(0, s)]
  while len(que) > 0:
    (d, u) = heappop(que)
    if result[u] < d: continue
    for (t, cost) in edges[u]:
      if d + cost < result[t]:
        result[t] = d + cost
        heappush(que, (d + cost, t))
  return result

V, E, r = reads()
edges = [[] for _ in range(V)]
for _ in range(E):
  s, t, d = reads()
  edges[s].append((t, d))
dist = dijkstra(edges, r)
for i in range(V):
  print("INF" if dist[i] >= INF else dist[i])
