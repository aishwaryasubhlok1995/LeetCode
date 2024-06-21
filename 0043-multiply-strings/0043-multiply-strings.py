class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prod1 = 0
        prod2 = 0
        if len(num1) == 1 and len(num2) == 1:
            return str(int(num1)*int(num2))
        if len(num1) < len(num2):
            prod1 = num1
            prod2 = num2
        else:
            prod1 = num2
            prod2 = num1
        ans = 0
        prod1 = prod1[::-1]
        for i in range(len(prod1)):
            ans += int(prod2) * (int(prod1[i]) * 10**i)
        return str(ans)
       
            
        