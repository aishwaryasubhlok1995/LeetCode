class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        queList = deque()
        adj = [[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])
        indegree = [0]*numCourses
        for i in adj:
            for j in i:
                indegree[j] +=  1
        for i in range(len(indegree)):
            if indegree[i] ==0:
                queList.append(i)
        while queList:
            node = queList.popleft()
            ans.append(node)
            for i in (adj[node]):
                indegree[i] -= 1
                if indegree[i] == 0:
                    queList.append(i)
        if len(ans) != numCourses:
            return []
        return ans
        

            
            