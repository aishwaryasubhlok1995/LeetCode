class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        numprocessed = 0
        queueList = deque()
        for i in prerequisites:
            adj[i[1]].append(i[0])
        print(adj)
        degree = [0]*numCourses
        for i in adj:
            for j in range(len(i)):
                degree[i[j]] += 1
        print(degree)
        for i in range(numCourses):
            if degree[i] == 0:
                queueList.append(i)
        print(queueList)
        while queueList:
            node = queueList.popleft()
            numprocessed += 1
            for i in range(len(adj[node])):
                degree[adj[node][i]] -= 1
                if degree[adj[node][i]] == 0:
                     queueList.append(adj[node][i])
        if numprocessed == numCourses:
            return True
        return False
                
            
        
                
        
        