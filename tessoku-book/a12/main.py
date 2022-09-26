# -*- coding: utf-8 -*-
"""
N台のプリンター
プリンターiはAi秒毎にチラシを1枚印刷
全てのプリンターのスイッチを同時に入れた時K枚目のチラシが印刷されるのは何秒後か

答えが10**9を超えないということがわかっているので、答えの方で二部探索をする
"""
from functools import reduce

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


def is_ok(seconds):
    possible_cnt = reduce(lambda prev, x: prev + (seconds // x), A, 0)
    return possible_cnt >= K


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans = meguru_bisect(-1, 10**9 + 1)
print(ans)
