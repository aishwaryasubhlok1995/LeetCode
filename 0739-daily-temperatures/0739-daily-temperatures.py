class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stackArr = []
        for i in range(len(temperatures)):
            stackArr.append([temperatures[i], i])
            if len(stackArr) >= 2:
                i = -2
                while abs(i) <= len(stackArr):
                    if stackArr[i][0] < stackArr[-1][0]:
                        ans[stackArr[i][1]] = stackArr[-1][1] - stackArr[i][1]
                        stackArr.pop(i)
                    else:
                        break
        return ans
                
            
            
            
               
                    
                
        