class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA = 0
        countB = 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i+1] == colors[i]:
                if colors[i] == 'A':
                    countA += 1
                else:
                    countB += 1
            
        if countA > countB:
            return True
        return False
            
            
        