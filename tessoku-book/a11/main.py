# -*- coding: utf-8 -*-
"""
二部探索の練習

めぐる式二部探索で実装するバージョン
"""
N, X = list(map(int, input().split()))
A = list(map(int, input().split()))


def is_ok(n):
    # 条件を満たすかどうか？問題ごとに定義
    return n > X


def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(A[mid]):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru_bisect(-1, N)
print(ans)
