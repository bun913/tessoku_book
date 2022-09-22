# -*- coding: utf-8 -*-
"""
L回目からR回めまでの中であたりとハズレのどちらが多いか

単純にあたり、ハズレ両方の数の累積和を持っておけば終わりでは
"""
N = int(input())
A = list(map(int, input().split()))
wins = [0]
losses = [0]
for i, a in enumerate(A):
    if a == 0:
        losses.append(losses[i] + 1)
        wins.append(wins[i])
        continue
    wins.append(wins[i] + 1)
    losses.append(losses[i])

Q = int(input())
for _ in range(Q):
    L, R = list(map(int, input().split()))
    win_num = wins[R] - wins[L - 1]
    loss_num = losses[R] - losses[L - 1]
    if win_num > loss_num:
        print("win")
        continue
    elif win_num < loss_num:
        print("lose")
        continue
    print("draw")
