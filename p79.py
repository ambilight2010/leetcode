class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x in range(len(board)):
            for y in range(len(board[x])):
                if self.exist_recursive(board, word, x, y):
                    return True
        return False

    def exist_recursive(self, board, word, x, y):
        if word == '': return True
        if not (0 <= x < len(board) and 0 <= y < len(board[x])): return False
        if board[x][y] == word[0]:
            c, board[x][y] = board[x][y], '##'
            word = word[1:]
            res = self.exist_recursive(board, word, x+1, y) \
                or self.exist_recursive(board, word, x, y+1) \
                or self.exist_recursive(board, word, x-1, y) \
                or self.exist_recursive(board, word, x, y-1)
            board[x][y] = c
            return res
        return False
