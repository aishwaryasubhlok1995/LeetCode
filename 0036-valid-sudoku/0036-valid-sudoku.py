class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #explore i and j for i to 3, and j to j+3
            #initially keep i stable and jsut extend j 
            # when j reaches 9- #increase I and make j to 0 
            
        visitedDict = {}
        i = 0 
        j = 0 
        for i in range(0, 9):
            visitedI = set()
            vistedJ = set()
            for j in range(0, 9):
                if board[i][j] != '.':
                    if board[i][j] not in visitedI:
                        visitedI.add(board[i][j])
                    else:
                        return False
                    key = (3*(i//3) + (j//3))
                    if key not in visitedDict:
                        visitedDict[key] = set(board[i][j])
                    else:
                        keySet = visitedDict[key]
                        if board[i][j] in keySet:
                            return False
                        visitedDict[key].add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] not in vistedJ:
                        vistedJ.add(board[j][i])
                    else:
                        return False
                    
        return True
                    
                
                
                            
            
        