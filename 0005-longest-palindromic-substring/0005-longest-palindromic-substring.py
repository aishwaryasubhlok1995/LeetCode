class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultString = ''
        for i in range(len(s)):
            Initialstring = s[i]
            for j in range(i+1, len(s)):
                Initialstring += s[j]
                if Initialstring == Initialstring[::-1] and len(Initialstring) > len(resultString):
                    resultString = Initialstring
        if resultString == "" and len(Initialstring) >= 1:
            resultString = Initialstring
        return resultString
                    
                