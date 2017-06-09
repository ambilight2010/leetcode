class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = init_trie(words)
        result = set()
        for x in range(len(board)):
            for y in range(len(board[x])):
                self.findWords_recursive(board, '', trie.root, x, y, result)
        return list(result)

    def findWords_recursive(self, board, word, node, x, y, result):
        if not (0 <= x < len(board) and 0 <= y < len(board[x])) or board[x][y] == '#': return
        word, board[x][y], c = word+board[x][y], '#', board[x][y]
        if c in node:
            node = node[c]
            if node['#']: result.add(word)
            self.findWords_recursive(board, word, node, x - 1, y, result)
            self.findWords_recursive(board, word, node, x + 1, y, result)
            self.findWords_recursive(board, word, node, x, y - 1, result)
            self.findWords_recursive(board, word, node, x, y + 1, result)
        board[x][y] = c


def init_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'#': False}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {'#': False}
            node = node[c]
        node['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return node['#']

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

