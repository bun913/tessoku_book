# -*- coding: utf-8 -*-
"""
DP経路の復元
"""
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
DP = [0 for _ in range(N)]
DP[1] = A[0]
DP[2] = min(DP[0] + A[1], B[0])

# DPによる最短コストの算出
for i in range(2, N):
    a = A[i - 1] + DP[i - 1]
    b = B[i - 2] + DP[i - 2]
    DP[i] = min(a, b)
# DPのコスト値から最短経路を算出
p = N - 1
ans = []
while p >= -1:
    n = p - 1
    ans.append(p + 1)
    if DP[p] == DP[p - 1] + A[n]:
        p -= 1
        continue
    p -= 2
print(len(ans))
print(*ans[::-1])
