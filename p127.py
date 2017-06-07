class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from string import ascii_lowercase

        wordset = set(wordList)
        queue = [beginWord]
        distance = 0

        while queue:
            temp_queue = []
            while queue:
                word = queue.pop(0)
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    for c in ascii_lowercase:
                        w = word[:i] + c + word[i+1:]
                        if w in wordset:
                            wordset.remove(w)
                            temp_queue.append(w)
            distance += 1
            queue = temp_queue

        return 0
