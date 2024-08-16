from typing import Optional

from Leetcode_top150.common import TreeNode


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    101. 对称二叉树
    :param root:
    :return:
    """
    if not root:
        return True

    if root.left and root.right:
        return isSymmetric(root.left) and isSymmetric(root.right)

    return False