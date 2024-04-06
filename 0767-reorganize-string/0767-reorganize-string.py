class Solution:
    import heapq
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        dict = {}
        finalRes = ''
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1        
        while len(dict.keys())> 0 :
            arr = heapq.nlargest(2, dict.keys(), dict.get)
            if finalRes == '':
                finalRes += arr[0]
                dict[arr[0]] -= 1
            if len(arr) == 1 and finalRes[-1] == arr[0]:
                return ""
            if finalRes[-1] != arr[0]:
                finalRes += arr[0]
                dict[arr[0]] -= 1
            if len(arr) > 1 and finalRes[-1] != arr[1]:
                finalRes += arr[1]
                dict[arr[1]] -= 1
            print(dict)
            if dict[arr[0]] == 0:
                del dict[arr[0]]
            if len(arr) > 1 and dict[arr[1]] == 0:
                del dict[arr[1]]
        if dict == {}:
            return finalRes
            
            
            
            
            
            
            
       

                
        