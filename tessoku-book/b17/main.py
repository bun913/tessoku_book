# -*- coding: utf-8 -*-
"""
DPで解いて経路を復元する
"""
N = int(input())
H = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 0
dp[1] = abs(H[1] - H[0])

for i in range(2, N):
    if i == 1:
        dp[i] = abs(H[i - 1] - H[i]) + dp[i - 1]
        continue
    opt = min(abs(H[i - 2] - H[i]) + dp[i - 2], abs(H[i - 1] - H[i]) + dp[i - 1])
    dp[i] = opt

ans = []
i = N - 1
while True:
    ans.append(i + 1)
    if i == 0:
        break
    if dp[i] == dp[i - 1] + abs(H[i] - H[i - 1]):
        i -= 1
        continue
    i -= 2
print(len(ans))
print(*ans[::-1])
