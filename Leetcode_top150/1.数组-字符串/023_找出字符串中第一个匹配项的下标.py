

def strStr(haystack: str, needle: str) -> int:
    """
    28. 找出字符串中第一个匹配项的下标
    思路：
    :param haystack:
    :param needle:
    :return:
    """
    # 解法1：Python API
    return haystack.find(needle)
    # 解法2: KMP算法

