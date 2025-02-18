class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        queueList = deque()
        def bfs(queueList, visited):
            while queueList:
                i, j = queueList.popleft()
                for dir in directions:
                    row = i + dir[0]
                    column = j + dir[1]
                    if row in range(len(mat)) and column in range(len(mat[0])) and (row, column) not in visited:
                        queueList.append([row, column])
                        visited.add((row, column))
                        mat[row][column] = mat[i][j] + 1


        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queueList.append([i, j])
                    visited.add((i, j))
        bfs(queueList, visited)
        return mat

        