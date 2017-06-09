class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatch_greedy(s, p)

    def isMatch_dp(self, s, p):
        """
        dp[i][j] = dp[i-1][j-1] && (s[i]==p[j] || p[j]=='?'), p[j]!='*'
                 = dp[i-1][j] || dp[i][j-1]
        dp[0][j] = dp[0][j-1] && p[j]=='*'
        dp[0][0] = True
        dp[i][0] = False
        """
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j-1] and p[j-1] == '*'
            for i in range(1, len(s) + 1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[len(s)][len(p)]

    def isMatch_greedy(self, s, p):
        i = 0
        j = 0
        m = len(s)
        n = len(p)
        star = -1
        match = 0
        while i < m:
            if j < n and p[j] != '*' and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                match = i
                star = j
                j += 1
            elif star >= 0:
                match += 1
                i = match
                j = star + 1
            else:
                return False
        while j < n and p[j] == '*':
            j += 1
        return j == n

