class Solution:
    def isHappy(self, n: int) -> bool:
        setOfNo = set()
        def isCheck(n, setOfNo):
            if n == 1:
                return True
            sumDigits = 0
            while n >= 1:
                digit = n%10
                n = n//10
                sumDigits += digit*digit
            if sumDigits in setOfNo:
                print('hello', sumDigits)
                return False
            setOfNo.add(sumDigits)
            return isCheck(sumDigits, setOfNo)
        return isCheck(n, setOfNo)
        
       
        
        