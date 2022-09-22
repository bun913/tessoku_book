# -*- coding: utf-8 -*-
"""
ザ累積和って感じ
区間の和を求めれば良いだけ
"""
from itertools import accumulate

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
S = [0] + list(accumulate(A))

for _ in range(Q):
    L, R = list(map(int, input().split()))
    s = S[R] - S[L - 1]
    print(s)
