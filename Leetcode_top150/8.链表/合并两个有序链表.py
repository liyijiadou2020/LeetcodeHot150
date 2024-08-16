from typing import Optional

from Leetcode_top150.common import ListNode


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    21. 合并两个有序链表
    :param list1:
    :param list2:
    :return:
    """
    p1 = list1
    p2 = list2
    dummy = ListNode(-1)
    p = dummy
    while p1 and p2:
        if p1.val <= p2.val:
            p.next = ListNode(p1.val)
            p1 = p1.next
        else:
            p.next = ListNode(p2.val)
            p2 = p2.next
        p = p.next

    while p1:
        p.next = ListNode(p1.val)
        p1 = p1.next
        p = p.next

    while p2:
        p.next = ListNode(p2.val)
        p2 = p2.next
        p = p.next

    return dummy.next

