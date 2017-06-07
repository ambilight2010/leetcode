class Solution(object):
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: bool
    #     """
    #     # dp[i] = True, if s[j:i] in words and dp[i] = True
    #     dp = [False for i in range(len(s) + 1)]
    #     dp[0] = True
    #     i = 1
    #     while i <= len(s):
    #         j = i - 1
    #         while j >= 0:
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break
    #             j -= 1
    #         i += 1
    #     return dp[len(s)]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # BFS
        queue = [0]
        visited = set()
        wordDict = set(wordDict)
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
