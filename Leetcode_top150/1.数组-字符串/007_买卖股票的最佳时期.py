"""
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
121. 买卖股票的最佳时期
"""
from typing import List


# 原始版本
def maxProfit_k_1(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0 for i in range(2)] for j in range(n)]
    for i in range(n):
        if i - 1 == -1:
            # base case
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], -prices[i])
    return dp[n-1][0]

# 空间复杂度优化版本
def maxProfit_k_1_optic(prices: List[int]) -> int:
    n = len(prices)
    # base case: dp[-1][0] = 0, dp[-1][1] = -infinity
    dp_i_0, dp_i_1 = 0, float('-inf')
    for i in range(n):
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp_i_0, dp_i_1 = max(dp_i_0, dp_i_1 + prices[i]), max(dp_i_1, -prices[i])
    return dp_i_0


