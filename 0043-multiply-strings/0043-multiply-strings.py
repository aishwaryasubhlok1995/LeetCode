class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prod1 = 0
        prod2 = 0
        if len(num1) == 1 and len(num2) == 1:
            return str(int(num1)*int(num2))
        if len(num1) < len(num2):
            prod1 = num1
            prod2 = int(num2)
        else:
            prod1 = num2
            prod2 = int(num1)
        ans = 0
        for i in range(len(prod1)):
            ans += prod2 * (int(prod1[i]) * 10 **(len(prod1) - i-1))
        return str(ans)