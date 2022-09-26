# -*- coding: utf-8 -*-
"""
正の整数Nが与えられる
x**3 + x = Nを満たす正の実数xを出力する
Nが10万以下であることは保証されている
ということはxの最大値は100以下であることは保証されている
"""
N = int(input())


def is_ok(x):
    return pow(x, 3) + x >= N


def meguru_bisect(ng, ok):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 0.001:
        mid = (ok + ng) / 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru_bisect(-1.0, 100.0)
print(f"{ans:.12f}")
