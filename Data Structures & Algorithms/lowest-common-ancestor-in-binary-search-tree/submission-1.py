# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root
        # get list of nodes to get to p
        p_list = self.search(root, p)
        q_list = self.search(root, q)

        common_ancestor = p_list[0]
        for i in range(1, min(len(p_list), len(q_list))):
            if p_list[i].val == q_list[i].val:
                common_ancestor = p_list[i]
            else:
                break

        return common_ancestor
        


        # get list of nodes to get to q
        # find the lowest comment ancestor by comparing the list

    def search(self, node, target):
        tmp_node = node
        cache = []
        while tmp_node.val != target.val:
            cache.append(tmp_node)
            if target.val < tmp_node.val:
                tmp_node = tmp_node.left
            else:
                tmp_node = tmp_node.right
        cache.append(target)

        return cache



