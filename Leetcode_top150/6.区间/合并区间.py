from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    合并区间
    :param intervals:
    :return:
    输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
    输出：[[1,6],[8,10],[15,18]]
    解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    """
    if not intervals:
        return []
    # 按区间的 start 升序排列
    # Python语法，记住！
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    # 合并区间的主逻辑
    for interval in intervals:
        # 找到最后一个区间
        last = res[-1]
        if interval[0] <= last[1]:
            # 更新更大的 end
            last[1] = max(last[1], interval[1])
        else:
            # 处理下一个待合并区间
            res.append(interval)

    return res




intervals = [[1,3],[2,6],[15,18],[8,10]]
merge(intervals)