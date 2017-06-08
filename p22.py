class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.bt(n, n, 0, [None] * (2 * n), result)
        return result

    def bt(self, left, right, cur, plist, result):
        if cur == len(plist):
            result.append(''.join(plist))
        if left > 0:
            plist[cur] = '('
            self.bt(left - 1, right, cur + 1, plist, result)
        if right > left:
            plist[cur] = ')'
            self.bt(left, right - 1, cur + 1, plist, result)
