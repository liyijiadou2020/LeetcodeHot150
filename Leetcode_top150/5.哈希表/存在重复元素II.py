from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    判断重复的元素II
    思路：滑动窗口。维护一个长度不超过 k + 1的窗口。如果在该窗口内存在重复元素，则下标一定满足要求。
    滑动窗口先右扩再左缩。右扩：当窗口的长度小于k的时候。左缩：当窗口的长度等于k+1时，移除掉窗口最左边的元素。
    每一次右扩窗口都要判断，新加入的元素是否在窗口中有重复元素，直到完成了整个数组的遍历为止。
    :param nums:
    :param k:
    :return:
    """
    s = set()
    for i, num in enumerate(nums):
        if i > k:
            s.remove(nums[i - k - 1])
        if num in s:
            return True
        s.add(num)
    return False