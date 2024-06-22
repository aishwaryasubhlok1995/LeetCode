class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=itemgetter(1))
        prev = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev:
                count += 1
            else:
                prev = intervals[i][1] 
        return count
        