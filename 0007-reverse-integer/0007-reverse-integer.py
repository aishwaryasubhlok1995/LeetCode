class Solution:
    def reverse(self, x: int) -> int:
        reverseNo = 0
        negative = False
        if x<0:
            x = x*-1
            negative = True
        while x>0:
            reverseNo = reverseNo*10 + x%10
            x = x//10
        if reverseNo > (2**31):
            return 0
        if negative:
            return -1*reverseNo
        return reverseNo
        