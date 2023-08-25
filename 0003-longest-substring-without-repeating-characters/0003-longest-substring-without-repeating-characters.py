class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        maxCounter = 1
        for x in range(len(s)):
            listOfchar = set()
            for i in range(x, len(s)):
                if s[i] not in listOfchar:
                    listOfchar.add(s[i])
                    #print(listOfchar)
                    maxCounter = max(len(listOfchar), maxCounter) 

                    #print("Current MaxLen={}".format(maxCounter))
                else:
                    maxCounter = max(len(listOfchar), maxCounter) 
                    #print(maxCounter)
                    break
        return maxCounter