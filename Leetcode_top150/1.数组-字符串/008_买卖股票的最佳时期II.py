from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    122. 买卖股票的最佳时期II
    :param prices:
    :return:
    """
    n = len(prices)
    dp_i_0, dp_i_1 = 0, float('-inf')
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0