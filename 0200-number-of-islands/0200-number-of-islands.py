class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        dir = [[0,1], [1, 0], [-1, 0], [0, -1]]
        queueList = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    ans += 1
                    queueList.append([i, j])
                    while queueList:
                        element = queueList.popleft()
                        for d in dir:
                            x = d[0] + element[0]
                            y = d[1] + element[1]
                            if x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] == '1' and (x, y)  not in visited:
                                visited.add((x, y))
                                queueList.append([x, y])
        return ans




        