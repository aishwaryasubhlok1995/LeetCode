class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num2 = int(num2)
        ans = 0
        num1 = num1[::-1]
        for i in range(len(num1)):
            ans += num2 * (int(num1[i]) * 10**i)
        return str(ans)
       
            
        