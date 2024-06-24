class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dir = [[0,1], [1, 0], [-1, 0], [0, -1]]
        Originalcolor = image[sr][sc]
        visited = set()
        quelist = deque()
        if Originalcolor != color:
            quelist.append([sr, sc])
            visited.add((sr, sc))
            image[sr][sc] = color
        else:
            return image
        while quelist:
            element = quelist.popleft()
            for i in dir:
                newRow = (element[0] + i[0])
                newColumn = (element[1] + i[1]) 
                if newRow in range(len(image)) and newColumn in range(len(image[0])) and (newRow,newColumn) not in visited and image[newRow][newColumn] == Originalcolor:        
                    quelist.append([newRow,newColumn])
                    visited.add((sr, sc))
                    image[newRow][newColumn] = color
        return image
                    
                    
            
                
        