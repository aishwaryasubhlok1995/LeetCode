class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        res.append(newInterval)
        while i < len(intervals):
            if intervals[i][0] <= res[-1][1]:
                res[-1] =([min(intervals[i][0], res[-1][0]), max(intervals[i][1], res[-1][1])])
            else:
                res.append(intervals[i])
            i += 1
        return res









        