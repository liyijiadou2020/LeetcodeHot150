from typing import Optional
from Leetcode_top150.common import ListNode

def reverse_1(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    【背！！！】
    递归反转链表
    :param head:
    :return:
    """
    # 递归函数要有 【base case】，也就是这句
    if not head or not head.next:
        return head
    # 当列表递归反转之后，新的节点就是last
    last = reverse_1(head.next)
    # 让反转后的链表的头结点（last）指向head
    head.next.next = head
    # 让head的下一个指向空指针，链表反转完成
    head.next = None
    # 返回反转后的链表
    return last


def reverse_2(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    【背！！】
    迭代反转链表
    :param head:
    :return:
    """
    pre, cur, nxt = None, head, head
    while cur:
        nxt = cur.next
        # 逐个节点反转
        cur.next = pre
        # 更新指针的位置
        pre = cur
        cur = nxt
    return pre

def reverse_interval(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    """
    反转部分链表
    反转区间[a, b)的元素，注意左闭右开
    :param a:
    :param b:
    :return:
    """
    pre, cur, nxt = None, a, a
    # 对比reverse_2，改一下while终止条件就行了
    while cur != b:
        nxt = cur.next
        cur.next = pre
        # 继续向前移动
        pre = cur
        cur = nxt
    return pre

def reverseGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    【面试常问！！】
    25. K个一组翻转链表
    :param head:
    :param k:
    :return:
    """
    if not head:
        return None

    a, b = head, head
    for i in range(k):
        if not b:
            return head
        b = b.next
    # 反转前 k 个元素
    new_head = reverse_interval(a, b)
    a.next = reverseGroup(b, k)

    return new_head


class Solution:
    successor = None  # 后驱节点
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        【递归，背！！！】
        反转以 head 为起点的 n 个节点，返回新的头结点
        :param head:
        :return:
        """
        global successor
        if n == 1:
            # 记录第 n + 1个节点
            successor = head.next
            return head
        # 以 head.next 为起点，需要反转钱 n - 1个节点
        last = self.reverseN(head.next, n - 1)

        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        head.next = successor
        return last

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        92. 反转链表II
        :param head:
        :param left:
        :param right:
        :return:
        相关问题：
        206. 反转链表
        92. 反转链表II
        25. K 个一组翻转链表 【困难】
        思路：
        链表反转有两种实现方式：1. 递归反转； 2. 迭代反转
        分析：
        递归解法并不高效。虽然时间复杂度都是O(N)，但是递归需要堆栈，空间复杂度是O(N)
        递归的空间复杂度只是O(1)
        考虑效率的话，还是递归好
        """
        # 【递归反转】
        # base case
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head



