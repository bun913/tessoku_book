# -*- coding: utf-8 -*-
"""
二次元DPで部分和問題
今回はNが60なのでbit全探索は不可
"""
N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
dp[0][0] = True

# DP表の作成
ans = set()
for i in range(1, N + 1):
    cur = A[i - 1]
    for j in range(S + 1):
        if dp[i - 1][j] is True:
            dp[i][j] = True
            continue
        if j >= cur and dp[i - 1][j - cur] is True:
            dp[i][j] = True
# Sを作れない場合
if dp[-1][-1] is False:
    print(-1)
    exit()

# # DPを復元する
ans = []
j = S
for i in range(N, 0, -1):
    if dp[i - 1][j] is True:
        continue
    j -= A[i - 1]
    ans.append(i)

print(len(ans))
print(*ans[::-1])
