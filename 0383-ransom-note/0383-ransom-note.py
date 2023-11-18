class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = list(magazine)
        for i in range (len(ransomNote)):
            if ransomNote[i] in arr:
                arr.remove(ransomNote[i])
            else:
                return False
        return True