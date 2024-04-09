class Solution:
    import math
    def getSquareOfdigit(self, n):
        sumOfdigits = 0
        while n>0:
            number = n%10
            sumOfdigits += number*number
            n = n//10
        return sumOfdigits
        
    def isHappy(self, n: int) -> bool:
        tempList = set()
        while n>0:
            sumOfdigits = self.getSquareOfdigit(n)
            beforeLength = len(tempList)
            if sumOfdigits == 1:
                return True
            tempList.add(sumOfdigits)
            if beforeLength == len(tempList):
                return False
            n = sumOfdigits
                
        
            