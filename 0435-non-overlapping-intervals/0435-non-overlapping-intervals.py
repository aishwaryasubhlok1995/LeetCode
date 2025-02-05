class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        i = 1
        count = 0
        prev = 0
        while i < len(intervals):
            if intervals[i][0] < intervals[prev][1]:
                count += 1
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
            else:
                prev = i 
            i += 1    
        return count