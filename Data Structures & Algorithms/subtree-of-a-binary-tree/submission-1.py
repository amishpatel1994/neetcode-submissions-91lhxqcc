# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        
        # check if current node matches subroot
        if self.isSameTree(root, subRoot):
            return True
        # check if left node has subroot
        if self.isSubtree(root.left, subRoot):
            return True
        # check if right node has sub root
        if self.isSubtree(root.right, subRoot):
            return True

        return False

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