from typing import Optional

from Leetcode_top150.common import ListNode


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """
    86. 分隔链表
    :param head:
    :param x:
    :return:
    """
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    p1, p2 = dummy1, dummy2
    p = head
    while p:
        if p.val >= x:
            p2.next = p
            p2 = p2.next
        else:
            p1.next = p
            p1 = p1.next
        temp = p.next
        p.next = None
        p = temp
    # 连接两个链表
    p1.next = dummy2.next

    return dummy1.next


