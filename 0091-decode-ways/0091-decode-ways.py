class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        arr = [1]*(len(s)+1)
        for i in range(len(s)-1, -1, -1):
            arr[i] = arr[i+1]
            if s[i] == '0':
                arr[i] = 0
            elif i+1 < len(s) and ((s[i] == '1')  or (s[i] == '2' and s[i+1] in ['0', '1', '2', '3', '4', '5', '6'])):
                arr[i] +=  arr[i+2]
        return arr[0]