class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [[0,1], [1, 0], [-1, 0], [0, -1]]
        Originalcolor = image[sr][sc]
        rowLen = len(image)
        colLen = len(image[0])
        visited = set()
        quelist = deque()
        quelist.append([sr, sc])
        visited.add((sr, sc))
        image[sr][sc] = color
        while quelist:
            element = quelist.popleft()
            for i in dir:
                newRow = (element[0] + i[0])
                newColumn = (element[1] + i[1]) 
                if newRow in range(rowLen) and newColumn in range(colLen) and (newRow,newColumn) not in visited and image[newRow][newColumn] == Originalcolor:        
                    quelist.append([newRow,newColumn])
                    visited.add((newRow, newColumn))
                    image[newRow][newColumn] = color
        return image
                    
                    
            
                
        