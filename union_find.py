# verified in http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
 
def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]

def main():
  n, q = reads()
  uf = union_find(n)
  for _ in range(q):
    c, x, y = reads()
    if c == 0:
      uf.unite(x, y)
    else:
      print(int(uf.same(x, y)))

class union_find:
  def __init__(self, n): self.par = [-1] * n; self.rank = [0] * n
  def __repr__(self): return "union_find({0})".format([self.root(i) for i in range(n)])
  def unite(self, x, y):
    x = self.root(x); y = self.root(y)
    if x == y: return
    if self.rank[x] < self.rank[y]: self.par[x] = y
    else:
      self.par[y] = x
      if self.rank[x] == self.rank[y]: self.rank[x] += 1
  def root(self, x):
    if self.par[x] == -1: return x
    else: self.par[x] = self.root(self.par[x]); return self.par[x]
  def same(self, x, y): return self.root(x) == self.root(y)

main()