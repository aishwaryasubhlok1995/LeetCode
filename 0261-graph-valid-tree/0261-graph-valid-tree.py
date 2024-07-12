class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0 and n == 1:
            return True
        elif len(edges) == 0:
            return False
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
            return True
        counter = 0
        isChecked = False
        for i in range(n):
            if visited[i] == False:
                counter += 1
                isChecked = checkTree(0, 0)
                if counter >= 2:
                    break
        if counter >= 2:
            return False
        return isChecked
                    
    
            
        