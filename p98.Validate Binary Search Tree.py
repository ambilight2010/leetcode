# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root, None, None)

    def dfs(self, node, min_node, max_node):
        if node is None: return True
        if min_node and min_node.val >= node.val: return False
        if max_node and node.val >= max_node.val: return False
        return self.dfs(node.left, min_node, node) and self.dfs(node.right, node, max_node)
