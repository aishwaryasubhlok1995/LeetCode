class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boards = []
        for i in range(len(board)):
            boards.append(set())
        for i in range(len(board)):
            row = set()
            columns = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in columns:
                        return False
                    columns.add(board[j][i])
                pos = (3*(i//3)) + (j//3)
                if board[i][j] != '.':
                    if board[i][j] in boards[pos]:
                        return False
                    boards[pos].add(board[i][j])  
                    
        return True
            
        