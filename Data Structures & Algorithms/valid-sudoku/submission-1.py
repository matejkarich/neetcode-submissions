class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if self.hasDuplicate(board[i]):
                return False
        for row in range(len(board)):
            column = []
            for col in range(len(board)):
                column.append(board[col][row])
            if self.hasDuplicate(column):
                return False
        boxes = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in boxes[(i//3)+3*(j//3)] and board[i][j] != ".":
                    return False
                boxes[(i//3)+3*(j//3)].add(board[i][j])
        return True


    def hasDuplicate(self, lst):
        dic = defaultdict(int)
        for s in lst:
            dic[s] += 1
            if s != "." and dic[s] > 1:
                return True
        return False