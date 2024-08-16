import re


def isPalindrome(s: str) -> bool:
    """
    125 验证回文串
    :param s:
    :return:
    """
    # 去除前后空格+转小写
    s = s.strip().lower()
    # Python 的re模块提供了re.sub()用于替换字符串中的匹配项【注意练习正则！】
    s = re.sub('[\W_]+', '', s)
    print(s)
    # 双指针
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


s = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
s4 = "A"
s5 = "@!#$!@#^%#$%^&"

print(isPalindrome(s5))


