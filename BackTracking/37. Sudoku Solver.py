class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C):
                if board[r][c] == '.':
                    for ch in '123456789':
                        if self.isValid(board, r, c, ch):
                            board[r][c] = ch
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[r][c] = '.'
                    return False
        return True

    def isValid(self, board, r, c, ch):
        for i in range(9):
            if board[i][c] == ch:
                return False
            if board[r][i] == ch:
                return False
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch:
                return False
        return True
