class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.cachedNode = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        138. 随机链表的复制
        :param self:
        :param head:
        :return:
        思路：回溯算法 + 哈希表
        本题的难点在于，按照顺序遍历链表拷贝的时候，由于随机指针的存在，有可能【当前节点的随机指针指向的节点】还没有被创建出来。
        于是我们采用回溯的方法来解决这个问题。
        具体就是：让每个节点的拷贝操作相互独立。对于当前节点我们首先进行拷贝，然后我们进行【当前节点的后继节点】
        和【当前节点的随机指针指向的节点】的拷贝，拷贝完成后将创建的新节点的指针返回，即可完成当前节点的两指针赋值。
        具体地，使用哈希表记录每一个节点对应新节点的创建情况。遍历链表的过程中检查【当前节点的后继节点】和【当前节点的随机指针指向的节点】的创建情况，
        如果已经被创建则直接返回，如果不存在则递归地创建。
        拷贝完成，回溯到当前层时，我们即可完成当前节点的指针赋值。
        特别要注意判定当前节点为空的情况。
        """

        if not head:
            return None

        if not self.cachedNode.get(head):
            new_head = Node(head.val)
            self.cachedNode[head] = new_head
            new_head.next = self.copyRandomList(head.next)
            new_head.random = self.copyRandomList(head.random)

        return self.cachedNode.get(head)
