# -*- coding: utf-8 -*-
"""
二部探索の練習
"""
from bisect import bisect_left

N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = bisect_left(A, X) + 1
print(ans)
