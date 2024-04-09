class Solution:
    import math
    def isHappy(self, n: int) -> bool:
        tempList = set()
        sumOfdigits = 0 
        while n>0:
            number = n%10
            sumOfdigits += number*number
            n = n//10
            if n == 0:
                beforeLength = len(tempList)
                if sumOfdigits == 1:
                    return True
                tempList.add(sumOfdigits)
                if beforeLength == len(tempList):
                    return False
                n = sumOfdigits
                sumOfdigits = 0
                
        
            