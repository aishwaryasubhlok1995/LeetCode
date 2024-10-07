class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []
        current = []
        def backtrack(i):
            if i==len(s):
                final.append(current.copy())
                return
            for j in range(i,len(s)):
                curStr = s[i:j+1] 
                if curStr == curStr[::-1]:
                    current.append(curStr)
                    backtrack(j+1)
                    current.pop()
        
        backtrack(0)
        return final