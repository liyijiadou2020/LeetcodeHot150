

def romanToInt(s: str) -> int:
    """
    13. 罗马数字转整数
    思路：小值在左边则减少小值，小值在右边则增加小值
    :param s:
    :return:
    """
    # 把单个罗马字母翻译成数字
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    n = len(s)
    res = 0
    pre = d[s[0]]
    for i in range(1, n):
        cur = d[s[i]]
        if pre < cur:
            res -= pre
        else:
            res += pre
        pre = d[s[i]]
    res += pre
    return res

print(romanToInt("LVIII"))

