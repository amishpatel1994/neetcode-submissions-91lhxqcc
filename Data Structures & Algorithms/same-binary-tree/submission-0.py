# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if left and right is the same tree if present
        # check if the value is the same for both nodes
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False

        return p.val == q.val