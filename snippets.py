# coding: utf-8
import sys
from copy import copy, deepcopy
import heapq
import bisect
import operator
from itertools import *

sys.setrecursionlimit(100000)

INF = 1 << 63

def accumulate2(mat, h, w):
  acc = matrix(0, h+1, w+1)
  for y in range(h):
    vec = accumulate1(mat[y])
    acc[y+1] = [acc[y][x] + vec[x] for x in range(w+1)]
  return acc
