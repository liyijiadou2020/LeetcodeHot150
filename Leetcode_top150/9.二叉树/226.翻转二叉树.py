from typing import Optional
from Leetcode_top150.common import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    226. 翻转二叉树
    :param root:
    :return:
    """
    if not root:
        return None

    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left = right
    root.right = left

    return root
