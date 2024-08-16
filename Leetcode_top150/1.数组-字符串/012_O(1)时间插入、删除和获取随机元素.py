"""
https://leetcode.cn/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
"""
import random


class RandomizedSet:
    """
    380. O(1) 时间插入、删除和获取随机元素
    关键是要结合哈希表，使数组的删除也达到O(1)复杂度.
    如果用数组存储元素的话，插入，删除的时间复杂度怎么可能是 O(1) 呢？
    可以做到！对数组尾部进行插入和删除操作不会涉及数据搬移，时间复杂度是 O(1)。
    如果我们想在 O(1) 的时间删除数组中的某一个元素 val，
    可以先把这个元素交换到数组的尾部，然后再 pop 掉。
    交换两个元素必须通过索引进行交换对吧，
    那么我们需要一个哈希表 valToIndex 来记录每个元素值对应的索引。
    """
    def __init__(self):
        self.nums = [] # 存储元素的值
        self.valToIndex = {} # 记录每个元素对应nums中的索引

    def insert(self, val: int) -> bool:
        """
        如果 val 不存在集合中，则插入并返回 true，否则直接返回 false
        :param val:
        :return:
        """
        if val in self.valToIndex:
            return False
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        【关键！】
        如果val在集合中则删除，否则返回false
        :param val:
        :return:
        """
        if val not in self.valToIndex:
            return False
        # 先获取到val对应的索引
        index = self.valToIndex[val]
        # 将最后一个元素对应的索引修改为index
        self.valToIndex[self.nums[-1]] = index
        # 交换最后一个元素和要删除的元素
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # 把要删除的元素pop出去，O(1)复杂度
        self.nums.pop()
        # 删除元素val对应的索引
        del self.valToIndex[val]
        return True


    def getRandom(self) -> int:
        """
        从集合中等概率地获取一个元素
        :return:
        """
        # 随机获取nums中的一个元素
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()