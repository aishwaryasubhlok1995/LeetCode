class Solution:
    def simplifyPath(self, path: str) -> str:
        returnStr = ''
        stack = []
        for i in (path.split('/')):
            if i == '..':            
                if len(stack) >= 1:
                    stack.pop(-1)
            elif i is '.':
                continue
            elif i is not '':
                stack.append(i)
        if len(stack) == 0:
            return '/'
        for i in stack:
            returnStr += '/' + i
        return returnStr
        
        