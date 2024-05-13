class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queueList = deque()
        newList = deque()
        ans = 0
        containsfresh = False
        directions = [[-1, 0], [1,0], [0, -1], [0, 1]]                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 2:
                    queueList.append([i, j])
                    visited.add((i, j))
        while queueList:
            element = queueList.popleft()
            for position in directions:
                leftPosition = element[0] + position[0]
                rightPosition = element[1] + position[1]
                if leftPosition in range(len(grid)) and rightPosition in range(len(grid[0])) and (leftPosition, rightPosition) not in visited and grid[leftPosition][rightPosition] == 1:
                    grid[leftPosition][rightPosition] = 2
                    visited.add((leftPosition, rightPosition))
                    newList.append([leftPosition, rightPosition])
            if len(queueList) == 0:
                if len(newList) > 0 : 
                    queueList = newList
                    newList = deque()
                    ans += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ((i,j) not in visited and grid[i][j] == 1):
                    return -1
        return ans

        
        
                    
        
            