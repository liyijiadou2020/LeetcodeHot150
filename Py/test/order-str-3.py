"""
@ File       : order-str-3.py
@ Time       ：2024/5/10
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：
"""

while True:
    try:
        strs = input().split(',')
        sorted_strs = sorted(strs)
        res = ','.join(sorted_strs)
        print(res)
    except EOFError:
        break
