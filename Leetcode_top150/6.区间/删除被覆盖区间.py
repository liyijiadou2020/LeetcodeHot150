from typing import List


def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    """
    1288. 删除被覆盖区间
    思路：我们算一下被覆盖区间有多少个，然后用总数相减就是剩余区间数了
    :param intervals:
    :return:
    """
    
