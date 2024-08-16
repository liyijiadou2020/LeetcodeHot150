"""
@ File       : a-plus-b-6.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：https://ac.nowcoder.com/acm/contest/5657/F
"""
import sys

for line in sys.stdin:
    if (len(line) == 0):
        break
    data = line.split()
    n = int(data[0])
    nums = list(map(int, data[1:]))
    res = sum(nums)
    print(res)

