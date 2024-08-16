class Solution:
    """
    空间复杂度：O(1)
    时间复杂度：O(logN)
    """

    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n

        while True:
            fast = self.getNext(fast)
            fast = self.getNext(fast)
            slow = self.getNext(slow)

            if fast == 1:
                return True
            if fast == slow:
                return False

    def getNext(self, num: int) -> int:
        """
        取各位数字的平方和，即下一个数
        """
        sum = 0
        localNum = num

        while localNum > 0:
            unitsDigit = localNum % 10  # 取个位数字
            sum += unitsDigit * unitsDigit
            localNum //= 10

        return sum