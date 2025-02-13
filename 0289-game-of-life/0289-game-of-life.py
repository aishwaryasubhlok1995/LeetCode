class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0,1], [1, 0], [0, -1], [-1, 0], [-1,1], [-1, -1], [1, -1], [1, 1]]
        def countOnes(i, j): 
            noOnes = 0        
            for dir in directions:
                row = dir[0] + i
                column = dir[1] + j 
                if row in range(0, len(board)) and column in range(len(board[0])):
                    if board[row][column] == 1 or board[row][column] == 'Y':
                        noOnes += 1
            return noOnes
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                noOfOnes = countOnes(i, j)
                if board[i][j] == 1 and (noOfOnes < 2 or noOfOnes > 3):
                    board[i][j] = 'Y'
                elif (board[i][j] == 0) and (noOfOnes == 3):
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    board[i][j] = 1 
                elif  board[i][j] == 'Y':
                    board[i][j] = 0 
        
        

        