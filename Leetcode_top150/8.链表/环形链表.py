from typing import Optional

from Leetcode_top150.common import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    """
    141. 环形链表
    :param head: 链表的头结点
    :return:
    """

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
