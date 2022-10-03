# -*- coding: utf-8 -*-
"""
典型定期なDP
答え・解説を見ずにチャレンジ
"""
N = int(input())
# 長さを合わせてDPしやすくする
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))
DP = [0 for _ in range(N)]

for i in range(1, N):
    if i == 1:
        DP[i] = A[i]
        continue
    a = A[i]
    b = B[i]
    optimized = min(DP[i - 1] + a, DP[i - 2] + b)
    DP[i] = optimized
print(DP[-1])
