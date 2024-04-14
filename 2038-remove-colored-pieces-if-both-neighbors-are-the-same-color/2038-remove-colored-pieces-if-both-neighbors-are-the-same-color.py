class Solution:
    
    def winnerOfGame(self, colors: str) -> bool:
        A = 0
        B = 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i+1] and colors[i-1] == 'A' and colors[i] == 'A':
                A += 1
            if colors[i-1] == colors[i+1] and colors[i-1] == 'B' and colors[i] == 'B':
                B += 1
        if A>B:
            return True
        return False
            
            
            
        