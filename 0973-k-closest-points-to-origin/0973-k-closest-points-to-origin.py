class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = [] 
        finalAns = []
        dictDist = {}
        def ksqrt(x, y):
            return(sqrt((y*y) + (x*x)))
        for i in points:
            value = (ksqrt(i[0], i[1]))
            if value not in dictDist:
                dictDist[value] = [[i[0], i[1]]]
            else:
                dictDist[value].append([i[0], i[1]])
            ans.append(value)
        heapq.heapify(ans)
        while len(finalAns) != k:
            x = heapq.heappop(ans)
            temp = dictDist[x]
            for j in range(len(temp)):
                finalAns.append(temp[j])
        return finalAns