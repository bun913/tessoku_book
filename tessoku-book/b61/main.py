# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
from collections import Counter, defaultdict

N, M = list(map(int, input().split()))
graph = [[] for i in range(N + 1)]
ans = defaultdict(int)
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
    ans[a] += 1
    ans[b] += 1

c = Counter(ans)
print(c.most_common()[0][0])
