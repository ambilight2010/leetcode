class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        m = {')': '(', ']': '[', '}': '{'}
        left = {'(', '[', '{'}
        for c in s:
            if c in left: stack.append(c)
            elif not stack or m[c] != stack.pop(-1): return False
        if stack: return False
        return True
