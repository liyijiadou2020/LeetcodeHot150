"""
@ File       : a-plus-b-2.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：https://ac.nowcoder.com/acm/contest/5657/B
"""
import sys


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    res = a + b
    print(res)
