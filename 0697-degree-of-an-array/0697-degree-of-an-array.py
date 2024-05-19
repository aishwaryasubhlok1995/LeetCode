class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #find degree first and gather elements which is giving me that degree and comapre length
        dict = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in dict:
                tempArray = dict[nums[i]]
                tempArray[0] += 1
                tempArray[2]  = i - tempArray[1]
            else:
                dict[nums[i]] = [1, i, i]
        TtempArray = sorted(dict.values())
        TtempArray = TtempArray[::-1]
        FinalMinValue = math.inf
        degree = TtempArray[0][0]
        for i in TtempArray:
            if i[0] == degree:
                FinalMinValue = min(FinalMinValue, i[2])
            else:
                break
        if degree == 1:
            return 1
        return FinalMinValue + 1
      
        
       
            
            
                
            
            
        