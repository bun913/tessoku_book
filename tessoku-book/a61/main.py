# -*- coding: utf-8 -*-
"""
"""
N, M = list(map(int, input().split()))
g = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

for k, s in enumerate(g[1:]):
    to_s = list(map(str, sorted(s)))
    f = "{" + ", ".join(to_s) + "}"
    print("{}: {}".format(k + 1, f))
