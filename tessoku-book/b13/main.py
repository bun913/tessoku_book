# -*- coding: utf-8 -*-
"""
Nが100000なのでbit全探索は無理
dequeを使った実装で素直にtotalを足したり引いたりすれば累積和も不要
"""
from collections import deque

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
q = deque()

ans = 0
total = 0
for a in A:
    q.append(a)
    total += a
    while q and total > K:
        rm = q.popleft()
        total -= rm
    ans += len(q)
print(ans)
