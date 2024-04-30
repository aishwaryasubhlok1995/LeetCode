class Solution:
     
    def bfs(self, r, c, visited, grid):
        directions = [[1,0],[-1, 0], [0, 1], [0, -1]]
        queuelist = deque()
        queuelist.append([r,c])
        visited.add((r,c))
        while queuelist:
            curr = queuelist.popleft()
            for d in (directions):
                row = curr[0]+d[0]
                column = curr[1]+d[1]
                if (row in range(len(grid))) and (column in range(len(grid[0]))) and (row,column) not in visited and grid[row][column] == '1':
                    queuelist.append([row, column])
                    visited.add((row, column))
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        if grid is None:
            return 
        visited = set()  
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visited:
                    self.bfs(r,c, visited, grid)
                    island += 1
        return island
                
                    
        