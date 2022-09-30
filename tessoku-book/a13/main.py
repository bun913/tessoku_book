# -*- coding: utf-8 -*-
"""
尺取り法で考え直してみた
O(N)で解いてみる
"""
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0

# 一番左から見始める
l = 0
r = l + 1
while l < N:
    left = A[l]
    # 左が右に追いついてしまっている場合は右をずらす
    if l == r:
        r += 1
    # 右端を行けるまで右にずらす
    while r < N and A[r] - left <= K:
        ans += r - l
        r += 1
    else:
        l += 1
print(ans)
