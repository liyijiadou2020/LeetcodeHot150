"""
@ File       : demo_1.py
@ Time       ：2024/5/11
@ Author     ：Li Yijia
@ version    ：python 3.8.12
@ Description：
"""

if __name__ == '__main__':
    n = int(input())
    good_record = {}
    for i in range(n):
        line = input().strip().split(',')
        record = (line[0], line[1])
        if record in good_record:
            good_record[record] += 1
        else:
            good_record[record] = 1

    names = set(name for name, _ in good_record.keys())
    for name in names:
        if (name, 'a') not in good_record:
            print(name, 'invalid')
            continue
        a_, b_, c_ = 0, 0, 0
        a_ = max(0, good_record.get((name, 'a'), 0) - 1)
        b_ = max(0, good_record.get((name, 'b'), 0) - 5)
        c_ = max(0, good_record.get((name, 'c'), 0) - 5)

        print(name, f'{a_},{b_},{c_}')