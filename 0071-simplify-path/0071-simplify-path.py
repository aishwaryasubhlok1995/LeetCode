class Solution:
    def simplifyPath(self, path: str) -> str:
        returnStr = ''
        stack = []
        for i in (path.split('/')):
            if i == '..' and len(stack) > 0:            
                stack.pop(-1)
            elif i is not '' and i != '.' and i != '..':
                stack.append(i)
        if len(stack) == 0:
            return '/'
        for i in stack:
            returnStr += '/' + i
        return returnStr
        
        