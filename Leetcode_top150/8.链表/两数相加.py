from typing import Optional

from Leetcode_top150.common import ListNode


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    2. 两数相加
    思路：
    1. 将两个链表先变成长度相同再进行遍历，方法是在短链表前面补0
    2. 每一位计算的同时需要考虑上一位的进位。当前位计算完后同样需要更新进位值
    3. 两个列表遍历完之后进位值为1，则在新链表最前方添加节点1
    :param l1:
    :param l2:
    :return:
    """
    dummy = ListNode(-1)
    cur = dummy
    carry = 0  # 表示进位
    while l1 or l2:  # 只要l1或l2有一个没遍历完就接着遍历
        # 如果短链表已经遍历完但长链表还没遍历完大情况下，把短链看做该位有数0进行遍历
        x = 0 if not l1 else l1.val
        y = 0 if not l2 else l2.val
        # 求出当前位置的和
        sum = x + y + carry

        carry = sum // 10  # 更新当前进位
        sum %= 10  # 计算当前位的值
        # 创建一个新的节点，值为sum模10后的结果
        cur.next = ListNode(sum)
        cur = cur.next
        # 如果链表还有下一位则前进
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    # 判断最后一位有无进位
    if carry == 1:
        cur.next = ListNode(carry)

    return dummy.next

