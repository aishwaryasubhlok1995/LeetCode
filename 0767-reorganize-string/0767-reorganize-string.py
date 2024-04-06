class Solution:
    import heapq
    def reorganizeString(self, s: str) -> str:
        dict = {}
        finalRes = ''
        prevChar = None
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1 
                
        while len(dict)> 0 :
            arr = heapq.nlargest(2, dict.keys(), dict.get)
            if len(arr) == 1 and dict[arr[0]] > 1:
                return ""
            if prevChar == None or prevChar != arr[0]:
                finalRes += arr[0]
                curChar = arr[0]
            else:
                finalRes += arr[1]
                curChar = arr[1]
            prevChar = curChar
            if dict[curChar]>1:
                dict[curChar] = dict[curChar]-1
            else:
                del dict[curChar]
        return finalRes
            
            
            
            
            
            
            
       

                
        