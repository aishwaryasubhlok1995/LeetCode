class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        finalString = ''
        stack.append([s[0],1])
        for i in range(1, len(s)):
            if len(stack) > 0 and stack[-1][0] == s[i]:
                tempArr = stack.pop()
                element = tempArr[1] +1
                if element != k:
                    stack.append([s[i],element])
            else:
                stack.append([s[i],1])
        for i in range(len(stack)):
            for j in range(stack[i][1]):
                finalString += stack[i][0] 
        return finalString
            

            
            
            
        