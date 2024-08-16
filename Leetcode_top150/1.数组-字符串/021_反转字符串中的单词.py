


def reverseWords(s: str) -> str:
    """
    151. 反转字符串中的单词
    :param s:
    :return:
    """
    ll = s.strip().split()
    ll = ll[::-1]
    return " ".join(ll)



s = "a good   example"
s1 = reverseWords(s)
print(s1)