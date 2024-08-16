from typing import Optional

from Leetcode_top150.common import ListNode


def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    61.旋转链表
    给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
    思路：先找到倒数第k个节点b，然后把以b开头的链表加到原链表的前面
    :param self:
    :param head:
    :param k:
    :return:
    """
    n = k
    a, b = head, head
    while n > 0:
        n -= 1
        a = a.next

    if not a:
        return head

    while a.next:
        a = a.next
        b = b.next

    b.next = None
    a = b.next

    while a.next:
        a = a.next
    a.next = head
    return a
