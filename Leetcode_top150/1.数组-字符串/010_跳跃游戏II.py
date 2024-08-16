from typing import List


def jump(nums: List[int]) -> int:
    """
    45. 跳跃游戏II
    :param nums:
    :return:
    """
    n = len(nums)
    dp = [0 for _ in range(n)]
    for i in range(n - 2, -1, -1):
        v = nums[i]
        if v == 0:
            dp[i] = float('inf')
            continue
        dp[i] = 1 + min(dp[i + 1:i + v + 1])

    return dp[0]


nums = [1000, 0]
print(jump(nums))
