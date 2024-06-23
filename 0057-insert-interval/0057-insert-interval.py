class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in intervals:
            if  newInterval[0] >= i[0] and newInterval[0] <= i[1]:
                if newInterval[1] > i[1]:
                    newInterval = [i[0], newInterval[1]]
                else:
                    newInterval = [i[0], i[1]]
            elif newInterval[0] <= i[0] and  newInterval[1] >= i[1]:
                    continue
            elif newInterval[1] >= i[0] and  newInterval[1] <= i[1]:
                if newInterval[0] < i[0]:
                    newInterval = [newInterval[0], i[1]]
                else:
                    newInterval = [i[0], i[1]]
                
            else:
                ans.append([i[0],i[1]])
        ans.append(newInterval)
        return sorted(ans)
                    
                
        