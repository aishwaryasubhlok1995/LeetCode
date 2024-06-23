class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        isNewinterval = False
        for i in range(len(intervals)):
            if  newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]:
                isNewinterval = True
                if newInterval[1] > intervals[i][1]:
                    newInterval = [intervals[i][0], newInterval[1]]
                else:
                    newInterval = [intervals[i][0], intervals[i][1]]
            elif newInterval[0] <= intervals[i][0] and  newInterval[1] >= intervals[i][1]:
                continue
            elif newInterval[1] >= intervals[i][0] and  newInterval[1] <= intervals[i][1]:
                isNewinterval = True
                if newInterval[0] < intervals[i][0]:
                    newInterval = [newInterval[0], intervals[i][1]]
                else:
                    newInterval = [intervals[i][0], intervals[i][1]]   
            else:
                ans.append([intervals[i][0], intervals[i][1]])
        ans.append(newInterval)
        return sorted(ans)
                    
                
        