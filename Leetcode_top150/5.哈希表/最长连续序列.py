from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    最长连续序列
    时间复杂度：O(n)，其中 n 为数组的长度。具体分析已在上面正文中给出。
    空间复杂度：O(n)。哈希表存储数组中所有的数需要 O(n) 的空间。
    -------
    思路：
    题解说的比较复杂，不太容易懂，简单来说就是每个数都判断一次这个数是不是连续序列的开头那个数。

    怎么判断呢，就是用哈希表查找这个数前面一个数是否存在，即num-1在序列中是否存在。存在那这个数肯定不是开头，直接跳过。
    因此只需要对每个开头的数进行循环，直到这个序列不再连续，因此复杂度是O(n)。 以题解中的序列举例:
    [100，4，200，1，3，4，2]
    去重后的哈希序列为：
    [100，4，200，1，3，2]
    按照上面逻辑进行判断：
    元素100是开头,因为没有99，且以100开头的序列长度为1
    元素4不是开头，因为有3存在，过，
    元素200是开头，因为没有199，且以200开头的序列长度为1
    元素1是开头，因为没有0，且以1开头的序列长度为4，因为依次累加，2，3，4都存在。
    元素3不是开头，因为2存在，过，
    元素2不是开头，因为1存在，过。
    完
    :param nums:
    :return:
    """
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            # 说明num可以是开头; 如果不是开头直接跳过这个数即可
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                # 从当前数字往后找，直到不再找到连续的元素
                current_num += 1
                current_streak += 1

            # 每找到一个符合条件的序列就更新一次最大值
            longest_streak = max(longest_streak, current_streak)

    return longest_streak


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(longestConsecutive(nums))
