from typing import Optional

from Leetcode_top150.common import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    100. 相同的数
    :param p:
    :param q:
    :return:
    """
    if not p and not q:
        return True

    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False