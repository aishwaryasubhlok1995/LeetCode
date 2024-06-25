class Solution:
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
        ans = sorted(ans)
        print(dictDist)
        i = 0
        while len(finalAns) != k:
            temp = dictDist[ans[i]]
            for j in range(len(temp)):
                finalAns.append(temp[j])
            i += 1

        return finalAns