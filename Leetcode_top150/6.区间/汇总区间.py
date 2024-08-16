from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    """
    给定一个  无重复元素 的 有序 整数数组 nums 。
    返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。
    也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
    列表中的每个区间范围 [a,b] 应该按如下格式输出：
        "a->b" ，如果 a != b
        "a" ，如果 a == b
    :param nums: [0,1,2,4,5,7]
    :return: ["0->2","4->5","7"]
    """
    left, right = 0, 0
    flag = 1 # 用来记录是否为连续序列
    res = []
    while right < len(nums):
        if right < len(nums) - 1 and nums[right + 1] == nums[left] + flag: # 连续序列扩充
            right += 1
            flag += 1
        else:
            if right > left:
                res.append(str(nums[left]) + "->" + str(nums[right]))
            else:
                res.append(str(nums[left]))
            left = right + 1
            right = left
            flag = 1
    return res


nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))