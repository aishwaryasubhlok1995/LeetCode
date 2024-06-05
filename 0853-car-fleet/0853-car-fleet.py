class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #car who is ahead should be slower than car who is behind but faster = together fleet 
        #car who is behind but even taking longer duration - they are alone 
        newPositions = []
        for i in range(len(position)):
            newPositions.append([position[i], speed[i]])
        newPositions = sorted(newPositions)
        newPositions = newPositions[::-1]
        arr = [(target - newPositions[0][0])/newPositions[0][1]]
        for i in range(1, len(newPositions)):
            time = (target - newPositions[i][0])/newPositions[i][1]
            if time > arr[-1]:
                arr.append(time)
        return len(arr)
            
                
            
            
            
            
        