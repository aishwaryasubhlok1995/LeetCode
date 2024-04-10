class Solution:
    import heapq
    def minimumKeypresses(self, s: str) -> int:
        dict = {}
        res = 0
        countOfChar = 0
        for i in range(len(s)):
            if s[i] not in dict.keys():
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        print(heapq.nlargest(1, dict.keys(), dict.get))
        while len(dict):
            char = heapq.nlargest(1, dict.keys(), dict.get)
            print(char)
            countOfChar += 1
            if countOfChar <= 9:
                res = res + dict[char[0]]
            elif countOfChar <= 18:
                res += dict[char[0]]*2
            else:
                res += dict[char[0]]*3
            del dict[char[0]]
        return res
                
            
            
        
                
            
                
                
        