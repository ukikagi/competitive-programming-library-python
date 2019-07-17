# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B
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

def bellman_ford(edges, s):
  N = len(edges)
  d = [INF] * N; d[s] = 0
  es = [(u, v, w) for u in range(N) for (v, w) in edges[u]]
  for _ in range(N):
    for u, v, w in es:
      if d[u] < INF: d[v] = min(d[v], d[u] + w)
  for u, v, w in es:
    if d[u] < INF and d[u] + w < d[v]:
      return [-INF] * N
  return d

V, E, r = reads()
edges = [[] for _ in range(V)]
for _ in range(E):
  s, t, d = reads()
  edges[s].append((t, d))
dist = bellman_ford(edges, r)
if dist[0] <= -INF:
  print("NEGATIVE CYCLE"); exit()
for i in range(V):
  print("INF" if dist[i] >= INF // 2 else dist[i])
