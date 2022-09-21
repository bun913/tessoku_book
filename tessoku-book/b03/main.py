# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

for l in combinations(A, 3):
    if sum(l) == 1000:
        print("Yes")
        exit()
print("No")
