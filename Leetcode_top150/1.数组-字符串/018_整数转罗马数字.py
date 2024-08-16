


def intToRoman(num: int) -> str:
    """
    12. 整数转罗马数字
    思路：贪心算法，每次尽量使用最大的数来表示。例如1994这个数，我们尽量用1000、900、90、4来表示，会得到正确答案MCMXCIV
    :param num:
    :return:
    """
    hashmap = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    res = ''
    for key in hashmap:
        if num // key != 0:
            count = num // key # 比如输入4000, count为4
            res += hashmap[key] * count
            num %= key
    return res


num = 1994
str = intToRoman(num)
assert "MCMXCIV" == str