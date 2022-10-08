# -*- coding: utf-8 -*-
"""
部分和問題
N枚のカード
カードの中からいくつかを選んで書かれた数の合計がS以下となる方法の確認
Nが60なのでbit全探索で全てのパターンを試すのは無理

二次元のDPで60パターンを試していけばなんとかなりそう
"""
N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
dp[0][0] = True

for i in range(1, N + 1):
    cur = A[i - 1]
    for j in range(S + 1):
        # 上がTrueなら特に条件なくTrue
        if dp[i - 1][j] is True:
            dp[i][j] = True
        if j - cur < 0:
            continue
        if dp[i - 1][j - cur]:
            dp[i][j] = True
print("Yes" if dp[-1][-1] is True else "No")
