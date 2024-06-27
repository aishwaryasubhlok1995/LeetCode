class Solution:
    import heapq
    def longestPalindrome(self, s: str) -> int:
        dictOfChar = {}
        oddElement = False
        count = 0
        for i in s:
            if i not in dictOfChar:
                dictOfChar[i] = 1
            else:
                dictOfChar[i] += 1
        for i in dictOfChar:
            if dictOfChar[i] % 2 == 0:
                count += dictOfChar[i]
            else:
                oddElement = True
                if dictOfChar[i] > 1:
                    count += dictOfChar[i] - 1
        if oddElement:
            return count + 1
        return count
        
            
        
        