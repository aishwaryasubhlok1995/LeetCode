class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroidStack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            while asteroidStack and asteroids[i] < 0 and asteroidStack[-1] > 0:
                if abs(asteroidStack[-1]) < abs(asteroids[i]):
                    asteroidStack.pop()
                elif abs(asteroidStack[-1]) == abs(asteroids[i]):
                    asteroidStack.pop()
                    break
                else:
                    break
            else:
                asteroidStack.append(asteroids[i])
        return asteroidStack
                
                
                