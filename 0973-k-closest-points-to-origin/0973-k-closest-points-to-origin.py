class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = [] 
        finalAns = []
        heapq.heapify(ans)
        def ksqrt(x, y):
            return(-sqrt((y*y) + (x*x)))
        for i in points:
            value = (ksqrt(i[0], i[1]))
            if len(ans) < k:
                heapq.heappush(ans, (value, i[0], i[1]))
            else:
                if ans[0][0] < value:
                    heapq.heappop(ans)
                    heapq.heappush(ans, (value, i[0], i[1]))
        for i in range(len(ans)):
            finalAns.append([ans[i][1], ans[i][2]])
        return finalAns