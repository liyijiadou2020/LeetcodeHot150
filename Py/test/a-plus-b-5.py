"""
@ File       : a-plus-b-5.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：
"""

import sys

t = int(input())

for _ in range(t):
    data = input().split()
    n = data[0]
    nums = list(map(int, data[1:]))
    res = sum(nums)
    print(res)
