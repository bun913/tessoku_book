# -*- coding: utf-8 -*-
"""
典型的なナップサック問題
"""
N, W = list(map(int, input().split()))
VW = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w = VW[i - 1][0]
    v = VW[i - 1][1]
    for j in range(1, W + 1):
        # 今回のものをバックに入れられない
        if j < w:
            dp[i][j] = dp[i - 1][j]
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[-1][-1])
