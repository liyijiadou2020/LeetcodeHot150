
def isIsomorphic(s: str, t: str) -> bool:
    """
    205 同构字符串
    :param s:
    :param t:
    :return:
    思路：这里要求s和t集合之间存在双射的关系。双射是指一一对应，既是单射又是满射，所以需要构建两个字典，
    对于每一个出现的字母都判断是不是单射+满射
    """
    s2t = {}
    t2s = {}
    for a, b in zip(s,t):
        if a in s2t and s2t[a] != b or b in t2s and t2s[b] != a:
            return False
        s2t[a] = b
        t2s[b] = a
    return True



s = "foo"
t = "zuu"

print(isIsomorphic(s, t))