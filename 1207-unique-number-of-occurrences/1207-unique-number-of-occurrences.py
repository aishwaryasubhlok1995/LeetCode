class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        l = set()
        for i in range(len(arr)):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            else:
                 dict[arr[i]] += 1
        for i in dict.values():
            if i not in l:
                l.add(i)
            else:
                return False
        return True
        
        