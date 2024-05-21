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
            print(intervals[i][1], ans[0])
            if intervals[i][0] < ans[0]:
                countOfRooms += 1
                print('here')
                heapq.heappush(listOfAvailbilty, intervals[i][1])
            else:
                print('her1e')
                heapq.heapreplace(listOfAvailbilty, intervals[i][1])
        return countOfRooms
        
        
        
                    
            
            
            
            