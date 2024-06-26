class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        listOfAvailbilty = []
        intervals = sorted(intervals)
        countOfRooms = 1
        listOfAvailbilty.append(intervals[0][1])
        heapq.heapify(listOfAvailbilty)
        for i in range(1, len(intervals)): 
            ans = heapq.nsmallest(1, listOfAvailbilty)
            if intervals[i][0] < ans[0]:
                countOfRooms += 1
                heapq.heappush(listOfAvailbilty, intervals[i][1])
            else:
                heapq.heapreplace(listOfAvailbilty, intervals[i][1])
        return countOfRooms
        
        
        
                    
            
            
            
            