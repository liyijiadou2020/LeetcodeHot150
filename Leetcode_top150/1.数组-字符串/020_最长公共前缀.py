from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """
    14. 最长公共前缀
    :param strs:
    :return:
    令最长公共前缀 ans 的值为第一个字符串，进行初始化；
    遍历后面的字符串，依次将其与 ans 进行比较，两两找出公共前缀，最终结果即为最长公共前缀；
    如果查找过程中出现了 ans 为空的情况，则公共前缀不存在直接返回；
    时间复杂度：O(s)，s 为所有字符串的长度之和。
    """
    if len(strs) == 0:
        return ""
    ans = strs[0]

    for i in range(1, len(strs)):
        idx = 0
        for char1, char2 in zip(ans, strs[i]):
            if char1 != char2:
                break
            idx += 1
        ans = ans[0:idx]
        if ans == "":
            break
    return ans

