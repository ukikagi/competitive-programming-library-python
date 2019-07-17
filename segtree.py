# coding: utf-8
import sys
from copy import copy, deepcopy
import heapq
import bisect
import operator
from itertools import *

def read():
  return int(input())

def reads():
  return [int(x) for x in input().split()]

INF = 2**31 - 1

def main():
  n, q = reads()
  st = segtree(n)
  for _ in range(q):
    c, x, y = reads()
    if c == 0:
      st.update(x, y)
    else:
      ans = st.find(x, y+1)
      print(ans)

class segtree:
  def __init__(self, n):
    self._size = n
    self._cap = next(1<<i for i in count() if 1<<i >= n)<<1
    self._body = [INF] * self._cap
  def __repr__(self):
    return ("segtree([" + ", ".join(str(x) for x in self._body[1:]) + "])")
  def size(self): return self._size
  def update(self, i, v):
    p = i + (self._cap >> 1)
    self._body[p] = v
    while p > 0:
      p >>= 1
      self._body[p] = min(self._body[p<<1], self._body[p<<1|1])
  def find(self, i, j, k = 1, l = 0, r = None):
    if r is None: r = self._cap >> 1
    if r <= i or j <= l:
      return INF
    elif i <= l and r <= j:
      res = self._body[k]
      return self._body[k]
    else:
      m = (l + r) >> 1
      res = min(self.find(i, j, k<<1, l, m), self.find(i, j, k<<1|1, m, r))
      return res

main()