# -*- coding: utf-8 -*-
"""
二次元配列の累積和
"""
from itertools import accumulate
import numpy as np

# 二次元の累積和を準備
H, W = list(map(int, input().split()))
X = [[0] + list(map(int, input().split(" "))) for _ in range(H)]
X.insert(0, [0 for _ in range(W + 1)])
accum = np.array(X)
accum = np.cumsum(accum, axis=1)
accum = np.cumsum(accum, axis=0)

# クエリ処理
Q = int(input())
for _ in range(Q):
    A, B, C, D = list(map(int, input().split()))
    ans = accum[C][D]
    # Aの1個左を引いて、Bの1個上を引く、さらに(A-1,B-1)の値をたす
    ans += accum[A - 1][B - 1]
    ans -= accum[A - 1][D]
    ans -= accum[C][B - 1]
    print(ans)
