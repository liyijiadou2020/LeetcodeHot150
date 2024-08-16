"""
@ File       : order-str-1.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：https://ac.nowcoder.com/acm/contest/5657/H
"""

n = int(input())
strs = input().split()

sorted = sorted(strs)
res = ' '.join(sorted)
print(res)