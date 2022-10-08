# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
N = int(input())
H = list(map(int, input().split()))
DP = [0 for _ in range(N)]
DP[1] = abs(H[1] - H[0])
for i in range(2, N):
    one_bef = DP[i - 1] + abs(H[i] - H[i - 1])
    two_bef = DP[i - 2] + abs(H[i] - H[i - 2])
    DP[i] = min(one_bef, two_bef)
print(DP[-1])
