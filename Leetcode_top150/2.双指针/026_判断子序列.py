def isSubsequence(s: str, t: str) -> bool:
    """
    392. 判断子序列
    给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
    --
    进阶：
    如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
    :param s: "abc"
    :param t: "ahbgdc"
    :return: True
    """
    # 法一、双指针
    # 初始化两个指针i和j，分别指向s和t的初始位置。匹配成功则i和j同时右移；匹配失败则j右移，i不变，尝试用t的下一个字符来匹配s。
    # 如果最终i移动到s的末尾，说明s是t的子序列
    # 时间复杂度: O(m+n).
    # 空间复杂度：O(1)
    n, m = len(s), len(t)
    i = j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == n

def isSubsequence2(s: str, t: str) -> bool:
    """
    392. 判断子序列【优化】
    法二：动态规划
    我们花费了大量时间在t中寻找下一个匹配的字符(O(m))，这个步骤应该是可以优化的。
    如果t固定不变，s的输入可以有上亿种情况，这时候我们就应该为t专门建立一个字母-位置矩阵表f，f[i][j]表示从位置i开始往后第一次字母j出现的位置。
    实现了这张表之后，我们就可以实现O(1)时间复杂度在t中寻找下一个匹配字符了。
    --
    时间复杂度：O(m×∣Σ∣+n)，其中n 为 s 的长度，m 为 t 的长度，Σ 为字符集。在本题中字符串只包含小写字母，∣Σ∣=26。
        预处理时间复杂度 O(m)，判断子序列的复杂度为O(n)
    空间复杂度：O(m×∣Σ∣)，为动态规划数组的开销。
    :param s:
    :param t:
    :return:
    """
    n, m = len(s), len(t)
    dp = [[0] * 26 for _ in range(m)]
    # 对于边界状态dp[m-1][...]，我们置dp[m][...]为m，让dp[m-1][...]可以正常转移
    dp.append([m] * 26)
    # 从后往前遍历数组,生成
    for i in range(m - 1, -1, -1):
        for j in range(26):
            dp[i][j] = i if ord(t[i]) == j + ord('a') else dp[i + 1][j]

    # 判断s是否为t的子串
    add = 0
    for i in range(n):
        if dp[add][ord(s[i]) - ord('a')] == m:
            return False
        add = dp[add][ord(s[i]) - ord('a')] + 1

    return True


s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))