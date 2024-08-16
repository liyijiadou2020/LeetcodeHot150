from typing import List


def canJump(nums: List[int]) -> bool:
    """
    55. 跳跃游戏
    方法：贪心算法。为了判断一个位置y是否可达，我们需要判断是否存在这样一个位置x，
    x可以跳跃的最大长度为x+nums[x]。我们依次遍历数组中的每个位置，实时维护一个数组dp表示最远可达位置，
    对于当前位置i，如果它最远可以到达n-1则直接返回True，否则如果dp(i)==0且i!=n-1，说明当前位置已经无法继续跳且未达到终点，此时返回False。
    :param nums:
    :return:
    """
    n = len(nums)
    if n == 1:
        return True
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    for i in range(1, n):
        # 可达
        if dp[i - 1] >= i:
            dp[i] = max(dp[i - 1], i + nums[i])
            if dp[i] >= n - 1:
                return True
    return False


nums = [0]
print(canJump(nums))
