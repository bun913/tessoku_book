# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from itertools import accumulate

T = int(input())
N = int(input())
memo = [0 for _ in range(T + 1)]

for _ in range(N):
    L, R = list(map(int, input().split()))
    memo[L] += 1
    memo[R] -= 1
num_people = list(accumulate(memo))

for i in range(T):
    print(num_people[i])
