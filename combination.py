from sys import exit, setrecursionlimit, stderr
from functools import reduce
from itertools import *
from collections import *
from bisect import bisect
from heapq import *

def read():
  return int(input())
 
def reads():
  return [int(x) for x in input().split()]
 
N = read()
MOD = 10**9 + 7

fact = [1] * N
for i in range(1, N): fact[i] = (fact[i-1] * i) % MOD
invfact = [0] * N; invfact[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(N-2, -1, -1): invfact[i] = invfact[i+1] * (i+1) % MOD
def comb(n, k):
  return fact[n] * invfact[n-k] * invfact[k] % MOD if 0 <= k <= n else 0

def egcd(a, b):
  if b == 0: return a, 1, 0
  else:
    q, r = divmod(a, b)
    g, x, y = egcd(b, r)
    return g, y, x - q * y

def inv(n):
  return pow(n, MOD-2, MOD)