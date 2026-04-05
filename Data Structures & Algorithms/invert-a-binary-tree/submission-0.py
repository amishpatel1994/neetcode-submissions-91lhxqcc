# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        # recursively invert the left and right subtrees if present
        # swap the left and right nodes for this node
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        tmp = root.right
        root.right = root.left
        root.left = tmp

        return root
