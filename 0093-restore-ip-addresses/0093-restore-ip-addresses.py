class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(start, parts, curStr):
            if len(parts) == 4 and start == len(s):
                res.append('.'.join(parts))
                return 
            if (len(parts)==4) or start>=len(s):
                return  
            curStr = curStr+s[start]
            if  (len(curStr) > 1 and curStr[0] == '0') or int(curStr) > 255:
                return
                
            parts.append(curStr) 
            backtrack(start+1, parts, "")
            parts.pop()
            backtrack(start+1, parts, curStr)
            
        backtrack(0, [], "")
        return res