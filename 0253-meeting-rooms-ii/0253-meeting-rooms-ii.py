class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetingRooms = 1 
        intervals = sorted(intervals)
        meetingArray = [intervals[0][1]]

        for i in range(len(intervals)):
            if i >= 1:
                if intervals[i][0] < meetingArray[0]:
                    meetingRooms += 1
                    meetingArray.append(intervals[i][1])
                else:
                    meetingArray[0] = intervals[i][1]
            meetingArray = sorted(meetingArray)   
        return meetingRooms
                    
            
            
            
            