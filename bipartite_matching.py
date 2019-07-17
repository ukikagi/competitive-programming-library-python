# See: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_7_A&lang=jp

from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

INF = 1 << 60

def main():
  X, Y, E = reads()
  bi = bipmatch(X + Y)
  for _ in range(E):
    x, y = reads()
    bi.add_edge(x, X+y)
  ans = bi.count_match()
  print(ans)
  
class bipmatch:
  def __init__(self, N):
    self.size = N
    self.edges = [[] for _ in range(N)]

  def add_edge(self, u, v):
    self.edges[u].append(v)
    self.edges[v].append(u)

  def dfs(self, match, used, u):
    N = self.size; edges = self.edges
    used[u] = True
    for v in edges[u]:
      w = match[v]
      if w < 0 or not used[w] and self.dfs(match, used, w):
        match[u], match[v] = v, u
        return True
    return False

  def count_match(self):
    N = self.size; edges = self.edges
    res = 0; match = [-1] * N
    for v in range(N):
      if match[v] < 0:
        used = [0] * N
        if self.dfs(match, used, v):
          res += 1
    return res

main()