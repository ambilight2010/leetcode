class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # return self.bfs(s)
        rml, rmr = 0, 0
        for c in s:
            if c == '(':
                rml += 1
            elif c == ')':
                if rml > 0: rml -= 1
                else: rmr += 1
        result = set()
        self.dfs(s, 0, result, rml, rmr, 0, '')
        return list(result)

    def dfs(self, s, i, result, rml, rmr, count, rs):
        """
        :param s: original string
        :param i: checking index
        :param result: set to storage result
        :param rml: most removed left pattern
        :param rmr: most removed right pattern
        :param count: count of left pattern
        :param rs: removed string
        """
        if rml < 0 or rmr < 0 or count < 0: return
        if i >= len(s):
            if rml == 0 and rmr == 0 and count == 0:
                result.add(rs)
            return
        if s[i] == '(':
            self.dfs(s, i + 1, result, rml, rmr, count + 1, rs + s[i])  # accept '('
            self.dfs(s, i + 1, result, rml - 1, rmr, count, rs)  # not accept '('
        elif s[i] == ')':
            self.dfs(s, i + 1, result, rml, rmr, count - 1, rs + s[i])  # accept ')'
            self.dfs(s, i + 1, result, rml, rmr - 1, count, rs)  # not accept ')'
        else:
            self.dfs(s, i + 1, result, rml, rmr, count, rs + s[i])  # not '(' or ')'

    def bfs(self, s):
        def is_valid(test_string):
            count = 0
            for c in test_string:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}
        while True:
            result = filter(is_valid, level)
            if result:
                return result
            level = {ts[:i] + ts[i+1:] for ts in level for i in range(len(ts))}
