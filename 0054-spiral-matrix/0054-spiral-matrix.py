class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        ans = []
        visited = set()
        i = 0
        j = 0
        ans.append(matrix[i][j]) 
        visited.add((i,j))
        pos = 0
        while True:
            i += directions[pos][0]
            j += directions[pos][1]
            if (i,j) not in visited and i in range(len(matrix)) and j in range(len(matrix[0])):
                ans.append(matrix[i][j]) 
                visited.add((i,j))
            else:
                i -= directions[pos][0]
                j -= directions[pos][1]
                pos = (pos+1)%4
                if len(ans) == len(matrix)*len(matrix[0]):
                    break
        return ans
                
                
            
            
                    
                
        