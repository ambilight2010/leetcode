# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.bfs(root)

    def bfs(self, root):
        if root is None: return []
        queue = [root]
        result = []
        m = {}
        while queue:
            node = queue.pop(0)
            if node.val not in m:
                m[node.val] = 0
            m[node.val] += 1
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        most = 0
        for k in m:
            if m[k] > most:
                most = m[k]
        for k in m:
            if m[k] == most:
                result.append(k)
        return result
