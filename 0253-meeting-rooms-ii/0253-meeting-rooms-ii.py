class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetingRooms = 1 
        intervals = sorted(intervals)
        print(intervals)
        meetingArray = [intervals[0][1]]
        heapq.heapify(meetingArray)
        for i in range(1, len(intervals)):
            if intervals[i][0] < meetingArray[0]:
                meetingRooms += 1
            else:
                heapq.heappop(meetingArray)
            heapq.heappush(meetingArray,intervals[i][1])    
        return meetingRooms
                    
            
            
            
            