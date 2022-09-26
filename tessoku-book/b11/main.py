# -*- coding: utf-8 -*-
"""
めぐる式二部探索で実装し直すバージョン
"""
N = int(input())
A = list(map(int, input().split()))
AD = sorted(A)
Q = int(input())


def is_ok(x: int, n: int):
    # 条件を満たすかどうか？問題ごとに定義
    return n >= x


def meguru_bisect(x, ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(x, AD[mid]):
            ok = mid
        else:
            ng = mid
    return ok


for i in range(Q):
    X = int(input())
    ind = meguru_bisect(X, -1, N)
    print(ind)
