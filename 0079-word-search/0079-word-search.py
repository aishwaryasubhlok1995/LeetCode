class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        k = 1
        curr = ''
        visited = set()
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def backtracking(i, j, pos):
            if len(word) == pos:
                return True 
            for d in dir:
                row = i + d[0]
                column = j + d[1]
                if row in range(len(board)) and column in range(len(board[0])) and (row, column) not in visited and  board[row][column] == word[pos]:
                    visited.add((row, column))
                    if backtracking(row, column, pos+1) == True:
                        return True 
                    visited.remove((row, column))
        


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    if backtracking(i, j, 1):
                        return True 
        return False
        