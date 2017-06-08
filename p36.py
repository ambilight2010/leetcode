class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        block = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i] \
                      or board[i][j] in col[j] \
                      or board[i][j] in block[i//3*3 + j//3]:
                        return False
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[i//3*3 + j//3].add(board[i][j])
        return True
