class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        return self.wordBreak_dfs(s, wordDict)

    def wordBreak_dp(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # dp[i] = True, if s[j:i] in words and dp[i] = True
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        i = 1
        while i <= len(s):
            j = i - 1
            while j >= 0:
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
                j -= 1
            i += 1
        return dp[len(s)]

    def wordBreak_bfs(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # BFS
        queue = [0]
        visited = set()
        while queue:
            begin = queue.pop(0)
            if begin not in visited:
                visited.add(begin)
                for end in range(begin + 1, len(s) + 1):
                    if s[begin:end] in wordDict:
                        queue.append(end)
                        if end == len(s):
                            return True
        return False

    def wordBreak_dfs(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # DFS
        def dfs(begin, check):
            if begin == len(s): return True
            if begin in check: return False
            for end in range(begin + 1, len(s) + 1):
                if s[begin:end] in wordDict:
                    if dfs(end, check): return True
            check.add(begin)
            return False

        return dfs(0, set())
