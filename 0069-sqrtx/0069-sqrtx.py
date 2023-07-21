class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x          
        while low<=high:
            mid = (low+high)//2
            sqMid = mid*mid
            sqNext=(mid+1)*(mid+1)
            if sqMid <= x and sqNext>x:
                return mid
            elif sqMid>x:
                high = mid-1
            else:
                low=mid+1