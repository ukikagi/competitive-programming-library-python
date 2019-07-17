# coding: utf-8
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B
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
  st = BIT(n)
  for _ in range(q):
    c, x, y = reads()
    if c == 0:
      st.add(x-1, y)
    else:
      ans = st.sum(x-1, y)
      print(ans)

class BIT:
  def __init__(self, n):
    self._size = n
    self._body = [0] * (n+1)
  def __repr__(self):
    return ("BIT([" + ", ".join(str(x) for x in self._body) + "])")
  def size(self):
    return self._size
  def add(self, i, v):
    assert 0 <= i < self.size()
    i += 1
    while(i <= self.size()):
      self._body[i] += v
      i += i & -i
  def sum(self, *args):
    assert 1 <= len(args) <= 2
    if len(args) == 1: # [0, i)の和をとる
      i = args[0]
      assert 0 <= i <= self.size()
      s = 0
      while(i > 0):
        s += self._body[i]
        i -= i & -i
      return s
    else: # [i, j)の和をとる
      (i, j) = args
      return self.sum(j) - self.sum(i)

# wrapper for http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
class bit_raq:
  def __init__(self, n):
    self._size = n
    self._bit = BIT(n+1)
  def __repr__(self):
    return str([self.get(i) for i in range(self._size)])
  def add(self, s, t, x):
    self._bit.add(s, x)
    self._bit.add(t, -x)
  def get(self, i):
    return self._bit.sum(i+1)

main()