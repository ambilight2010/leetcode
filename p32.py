class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.dp(s)

    def stack(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(': stack.append(i)
            else:
                if stack and s[stack[-1]] == '(': stack.pop(-1)
                else: stack.append(i)
        stack.append(len(s))
        max_count = 0
        prev = -1
        for pos in stack:
            max_count = max(max_count, pos - prev - 1)
            prev = pos
        return max_count

    def dp(self, s):
        """
        dp[i] =
           0, if s[i] == '('
           dp[i-1] + 2 + dp[i - dp[i-1] -2], if s[i] == ')' and s[i-dp[i-1]-1] == '('
        """
        max_count = 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
                max_count = max(max_count, dp[i])
        return max_count
