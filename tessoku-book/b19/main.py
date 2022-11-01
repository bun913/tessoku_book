# -*- coding: utf-8 -*-
"""
今度はナップサックだが、Wが大きくVが小さい
iをどの品物を使うか、jを価値とした表にする
"""
N, W = list(map(int, input().split()))
limit = 1000 * N + 1
WV = [list(map(int, input().split())) for _ in range(N)]
dp = [[10**15 for _ in range(limit)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w = WV[i - 1][0]
    v = WV[i - 1][1]
    for j in range(1, limit):
        if j < v:
            dp[i][j] = dp[i - 1][j]
            continue
        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v] + w)
ans = 0
for i, w in enumerate(dp[N]):
    if w <= W:
        ans = i
print(ans)
