class Solution:
    def checkPath(self, adj, source, destination, visited):
        arr = deque()
        visited[source] = True
        arr.append(source)
        while arr:
            source = arr.popleft()
            if source == destination:
                return True
            for n in adj[source]:
                if visited[n] == False:
                    visited[n] = True
                    arr.append(n)
                
            
                   
        
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        visited = [False]*n
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1]) 
            adj[edges[i][1]].append(edges[i][0])
        return self.checkPath(adj, source, destination, visited)
        
            
        
    