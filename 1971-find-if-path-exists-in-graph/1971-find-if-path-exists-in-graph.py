class Solution:
    def checkPath(self, adj, source, destination, visited):
        if source == destination:
            return True
        visited[source] = True
        for node in adj[source]:
            if visited[node] == False:
                if self.checkPath(adj, node, destination, visited):
                    return True
        return False
        
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for i in range(n)]
        visited = [False]*n
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1]) 
            adj[edges[i][1]].append(edges[i][0])
        return self.checkPath(adj, source, destination, visited)
        
            
        
    