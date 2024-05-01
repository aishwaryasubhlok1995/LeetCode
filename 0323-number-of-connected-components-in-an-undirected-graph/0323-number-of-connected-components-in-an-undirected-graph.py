class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def bfs(i):
            visited[i] = True
            for node in (adj[i]):
                if visited[node] == False:
                    bfs(node)
        
        adj = [[] for i in range(n)]
        visited = [False]*n
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        counter = 0
        for i in range(len(adj)):
            if visited[i] == False:
                counter += 1
                bfs(i)
        return counter
            
        