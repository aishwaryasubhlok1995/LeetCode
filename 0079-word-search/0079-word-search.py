class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def backtrack(i, j, counter, visited):
            if counter == len(word):
                return True
            for d in dir:
                row = i+d[0]
                column = j + d[1]
                if row in range(len(board)) and column in range(len(board[0])) and (row, column) not in visited and board[row][column] == word[counter]:
                    visited.add((row, column))
                    if backtrack(row, column, counter+1, visited) == True:
                        return True
                    visited.remove((row,column))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1, {(i,j)}) == True:
                        return True
        return False
        