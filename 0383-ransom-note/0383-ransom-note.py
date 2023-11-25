class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictMagazine = {}
        for i in range(len(magazine)):
            if magazine[i] in dictMagazine.keys():
                dictMagazine[magazine[i]]  += 1
            else:
                dictMagazine[magazine[i]] = 1
        for i in range(len(ransomNote)):
            if ransomNote[i] in dictMagazine.keys():
                dictMagazine[ransomNote[i]] -= 1
                if dictMagazine[ransomNote[i]] == 0:
                    dictMagazine.pop(ransomNote[i])
            else:
                return False
        return True