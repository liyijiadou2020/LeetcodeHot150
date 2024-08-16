"""
@ File       : a-plus-b-7.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：https://ac.nowcoder.com/acm/contest/5657/G
"""

import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    res = sum(nums)
    print(res)


