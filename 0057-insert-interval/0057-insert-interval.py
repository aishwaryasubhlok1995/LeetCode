class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not len(intervals):
            return [newInterval]
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
            if i == len(intervals)-1:
                intervals.insert(i+1, newInterval)
        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1] = [min(intervals[i][0], ans[-1][0]), max(intervals[i][1], ans[-1][1])]
            else:
                ans.append(intervals[i])
        return  ans            