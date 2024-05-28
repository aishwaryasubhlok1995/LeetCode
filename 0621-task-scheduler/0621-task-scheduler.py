class Solution:
    import heapq
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict = {}
        ans = ''
        dictCycles = {}
        for i in tasks:
            if i not in dict:
                dict[i] = 1
                dictCycles[i] = 0
            else:
                dict[i] += 1
        while dict:
            element = (heapq.nlargest(len(dict), dict.keys(), key= dict.get))
            dictKey = ''
            for i in element:
                if dictCycles[i] == 0: 
                    dictKey = i
                    dictCycles[i] = n
                    ans += dictKey
                    break
            if dictKey == '':
                ans += 'I'
            else:
                dict[dictKey] -= 1
            if len(ans) > 1:
                for char in dictCycles:
                    if char != dictKey and dictCycles[char] > 0:
                        dictCycles[char] -= 1
            if dict[i] == 0:
                del dict[i]
        return len(ans)
            
            
        
            