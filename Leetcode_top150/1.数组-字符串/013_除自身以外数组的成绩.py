from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    238. 除自身以外数组的乘积
    算法技巧：前缀积技巧（前缀和的变种）
    构造一个prefix数组记录前缀积，在用一个suffix数组记录后缀积，
    根据前缀和后缀积可以计算除了当前元素以外其他元素的积了
    :param nums: [1,2,3,4]
    :return: [24, 12, 8, 6]
    """
    n = len(nums)
    prefix = [1] * n
    prefix[0] = nums[0]
    # 从左到右的前缀积，prefix[i]是nums[0..i]的元素积
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i]

    suffix = [1] * n
    suffix[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i]
    # 结果数组
    res = [0] * n
    res[0] = suffix[1]
    res[n - 1] = prefix[n - 2]
    for i in range(1, n - 1):
        res[i] = prefix[i - 1] * suffix[i + 1]
    return res


print(productExceptSelf([1, 2, 3, 4]))
