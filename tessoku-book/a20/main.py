# -*- coding: utf-8 -*-
"""
"""
S = input()
T = input()

x_limit = len(S) + 1
y_limit = len(T) + 1

dp = [[0 for _ in range(y_limit)] for _ in range(x_limit)]
# 競プロ本128pにあるように各マスでの赤い線を通れる最大値を数えていく
for i in range(1, x_limit):
    for j in range(1, y_limit):
        is_same = S[i - 1] == T[j - 1]
        if is_same is True:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])
