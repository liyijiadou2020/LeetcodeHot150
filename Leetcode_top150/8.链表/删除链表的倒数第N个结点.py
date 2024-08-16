from typing import Optional

from Leetcode_top150.common import ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    19. 删除链表的倒数第N个结点
    :param head:
    :param n:
    :return:
    思路：
    前后两个指针，初始化前后两个指针都指向head
    前面的指针先走n步，然后两个指针同时向前走
    直到前面的指针指向null停止
    删除后面的指针指向的节点
    """
    if not head:
        return head
    # a先走n步i，然后a、b同时一起出发，直到a.next 为空，此时b指向要删除的节点的前一个节点
    a, b = head, head
    count = n
    while count > 0:
        count -= 1
        a = a.next

    if not a:  # 把链表的头删掉
        head = head.next
        return head

    while a and a.next:
        a = a.next
        b = b.next

    # 此时b指向要删除节点的前一个节点
    b.next = b.next.next
    return head




