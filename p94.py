# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # result = []
        # self.dfs(root, result)
        # return result
        return self.iterative(root)

    def dfs(self, node, result):
        if node is None: return
        self.dfs(node.left, result)
        result.append(node.val)
        self.dfs(node.right, result)

    def iterative(self, root):
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            result.append(node.val)
            node = node.right
        return result
