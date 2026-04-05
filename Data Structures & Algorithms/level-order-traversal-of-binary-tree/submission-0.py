# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # Need to perform BFS (queues)
        # For each level, add the queue contents to res and then consume
        res = [[root.val]]
        curr_level_queue = [root]
        next_level_queue = []
        while len(curr_level_queue) > 0 or len(next_level_queue) > 0:
            if len(curr_level_queue) == 0:
                res.append([node.val for node in next_level_queue])
                curr_level_queue = next_level_queue
                next_level_queue = []

            node = curr_level_queue.pop(0)
            if node.left:
                next_level_queue.append(node.left)
            if node.right:
                next_level_queue.append(node.right)
        return res
        