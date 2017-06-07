class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
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
