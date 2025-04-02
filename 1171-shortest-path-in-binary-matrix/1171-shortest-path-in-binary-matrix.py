class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        minLength = 1
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        direction = [[0,1], [1, 0], [0, -1], [-1, 0],[1, -1], [-1, -1], [-1, 1], [1, 1]]
        visited = set((0, 0))
        queueList = deque()
        queueList.append([0, 0, 1])
        while queueList:
            element = queueList.popleft()
            length = element[2]
            if element[0] == n-1 and element[1] == n-1:
                return length 
            for dir in direction:
                row =  element[0] + dir[0]
                column = element[1] + dir[1]
                if row in range(len(grid)) and column in range(len(grid[0])) and (row, column) not in visited and grid[row][column] == 0:   
                    visited.add((row, column))
                    queueList.append([row, column, length+1])
        return -1
            
