# -*- coding: utf-8 -*-
"""
N個の整数
小さい順に並んでいる。異なる二つの整数のペアを選んでその差がK以下になるような選び方

1つの数は総当たりで、他は二部探索で探せば良くないか
"""
from bisect import bisect_right

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
for i, a in enumerate(A):
    j = bisect_right(A, a + K)
    ans += j - (i + 1)
print(ans)
