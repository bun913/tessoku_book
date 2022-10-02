# -*- coding: utf-8 -*-
"""
Python式のdequeの尺取り方を試してみた

2つの整数の組み合わせを左から試す
Aは小さい順に並んでいるので並び替え不要
"""
from collections import deque

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
q = deque()

ans = 0
for a in A:
    q.append(a)
    while not (a - q[0]) <= K:
        rm = q.popleft()
    lq = len(q)
    ans += lq - 1
print(ans)
