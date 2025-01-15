class Solution:
   
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs( queue, visited):
            while queue:
                cell = queue.popleft()
                visited.add((cell[0], cell[1]))
                for dir in directions:
                    row = cell[0] + dir[0]
                    column = cell[1] + dir[1]
                    if row in range(len(heights)) and column in range(len(heights[0])) and (row, column) not in visited and heights[row][column] >= heights[cell[0]][cell[1]]:
                        queue.append([row, column])
                        visited.add((row, column))
            return visited

        pacificQueue = deque()
        atlanticQueue = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pacificQvisited = set()
        atlanticQvisited = set()
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pacificQueue.append([i, j])
                    pacificQvisited.add((i, j))
                if i == len(heights)-1 or j == len(heights[0]) -1:
                    atlanticQueue.append([i, j])
                    atlanticQvisited.add((i, j))
        pacificQueueVisited = bfs(pacificQueue, pacificQvisited)
        atlanticQueueVisited = bfs(atlanticQueue, atlanticQvisited)
        for row,column in atlanticQueueVisited:
            if (row, column) in pacificQueueVisited:
                res.append([row, column])
        return res 


        