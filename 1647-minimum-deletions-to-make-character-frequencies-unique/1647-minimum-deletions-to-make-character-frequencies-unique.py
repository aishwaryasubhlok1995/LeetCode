class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = set(s)
        result = []
        for i in arr:
            count = 0
            for j in range(len(s)):
                if s[j] == i:
                    count += 1
            result.append(count)
        tempArr = set()
        res = 0
        for i in range(len(result)):
            while result[i] in tempArr:
                result[i] =  result[i] - 1
                res += 1
                if result[i] == 0:
                    break
            tempArr.add(result[i])
        return res
            
                    
                    
        
    
                
        