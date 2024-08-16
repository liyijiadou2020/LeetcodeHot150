

def lengthOfLastWord(s: str) -> int:
    """
    58. 最后一个单词的长度
    :param s:
    :return:
    """
    return len(s.strip().split()[-1])


n = lengthOfLastWord( "   fly me   to   the moon  ")
n1 = lengthOfLastWord("luffy is still joyboy")
print(n1)