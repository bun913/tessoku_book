# -*- coding: utf-8 -*-
"""
Nが100,000なのでO(n)で求めないと厳しい
"""
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
AD = sorted(list(set(A)))
ans = []
for a in A:
    ind = bisect_left(AD, a)
    ans.append(ind + 1)
print(*ans)
