class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stackArr = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            while len(stackArr) > 0 and temperatures[i] > stackArr[-1][0]:
                ans[stackArr[-1][1]] = i - stackArr[-1][1]
                stackArr.pop()
            stackArr.append([temperatures[i], i])

        return ans
                
            
            
            
               
                    
                
        