class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            dic = Counter(row)
            for key, val in dic.items():
                if val > 1 and key != ".":
                    return False
        for c in range(len(board[0])):
            column = []
            for r in range(len(board)):
                column.append(board[r][c])
            dic = Counter(column)
            for key, val in dic.items():
                if val > 1 and key != ".":
                    return False
        squares = [[] for i in range(9)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                squares[3*(r//3)+(c//3)].append(board[r][c])
        for square in squares:
            dic = Counter(square)
            for key, val in dic.items():
                if val > 1 and key != ".":
                    return False
        return True

