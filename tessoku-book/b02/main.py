# -*- coding: utf-8 -*-
"""
Atcoderの問題解く用

全ての組み合わせを列挙する方法
list(0...8)から2つを抜き出す
list(combinations(l, 2))

bit全探索でフラグが立っているかチェックする
if ((i >> j) & 1)
"""
A, B = list(map(int, input().split()))
for n in range(A, B + 1):
    if 100 % n == 0:
        print("Yes")
        exit()
print("No")
