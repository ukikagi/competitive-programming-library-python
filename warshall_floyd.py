# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
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
INF = 1 << 60

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

def adjmat(edges):
  N = len(edges)
  K = [[INF] * N for _ in range(N)]
  for u in range(N):
    K[u][u] = 0
    for v, c in edges[u]:
      K[u][v] = c
  return K

def warshall_floyd(edges):
  N = len(edges); d = adjmat(edges)
  for k, i, j in product(range(N), range(N), range(N)):
    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
  return d

def stri(x):
  return "INF" if x >= INF // 2 else str(x)

V, E = reads()
edges = [[] for _ in range(V)]
for _ in range(E):
  s, t, d = reads()
  edges[s].append((t, d))
dmat = warshall_floyd(edges)

if any(dmat[i][i] < 0 for i in range(V)):
  print("NEGATIVE CYCLE"); exit()
for i in range(V):
  print(" ".join(stri(dmat[i][j]) for j in range(V)))
