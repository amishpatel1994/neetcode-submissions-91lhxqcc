# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # max depth is max of maxDepth of left and right nodes
        # if a leaf node is detected, return 1
        if root.left is None and root.right is None:
            return 1

        max_depth = 0
        if root.left:
            max_depth = max(max_depth, 1 + self.maxDepth(root.left))

        if root.right:
            max_depth = max(max_depth, 1 + self.maxDepth(root.right))

        return max_depth