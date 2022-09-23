# -*- coding: utf-8 -*-
"""
累積和の問題
それぞれの参加者の前日比を取る
前日比の累積和が答えになる
"""
from itertools import accumulate

D = int(input())
N = int(input())
# 前日比を格納する配列
rates = [0 for _ in range(D)]
for _ in range(N):
    L, R = list(map(int, input().split()))
    rates[L - 1] += 1
    if R < D:
        rates[R] -= 1
# 累積和がd日目の出席者数になる
for d in accumulate(rates):
    print(d)
