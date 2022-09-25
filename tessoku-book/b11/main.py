# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
AD = sorted(A)
Q = int(input())

for i in range(Q):
    X = int(input())
    ind = bisect_left(AD, X)
    print(ind)
