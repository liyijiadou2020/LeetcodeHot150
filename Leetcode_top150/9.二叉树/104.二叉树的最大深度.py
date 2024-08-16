
from typing import Optional

from Leetcode_top150.common import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    104. 二叉树的最大深度
    :param root:
    :return:
    """
    if not root:
        return 0

    max_depth = max(maxDepth(root.right), maxDepth(root.left)) + 1

    return max_depth

