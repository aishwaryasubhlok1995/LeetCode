class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        listIndexesToRemove = []
        i =1
        while i < len(intervals):
            print(intervals[i], intervals[i-1])
            if intervals[i-1][1] >= intervals[i][0]:
                end = intervals[i][1] if intervals[i][1] >intervals[i-1][1] else intervals[i-1][1]
                intervals[i] = [intervals[i-1][0], end]
                intervals.pop(i-1)
            else:
                i = i+1
        return intervals
    
        