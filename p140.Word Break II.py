class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        list_list_word = self.dfs(s, wordDict, 0, {})
        result = []
        for list_word in list_list_word:
            list_word.reverse()
            result.append(' '.join(list_word))
        return result

    def dfs(self, s, wordDict, begin, m):
        if begin == len(s):
            return [[]]
        result = []
        for end in range(begin + 1, len(s) + 1):
            w = s[begin:end]
            if w in wordDict:
                if end in m:
                    list_list_word = m[end]
                else:
                    list_list_word = self.dfs(s, wordDict, end, m)
                for list_word in list_list_word:
                    result.append(list_word + [w])
        m[begin] = result
        return result
