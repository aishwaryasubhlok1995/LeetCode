class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        ans = []
        queuelist = deque()
        for i in prerequisites:
            adj[i[1]].append(i[0])
        print(adj)
        #calculate indegrees
        indegrees = [0]*numCourses
        for i in adj:
            for j in range(len(i)):
                indegrees[i[j]] += 1
        print(indegrees)
        for i in range(numCourses):
            if indegrees[i] == 0:
                queuelist.append(i)
        while queuelist:
            node = queuelist.popleft()
            ans.append(node)
            for i in adj[node]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queuelist.append(i)
        if len(ans) != numCourses:
            return []
        return ans
        
        
        