class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
        stackList = []
        for i in range(len(s)):
            if (s[i]=='(' or s[i]=='['or s[i]=='{') :
                stackList.append(s[i])
            else:
                if len(stackList) == 0:
                    return False
                else:
                    if s[i] ==')' and stackList.pop() != '(':
                        return False
                    if s[i] ==']' and stackList.pop() != '[':
                        return False
                    if s[i] == '}' and  stackList.pop() != '{':
                        return False
        if len(stackList) == 0:
            return True
        else:
            return False
            
            