

def convert(s: str, numRows: int) -> str:
    """
    6. Z字形变换
    字符串 s 是以 Z 字形为顺序存储的字符串，目标是按行打印。
    思路：按顺序遍历字符串s时，每个字符c在N字形中对应的行索引先从s1增大到sn，
    再从sn减小至s1，...如此反复。
    解决方案为：模拟这个行索引的变化，在遍历s中把每个字符填到正确的行res[i]
    :param s:
    :param numRows:
    :return:
    """
    if numRows < 2:
        return s
    res = ["" for _ in range(numRows)]
    # flag用来控制索引方向
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return "".join(res)