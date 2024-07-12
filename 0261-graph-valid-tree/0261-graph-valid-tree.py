class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
       
        adj = [[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        visited = [False]*n
        visited[0] = True
        def checkTree(node, source):
            nodes = adj[node]
            for i in range(len(nodes)):
                if visited[nodes[i]] == False:
                    visited[nodes[i]] = True 
                    if checkTree(nodes[i], node) == False:
                        return False
                else:
                    if nodes[i] != source:
                        return False
        if checkTree(0, 0) == False:
            return False
        for i in range(n):
            if visited[i] == False:
                return False
        return True
        
                    
    
            
        