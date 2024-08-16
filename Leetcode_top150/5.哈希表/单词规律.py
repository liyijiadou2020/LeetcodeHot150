


def wordPattern(pattern: str, s: str) -> bool:
    """
    290 单词规律
    :param pattern:
    :param s:
    :return:
    """
    lls = s.split(' ')
    if len(lls) != len(pattern):
        return False
    # t: pattern, s: s
    pattern2s, s2pattern = {}, {}
    for i in range(len(lls)):
        # 判断单词映射到字母
        if lls[i] in s2pattern and pattern[i] != s2pattern[lls[i]] \
                or pattern[i] in pattern2s and pattern2s[pattern[i]] != lls[i]: # 判断字母映射到单词
            return False
        s2pattern[lls[i]] = pattern[i]
        pattern2s[pattern[i]] = lls[i]
    return True


t = "abba"
s = "dog cat cat dog"
print(wordPattern(t, s))

t1 = "aaaa"
s1 = "dog cat cat fish"
print(wordPattern(t1, s1))



