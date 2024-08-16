class MinStack:
    """
    155. 最小栈
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    实现 MinStack 类:
    MinStack() 初始化堆栈对象。
    void push(int val) 将元素val推入堆栈。
    void pop() 删除堆栈顶部的元素。
    int  top() 获取堆栈顶部的元素。
    int  getMin() 获取堆栈中的最小元素。
    思路：
    1. 每一个元素入栈时，使用一个额外的栈minStk记录栈中每个元素入栈时栈中元素最小元素是多少
        这样每次删除元素时就能快速得到剩余栈中的最小元素了
    2. 其次，可以做一些优化，减少minStk中存储的元素个数
    """
    def __init__(self):
        # 记录栈中的所有元素
        self.stk = []
        # 阶段性记录栈中最小元素
        self.minStk = []

    def push(self, val: int) -> None:
        """
        入栈。需要维护 minStk
        :param val:
        :return:
        """
        self.stk.append(val)
        # 维护 minStk 栈顶为全栈最小元素
        if not self.minStk or val <= self.minStk[-1]:
            self.minStk.append(val)
        else:
            self.minStk.append(self.minStk[-1])

    def pop(self) -> None:
        """
        出栈。
        :return:
        """
        self.stk.pop()
        self.minStk.pop()

    def top(self) -> int:
        """
        获取堆栈顶部的元素。
        :return:
        """
        return self.stk[-1]

    def getMin(self) -> int:
        """
        获取堆栈中的最小元素。
        :return:
        """
        return self.minStk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()