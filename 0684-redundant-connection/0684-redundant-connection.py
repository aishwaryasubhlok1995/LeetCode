class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def checkCycle(source, node):
            for i in adjList[node]:
                if i not in visited:
                    visited.add(i)
                    if checkCycle(node, i):
                        return True
                elif i != source:
                    return True
            return False


        adjList = [[] for i in range(len(edges)+1)]
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
            visited = set()
            visited.add(e[0])
            if checkCycle(e[0], e[0]):
                return e 









