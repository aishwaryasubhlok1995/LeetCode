class Solution:
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def detectCycle(curr, source):
            visited[curr] = True
            for node in adj[curr]:
                if visited[node] == False:
                    if detectCycle(node, curr):
                        return True
                    else:
                        detectCycle(node, curr)
                elif visited[node] == True and node != source:
                    print('i am in', node ,source)
                    return True
                
        
        visited = [False]*n
        adj = [[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        source = 0
        counter = 0
        for i in range(n):
            if visited[i] == False:
                counter += 1
                if counter >= 2:
                    return False
                if detectCycle(source, source):
                    return False
        return True
        
        
        