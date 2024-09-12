class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsHeapList = []
        ansList = []
        for i in points:
            value = i[0]*i[0] + i[1]*i[1]
            heapq.heappush(pointsHeapList, [-value, i])
            if len(pointsHeapList) > k:
                 heapq.heappop(pointsHeapList)
        for i in pointsHeapList:
            ansList.append(i[1])
        return ansList
            
        
            
        